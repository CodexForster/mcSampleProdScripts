from bash_template import make_template
import argparse
import os
from pathlib import Path
import re

def extract_after_dbs(filename):
    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'dbs:(/\S+)', line)
            if match:
                return match.group(1)  # The string after 'dbs:'

def replace_line_in_file(filename, match_string, new_line):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if match_string in line:
                file.write(new_line + '\n')  # insert before match
            file.write(line)  # write the original line

######################################
def make_jobs(args, base_dir):
    files = sorted(Path(args.path).glob('cms*lhe'))

    # listfile = base_dir / 'input_list.txt'
    # with open(listfile, 'w') as listfile:
    #     for ifile in files:
    #         fname = ifile.name
    #         save_string = f"{ifile}, {fname}"
    #         listfile.write(save_string + '\n')

    bash_template = make_template(args.eospath, str(args.year), args.nevt, args.backup)
    with open(f'run_MC_{args.year}.sh','w') as bashfile:
        bashfile.write(bash_template)
    updating_premix_files = """location=$(dasgoclient -query="file dataset={0}" | head -n 1 | sed 's/\/[^/]*\/[^/]*$//')
full_path="/eos/cms$location/"
find "$full_path" -type f > find_query_list_test.txt
sed -i "s|/eos/cms/|/|g; s|root$|root|g" find_query_list_test.txt
python3 update_paths.py""".format(extract_after_dbs(f'run_MC_{args.year}.sh'))
    replace_line_in_file(f'run_MC_{args.year}.sh', 'cmsRun DRPremix_cfg.py', updating_premix_files)

    ### Condor Job Flavour = Maximum wall time
    ### espresso     = 20 minutes
    ### microcentury = 1 hour
    ### longlunch    = 2 hours
    ### workday      = 8 hours
    ### tomorrow     = 1 day
    ### testmatch    = 3 days
    ### nextweek     = 1 week

    jdl = """universe              = vanilla
executable            = {1}
Proxy_path            = {3}
arguments             = $(ClusterId) $(ProcId) {4}
should_Transfer_Files = YES
transfer_input_files  = {2},$(Proxy_path)
transfer_output_files = ""
output                = {0}/$(ClusterId).$(ProcId).stdout
error                 = {0}/$(ClusterId).$(ProcId).stderr
log                   = {0}/$(ClusterId).$(ProcId).log
MY.SingularityImage   = "/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/batch-team/containers/plusbatch/el8-full:latest"
+JobFlavour           = "workday"
queue 1
""".format(log_dir.name, f'run_MC_{args.year}.sh', args.hadronizer, args.proxypath, proxyfilename)

    with open(f'condor_MC.jdl','w') as jdlfile:
        jdlfile.write(jdl)

    if args.dryrun:
        print('\n=========== Bash file ===========')
        os.system(f'cat run_MC_{args.year}.sh')
        print()
        print()
        print('=========== JDL file ===========')
        os.system('cat condor_MC.jdl')
    else:
        os.system('condor_submit condor_MC.jdl')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--path",       dest="path",        required = True,  help="Input path to LHE files", type=str)
    parser.add_argument("--hadronizer", dest="hadronizer",  required = True,  help="Hadronizer file")
    parser.add_argument("--proxypath",  dest="proxypath",   required = True,  help="Full AFS path to your x509 proxy", type=str)
    parser.add_argument("--eospath",    dest="eospath",     required = True,  help="EOS path to store NanoAODs", type=str)
    parser.add_argument("--backup",     dest="backup",      default="",       help="Extra path to save NanoAOD", type=str)
    parser.add_argument("--nevt",       dest="nevt",        default=10,      help="Number of events to produce, default = 10", type=int)
    parser.add_argument("--year",       dest="year",        default=2023,     help="Year for MC production")
    parser.add_argument("--lpc",    dest="lpc",    action="store_true", help="Submit condor jobs on LPC server")
    parser.add_argument("--dryrun", dest="dryrun", action="store_true", help="Print bash, and jdl instead of submitting job")

    args = parser.parse_args()
    # expecting a proxypath like /afs/cern.ch/user/d/dshekar/public/x509up_u154072
    proxyfilename = args.proxypath.split('/')[-1]

    base_dir = Path('./')
    log_dir_name = 'condor_logs_mc_production'
    log_dir = base_dir / log_dir_name

    if log_dir.exists():
        os.system(f'rm {log_dir_name}/*log')
        os.system(f'rm {log_dir_name}/*stdout')
        os.system(f'rm {log_dir_name}/*stderr')
        os.system(f'ls {log_dir_name}/*log | wc -l')

    log_dir.mkdir(exist_ok=True)

    make_jobs(args, base_dir)


