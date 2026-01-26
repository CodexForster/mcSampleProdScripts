Resources: https://www.physics.purdue.edu/Tier2/user-info/tutorials/crab3.php, https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial.

## Folder Organization
For the inital attempt, a separate folder was created for each request (wmLHEGS, miniAOD, nanoAOD, etc.) inside which, the correct CMSSW was installed. The files were organized this was to accomodate for producing files in the correct CMSSW versions they were designed to be run in. The CMSSW installation and initial steps can be followed using the scripts within 'centralRequestCommands/'. Explicit commands used can be found in full_terminal_cmds.sh.

## Initializing CRAB and VOMS proxy
Go to your respective source directory of the CMSSW files (depending on which step you're in. Ex - wmLHEGS/miniAOD/etc.). Then run:
'''
cd ~/CRAB_tests/CMSSW_12_3_4/src
cmsenv
git cms-init
source /cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.6/current/el8-x86_64/setup.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init -voms cms -rfc -valid 168:00
'''

## Submitting jobs
crab submit -c crab_config_file.py