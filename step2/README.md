## Before submitting condor jobs
https://batchdocs.web.cern.ch/local/myschedd.html

This can help user jumping to the schedd that has less jobs.
`myschedd bump`

## Move your x509 proxy to your lxplus private area
https://batchdocs.web.cern.ch/tutorial/exercise2e_proxy.html

## How to run
usage: submit.py [-h] --path PATH --hadronizer HADRONIZER --proxypath PROXYPATH --eospath EOSPATH [--nevt NEVT] [--year YEAR] [--dryrun]

Example:

python3 submit.py --path /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/vbfhToWW2L2Nu/CMSSW_13_0_13/src/genproductions_scripts/bin/Powheg/VBF_H_el8_amd64_gcc11_CMSSW_13_0_13_VBFHToWW2L2Nu.tgz --hadronizer /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --proxypath /afs/cern.ch/user/d/dshekar/private/x509up_u154072 --eospath root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/ --backup https://cernbox.cern.ch/files/spaces/eos/user/d/dshekar/mcSample/ --nevt 10 --year 2023

## I think incorrect: python3 submit.py --path ./ --hadronizer /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --proxypath /afs/cern.ch/user/d/dshekar/private/x509up_u154072 --eospath root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/ --nevt 10 --year 2023

options:
*  -h, --help              show this help message and exit
*  --path PATH             Input path to LHE files
*  --hadronizer HADRONIZER Hadronizer file
*  --proxypath PROXYPATH   Full AFS path to your x509 proxy
*  --eospath EOSPATH       EOS path to store NanoAODs
*  --nevt NEVT             Number of events to produce, default = 500
*  --year YEAR             Year for MC production
*  --dryrun                Print bash, and jdl instead of submitting job