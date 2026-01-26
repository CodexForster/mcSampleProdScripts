import CRABClient
from CRABClient.UserUtilities import config 

config = config()

config.section_("General")
config.General.requestName = 'Jan2026_MC_for_BDT'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
# config.JobType.pluginName = 'PrivateMC'
config.JobType.scriptExe = 'run_MC_2022.sh' # File to run
config.JobType.inputFiles = ['/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/HIG-Run3Summer22wmLHEGS-02385-fragment.py', '/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/ZH_HWW_Z2L_centralSample/step2/update_paths.py']

# config.section_("Data")
# config.Data.outputPrimaryDataset = 'testName1'
# config.Data.splitting = 'EventBased'
# config.Data.unitsPerJob = 10 # each CRAB job will produce 'unitsPerJob' number of events
# NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line
# config.Data.totalUnits = config.Data.unitsPerJob * NJOBS # total number of events to generate/process
# config.Data.publication = True
# config.Data.outputDatasetTag = 'Jan2026_MC_for_BDT_ZH_HWW_Z2L'

config.section_("Site")
config.Site.storageSite = 'T2_US_Purdue' 