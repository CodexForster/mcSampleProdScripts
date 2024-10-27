## Before submitting condor jobs
https://batchdocs.web.cern.ch/local/myschedd.html

This can help user jumping to the schedd that has less jobs.
`myschedd bump`

## Move your x509 proxy to your lxplus private area
https://batchdocs.web.cern.ch/tutorial/exercise2e_proxy.html

## How to run
usage: submit.py [-h] --path PATH --hadronizer HADRONIZER --proxypath PROXYPATH --eospath EOSPATH [--nevt NEVT] [--year YEAR] [--dryrun]

options:
*  -h, --help              show this help message and exit
*  --path PATH             Input path to LHE files
*  --hadronizer HADRONIZER Hadronizer file
*  --proxypath PROXYPATH   Full AFS path to your x509 proxy
*  --eospath EOSPATH       EOS path to store NanoAODs
*  --nevt NEVT             Number of events to produce, default = 500
*  --year YEAR             Year for MC production
*  --dryrun                Print bash, and jdl instead of submitting job