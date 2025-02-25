import json
import argparse
import os
from jinja2 import Template
from pathlib import Path

def load_bash_script(direct_copy):

    if direct_copy:
        template = """#!/bin/bash
mkdir temp_{{ random_seed }}
ls -ltrh
tar -axf {{ input }} -C temp_{{ random_seed }}
echo ""
rm {{ input }}
ls -ltrh

### Make LHE and change output file name
cd temp_{{ random_seed }}
./runcmsgrid.sh {{ nevt }} {{ random_seed }} {{ ncpu }}
mv cmsgrid_final.lhe ../cmsgrid_final_{{ random_seed }}.lhe
cd ../

### Copy output
xrdcp cmsgrid_final_{{ random_seed }}.lhe root://eosuser.cern.ch//eos/user/{{ cernbox_path }}

### Clear directory
rm -r temp_{{ random_seed }}
rm cmsgrid_final_{{ random_seed }}.lhe
ls -ltrh
"""

    else:
        template="""#!/bin/bash
### Untar gridpack
mkdir temp_{{ random_seed }}
ls -ltrh
tar -axf {{ input }} -C temp_{{ random_seed }}
echo ""
rm {{ input }}
ls -ltrh

### Make LHE and change output file name
cd temp_{{ random_seed }}
./runcmsgrid.sh {{ nevt }} {{ random_seed }} {{ ncpu }}
mv cmsgrid_final.lhe ../cmsgrid_final_{{ random_seed }}.lhe
cd ../

### Clear directory
rm -r temp_{{ random_seed }}
ls -ltrh
"""
    return template

def load_jdl_script(direct_copy, run_dir):
    if direct_copy:
        jdl = """universe              = vanilla
executable            = $(filename)
transfer_Input_Files  = {1}
output                = {0}/$(ClusterId).$(ProcId).stdout
error                 = {0}/$(ClusterId).$(ProcId).stderr
log                   = {0}/$(ClusterId).$(ProcId).log
+JobFlavour           = "longlunch"
queue filename matching files {2}/*.sh
""".format(str(log_dir), args.input, run_dir.name)

    else:
        jdl = """universe              = vanilla
executable            = $(filename)
should_Transfer_Files = YES
whenToTransferOutput  = ON_EXIT
transfer_Input_Files  = {1}
output                = {0}/$(ClusterId).$(ProcId).stdout
error                 = {0}/$(ClusterId).$(ProcId).stderr
log                   = {0}/$(ClusterId).$(ProcId).log
MY.XRDCP_CREATE_DIR   = True
output_destination    = root://eosuser.cern.ch//eos/user/{3}/{4}/{5}
+JobFlavour           = "longlunch"
queue filename matching files {2}/*.sh
""".format(str(log_dir), args.input, run_dir.name, os.getlogin()[0], os.getlogin(), args.outdir)

    return jdl

def make_jobs(args, base_dir):

    run_scripts_dir = base_dir / 'run_scripts'
    run_scripts_dir.mkdir(exist_ok=True)

    ### Clean run_scripts_dir
    if run_scripts_dir.exists() and run_scripts_dir.is_dir():
        for item in run_scripts_dir.iterdir():
            if item.is_file():
                item.unlink()

    ### Make output directory manually when direct_copy option is on
    if args.direct_copy:
        out_dir_base = Path(f'/eos/user/{os.getlogin()[0]}/{os.getlogin()}/{args.outdir}')
        out_dir_base.mkdir(exist_ok=False)

    bash_template = load_bash_script(args.direct_copy)
    options = {
            'input': args.input,
            'nevt': args.nevt,
            'ncpu': args.ncpu,
            }

    if args.direct_copy:
        options['cernbox_path'] = f'{os.getlogin()[0]}/{os.getlogin()}/{args.outdir}'

    for i in range(args.njobs):
        original_random_num = int.from_bytes(os.urandom(4), byteorder='little')
        # Trim the last two characters if the seed is too long for your purpose
        random_seed = int(str(original_random_num)[:-2]) if len(str(original_random_num)) > 2 else original_random_num

        options['random_seed'] = random_seed

        bash_script = Template(bash_template).render(options)
        with open(run_scripts_dir / f'run_LHE_{random_seed}.sh','w') as bashfile:
            bashfile.write(bash_script)

    jdl = load_jdl_script(args.direct_copy, run_scripts_dir)

    with open(f'condor_LHE.jdl','w') as jdlfile:
        jdlfile.write(jdl)

    if args.dryrun:
        print('\n=========== Bash file ===========')
        for item in run_scripts_dir.iterdir():
            os.system(f'cat {item}')
            break
        print()
        print()
        print('=========== JDL file ===========')
        os.system('cat condor_LHE.jdl')
    else:
        os.system(f'condor_submit condor_LHE.jdl')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input",  dest="input",  required = True,  help="Input gridpack", type=str)
    parser.add_argument("--nevt",   dest="nevt",   default=500,      help="Number of events to produce, default = 500", type=int)
    parser.add_argument("--ncpu",   dest="ncpu",   default=1,        help="Number of cpu for LHE production, default = 1", type=int)
    parser.add_argument("--njobs",  dest="njobs",  default=300,      help="Number LHE outputs, default = 300", type=int)
    parser.add_argument("--outdir", dest="outdir", default='output', help="Name for the output directory, default = output", type=str)
    parser.add_argument("--direct_copy", dest="direct_copy", action="store_true", help="Copy LHE output by using xrdcp command")
    parser.add_argument("--dryrun", dest="dryrun", action="store_true", help="Print bash, and jdl instead of submitting job")

    args = parser.parse_args()

    current_dir = Path('./')
    log_dir_name = 'condor_logs_lhe_production'
    log_dir = current_dir / log_dir_name
    log_dir.mkdir(exist_ok=True)

    if log_dir.exists():
        os.system(f'rm {log_dir_name}/*log')
        os.system(f'rm {log_dir_name}/*stdout')
        os.system(f'rm {log_dir_name}/*stderr')
        os.system(f'ls {log_dir_name}/*log | wc -l')

    make_jobs(args, current_dir)
