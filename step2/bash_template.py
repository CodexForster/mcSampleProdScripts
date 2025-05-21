from cmsdriver_commands import command_dict
from jinja2 import Template

cmssw_mc_template = """#!/bin/bash

{{ LC_template }}

############
### Computing environments
############
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh
export BASEDIR=`pwd`
echo "basedir = ${BASEDIR}"

{{ proxy_template }}
echo "DAN "
echo "Argument 0: ${0}"
echo "Argument 1: ${1}"
echo "Argument 2: ${2}"
echo "Argument 3: ${3}"
echo "Argument 4: ${4}"

############
### LHEGS step
############
echo "********** lhegs start **********"
export SCRAM_ARCH={{ lhegs_scram_arch }}
scram p {{ lhegs_cmssw }}
cd {{ lhegs_cmssw }}/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
mv ${BASEDIR}/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py Configuration/GenProduction/python/
# xrdcp root://eosuser.cern.ch/{{ path }} ./ ## Copy input file
echo "path = ${{ path }}"

scram b

{{ lhegs_command }}
cmsRun wmLHEGS_cfg.py
echo "********** LHE End **********"

mv ${BASEDIR}/{{ lhegs_cmssw }}/src/vbfhToWW2L2Nu_LHEGS.root ./

############
### DIGI-Premix step
############
echo "********** DIGI Premix start **********"
{{ drpremix_command }}
cmsRun DRPremix_cfg.py

echo "********** DIGI Premix End **********"

mv ${BASEDIR}/{{ drpremix_cmssw }}/src/vbfhToWW2L2Nu_DRPremix.root ./

############
### AOD step
############
echo "********** AOD start **********"
{{ aod_command }}
cmsRun aod_cfg.py
echo "********** AOD End **********"

### Move file
mv ${BASEDIR}/{{ aod_cmssw }}/src/vbfhToWW2L2Nu_aod.root ./

############
### MINIAOD step
############
echo "********** MINIAOD start **********"
{{ miniaod_command }}
cmsRun miniAOD_cfg.py
echo "********** MINIAOD End **********"

### Move file
mv ${BASEDIR}/{{ miniaod_cmssw }}/src/vbfhToWW2L2Nu_miniaod.root ./

############
### NANOAOD step
############
echo "********** NANOAOD start **********"
{{ nanoaod_command }}
cmsRun nanoAOD_cfg.py
echo "********** NANOAOD End **********"

### Change file name
mv vbfhToWW2L2Nu_nanoAOD.root nanoAOD.root
xrdfs {{ xrootd_protocol }} mkdir -p {{ eos_localpath }}
xrdcp -f nanoAOD.root {{ full_eospath }}/nanoAOD.root

### Backup path to save NanoAOD
{{ cernbox_outpath }}
"""

proxy_template="""
############
### Add x509 proxy
############
export X509_USER_PROXY=${3}
voms-proxy-info -all
voms-proxy-info -all -file ${3}
"""

LC_template = """
############
### Set LANG environments
############
export LC_CTYPE=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
"""


def make_template(eospath: str, year: str, nevt: int = 10, backup: str = "", submit_lpc: bool = False):
    cmd_list = command_dict[year]
    path_list = eospath.split('//')

    cernbox_outpath = f"xrdcp -f nanoaod.root root://eosuser.cern.ch/{backup}/nanoaod.root"
    if backup == "":
        cernbox_outpath = ""

    misc_options = {
        # 'input': '${2}',
        'nevt': nevt
    }
    print("path_list: ", path_list)

    cmd_options = {
        'path': '${1}',
        'xrootd_protocol': f'{path_list[0]}//{path_list[1]}/',
        'eos_localpath': f'/{path_list[2]}/',
        'full_eospath': eospath,
        'cernbox_outpath': cernbox_outpath,
        'lhegs_scram_arch': cmd_list['LHEGS']['scram_arch'],
        'lhegs_cmssw': cmd_list['LHEGS']['cmssw'],
        'lhegs_command': Template(cmd_list['LHEGS']['command']).render(misc_options),
        'drpremix_cmssw': cmd_list['DRPremix']['cmssw'],
        'drpremix_command': Template(cmd_list['DRPremix']['command']).render(misc_options),
        'aod_cmssw': cmd_list['AOD']['cmssw'],
        'aod_command': Template(cmd_list['AOD']['command']).render(misc_options),
        'miniaod_cmssw': cmd_list['MINI']['cmssw'],
        'miniaod_command': Template(cmd_list['MINI']['command']).render(misc_options),
        'nanoaod_cmssw': cmd_list['NANO']['cmssw'],
        'nanoaod_command': Template(cmd_list['NANO']['command']).render(misc_options),
        'proxy_template': proxy_template if not submit_lpc else "",
        'LC_template': LC_template if submit_lpc else "",
        # 'path': '${1}',
        # 'xrootd_protocol': f'{path_list[0]}//{path_list[1]}/',
        # 'eos_localpath': f'/{path_list[2]}/',
        # 'full_eospath': eospath,
        # 'cernbox_outpath': cernbox_outpath,
        # 'lhe_scram_arch': cmd_list['LHE']['scram_arch'],
        # 'lhe_cmssw': cmd_list['LHE']['cmssw'],
        # 'lhe_command': Template(cmd_list['LHE']['command']).render(misc_options),
        # 'gen_command': Template(cmd_list['GEN']['command']).render(misc_options),
        # 'sim_cmssw': cmd_list['SIM']['cmssw'],
        # 'sim_command': Template(cmd_list['SIM']['command']).render(misc_options),
        # 'digi_command': Template(cmd_list['DIGI']['command']).render(misc_options),
        # 'hlt_scram_arch': cmd_list['HLT']['scram_arch'],
        # 'hlt_cmssw': cmd_list['HLT']['cmssw'],
        # 'hlt_command': Template(cmd_list['HLT']['command']).render(misc_options),
        # 'reco_scram_arch': cmd_list['RECO']['scram_arch'],
        # 'reco_cmssw': cmd_list['RECO']['cmssw'],
        # 'reco_command': Template(cmd_list['RECO']['command']).render(misc_options),
        # 'miniaod_cmssw': cmd_list['MINI']['cmssw'],
        # 'miniaod_command': Template(cmd_list['MINI']['command']).render(misc_options),
        # 'nanoaod_cmssw': cmd_list['NANO']['cmssw'],
        # 'nanoaod_command': Template(cmd_list['NANO']['command']).render(misc_options),
        # 'proxy_template': proxy_template if not submit_lpc else "",
        # 'LC_template': LC_template if submit_lpc else "",
    }

    bash_script = Template(cmssw_mc_template).render(cmd_options)
    return bash_script

