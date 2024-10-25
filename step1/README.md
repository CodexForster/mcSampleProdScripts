## Before submitting condor jobs
https://batchdocs.web.cern.ch/local/myschedd.html

This can help user jumping to the schedd that has less jobs.
`myschedd bump`

## How to run
usage: submit.py [-h] --input INPUT [--nevt NEVT] [--ncpu NCPU] [--njobs NJOBS] [--outdir OUTDIR] [--dryrun]

optional arguments:
* -h, --help       show this help message and exit
* --input INPUT    Input gridpack
* --nevt NEVT      Number of events to produce, default = 500
* --ncpu NCPU      Number of cpu for LHE production, default = 1
* --njobs NJOBS    Number LHE outputs, default = 300
* --outdir OUTDIR  Name for the output directory, default = output
* --dryrun         Print bash, and jdl instead of submitting job
