from bash_template import make_template
import argparse
import os
from pathlib import Path

def make_jobs(args, base_dir):
    files = sorted(Path(args.path).glob('cms*lhe'))

    listfile = base_dir / 'input_list.txt'
    with open(listfile, 'w') as listfile:
        for ifile in files:
            fname = ifile.name
            save_string = f"{ifile}, {fname}"
            listfile.write(save_string + '\n')

    bash_template = make_template(args.path, str(args.year), args.nevt)
    with open(f'run_MC_{args.year}.sh','w') as bashfile:
        bashfile.write(bash_template)

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
arguments             = $(path) $(fname) $(Proxy_path) $(ClusterId) $(ProcId)
should_Transfer_Files = YES
transfer_input_files  = {2}
transfer_output_files = ""
output                = {0}/$(ClusterId).$(ProcId).stdout
error                 = {0}/$(ClusterId).$(ProcId).stderr
log                   = {0}/$(ClusterId).$(ProcId).log
MY.SingularityImage   = "/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/batch-team/containers/plusbatch/el7-full:latest"
+JobFlavour           = "tomorrow"
queue path,fname from input_list.txt
""".format(log_dir.name, f'run_MC_{args.year}.sh', args.hadronizer, args.proxypath)

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
    parser.add_argument("--nevt",       dest="nevt",        default=500,      help="Number of events to produce, default = 500", type=int)
    parser.add_argument("--year",       dest="year",        default=2018,     help="Year for MC production")
    parser.add_argument("--dryrun", dest="dryrun", action="store_true", help="Print bash, and jdl instead of submitting job")

    args = parser.parse_args()

    base_dir = Path('./')
    log_dir_name = 'condor_logs_mc_production'
    log_dir = base_dir / log_dir_name
    log_dir.mkdir(exist_ok=True)

    if log_dir.exists():
        os.system(f'rm {log_dir_name}/*log')
        os.system(f'rm {log_dir_name}/*stdout')
        os.system(f'rm {log_dir_name}/*stderr')
        os.system(f'ls {log_dir_name}/*log | wc -l')

    make_jobs(args, base_dir)