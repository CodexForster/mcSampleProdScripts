from cmsdriver_commands import command_dict
from jinja2 import Template
from os import getlogin

cmssw_mc_template = """#!/bin/bash

### Computing environments
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
export BASEDIR=`pwd`

### Copy input file
xrdcp -r root://eosuser.cern.ch/{{ path}}/{{ input }} ./

ls -ltrh

### LHE step
scram p {{ lhe_cmssw }}
cd {{ lhe_cmssw }}/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
mv ${BASEDIR}/monoWprime_hadronizer.py Configuration/GenProduction/python/

ls -ltrh

scram b

{{ lhe_command }}
cmsRun lhe_cfg.py

### GEN step
{{ gen_command }}
cmsRun gen_cfg.py

### SIM step
cd ${BASEDIR}

scram p {{ sim_cmssw }}
cd {{ sim_cmssw }}/src
eval `scram runtime -sh`

### Move file

{{ sim_command }}
cmsRun sim_cfg.py

### DIGI-Premix step

{{ digi_command }}
cmsRun digi_cfg.py

### HLT step
cd ${BASEDIR}

scram p {{ hlt_cmssw }}
cd {{ hlt_cmssw }}/src
eval `scram runtime -sh`

{{ hlt_command }}
cmsRun hlt_cfg.py

### RECO step
cd ${BASEDIR}
cd {{ reco_cmssw }}/src
eval `scram runtime -sh`

{{ reco_command }}
cmsRun reco_cfg.py

### MINIAOD step
cd ${BASEDIR}

scram p {{ miniaod_cmssw }}
cd {{ miniaod_cmssw }}/src
eval `scram runtime -sh`

{{ miniaod_command }}
cmsRun miniaod_cfg.py

### NANOAOD step
cd ${BASEDIR}

scram p {{ nanoaod_cmssw }}
cd {{ nanoaod_cmssw }}/src
eval `scram runtime -sh`

{{ nanoaod_command }}
cmsRun nanoaod_cfg.py

### Copy NanoAOD file to storage
mv nanoaod.root nanoaod_$(ClusterId)_$(ProcId).root
"""

def make_template(eos_path: str, year: str, nevt: int = 10):
    cmd_list = command_dict[year]

    misc_options = {
        'nevt': nevt
    }

    cmd_options = {
        'path': eos_path,
        'input': '${1}',
        'lhe_cmssw': cmd_list['LHE']['cmssw'],
        'lhe_command': Template(cmd_list['LHE']['command']).render(misc_options),
        'gen_command': Template(cmd_list['GEN']['command']).render(misc_options),
        'sim_cmssw': cmd_list['SIM']['cmssw'],
        'sim_command': Template(cmd_list['SIM']['command']).render(misc_options),
        'digi_command': Template(cmd_list['DIGI']['command']).render(misc_options),
        'hlt_cmssw': cmd_list['HLT']['cmssw'],
        'hlt_command': Template(cmd_list['HLT']['command']).render(misc_options),
        'reco_cmssw': cmd_list['RECO']['cmssw'],
        'reco_command': Template(cmd_list['RECO']['command']).render(misc_options),
        'miniaod_cmssw': cmd_list['MINI']['cmssw'],
        'miniaod_command': Template(cmd_list['MINI']['command']).render(misc_options),
        'nanoaod_cmssw': cmd_list['NANO']['cmssw'],
        'nanoaod_command': Template(cmd_list['NANO']['command']).render(misc_options),
    }

    bash_script = Template(cmssw_mc_template).render(cmd_options)
    return bash_script
