#!/usr/bin/python

# Submission script for parallel processing of Morris' .gz files on lxplus
# For a new dataset, make sure the range of integers below matches the file names

import os, sys
import subprocess
import argparse

# Main method                                                                          
def main():

    os.system('mkdir -p logs')

    num_nodes = 20
    for i in range(num_nodes):
        # Recreate the condor submission file                                                                   
        subfile = "logs/d"+str(i)+".sub"
        if os.path.isfile(subfile):
            os.remove(subfile)

        f = open(subfile,"w")
        
        f.write("universe                = vanilla \n")
        f.write("executable              = run_MC_2023.sh \n")
        f.write("Proxy_path            = /afs/cern.ch/user/d/dshekar/private/x509up_u154072\n")
        f.write("arguments             = $(ClusterId) $(ProcId) x509up_u154072\n")
        f.write("should_Transfer_Files = YES\n")
        # f.write("request_memory          = 6000 \n")
        f.write("transfer_input_files  = /afs/cern.ch/user/d/dshekar/private/mcSamples/ZH_HWW_Z2L/step2/ZH_Hto2W_Zto2L_M-125_TuneCP5_13p6TeV_powheg-minlo-fragment.py, $(Proxy_path), /afs/cern.ch/user/d/dshekar/private/mcSamples/ZH_HWW_Z2L/step2/update_paths.py\n")
        f.write("transfer_output_files   = \"\" \n")
        f.write("output                  = logs/$(ClusterId).$(ProcId).out \n")
        f.write("error                   = logs/$(ClusterId).$(ProcId).err \n")
        f.write("log                     = logs/$(ClusterId).$(ProcId).log \n")
        f.write("MY.SingularityImage   = \"/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/batch-team/containers/plusbatch/el8-full:latest\"\n")
        
        # Job flavour determines job wall time                                                                  
        # https://batchdocs.web.cern.ch/local/submit.html#job-flavours                                          
        f.write("+JobFlavour             = \"testmatch\" \n")
        f.write("queue \n")
        
        f.close()
    
        # submit the job                                                                                        
        os.system("condor_submit " + subfile)
    
    return 

if __name__ == "__main__":
    main()
