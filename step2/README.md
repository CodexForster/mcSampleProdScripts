## Generate x509 proxy and move to your lxplus private area
Initiate voms with a command like: voms-proxy-init --rfc --voms cms -valid 192:00.
Resources: https://www.hep.wisc.edu/cms/comp/basicgrid.html, https://batchdocs.web.cern.ch/tutorial/exercise2e_proxy.html.

## Submitting jobs via submit.py
Update the relevant paths and MC parameters in run_MC_202X.sh and submit.py.

usage: 'python3 submit.py'

Please note that the 2022 job submission uses the fragment file used by the central MC campaign from https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/HIG-Run3Summer22wmLHEGS-02385.

## Using longsubmit.py job file [DEPRECIATED]
usage: 'longsubmit.py [-h] --path PATH --hadronizer HADRONIZER --proxypath PROXYPATH --eospath EOSPATH [--nevt NEVT] [--year YEAR] [--dryrun]'

Example:
'''
python3 longsubmit.py --path /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/vbfhToWW2L2Nu/CMSSW_13_0_13/src/genproductions_scripts/bin/Powheg/VBF_H_el8_amd64_gcc11_CMSSW_13_0_13_VBFHToWW2L2Nu.tgz --hadronizer /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --proxypath /afs/cern.ch/user/d/dshekar/private/x509up_u154072 --eospath root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/ --backup https://cernbox.cern.ch/files/spaces/eos/user/d/dshekar/mcSample/ --nevt 10 --year 2023 --pyedits /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/mcSampleProdScripts/step2/update_paths.py  --premix_file_path /eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/
'''

# I think incorrect: python3 longsubmit.py --path ./ --hadronizer /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --proxypath /afs/cern.ch/user/d/dshekar/private/x509up_u154072 --eospath root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/ --nevt 10 --year 2023

options:
*  -h, --help              show this help message and exit
*  --path PATH             Input path to LHE files
*  --hadronizer HADRONIZER Hadronizer file
*  --proxypath PROXYPATH   Full AFS path to your x509 proxy
*  --eospath EOSPATH       EOS path to store NanoAODs
*  --nevt NEVT             Number of events to produce, default = 500
*  --year YEAR             Year for MC production
*  --dryrun                Print bash, and jdl instead of submitting job