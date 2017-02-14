from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'PAMB1_cumu_eff_v3'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumu_pPb16_MB_eff_v2.py'
config.Data.inputDataset = '/PAMinimumBias1/PARun2016C-PromptReco-v1/AOD'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = '/store/user/qwang/cumu/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/HI/Cert_285479-285832_HI8TeV_PromptReco_pPb_Collisions16_JSON_NoL1T.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
config.Site.ignoreGlobalBlacklist = True
config.Data.allowNonValidInputDataset = True
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

### sysTight
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_tight.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### sysLoose
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_loose.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### syVzNarrow
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_narrow.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
### syVzWide
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_wide.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#







### 2
config.Data.inputDataset = '/PAMinimumBias2/PARun2016C-PromptReco-v1/AOD'

config.General.requestName = 'PAMB2_cumu_eff_v3'
config.JobType.psetName = 'qwcumu_pPb16_MB_eff_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


### sysTight
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_tight.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### sysLoose
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_loose.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

### syVzNarrow
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_narrow.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#### syVzWide
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_wide.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)



### 3
config.Data.inputDataset = '/PAMinimumBias3/PARun2016C-PromptReco-v1/AOD'


config.General.requestName = 'PAMB3_cumu_eff_v3'
config.JobType.psetName = 'qwcumu_pPb16_MB_eff_v2.py'
config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v2.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


#### sysTight
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_tight.root']
##try:
##        crabCommand('submit', config = config)
##except HTTPException as hte:
##        print "Failed submitting task: %s" % (hte.headers)
##except ClientException as cle:
##        print "Failed submitting task: %s" % (cle)
#
#### sysLoose
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v3_loose.root']
##try:
##        crabCommand('submit', config = config)
##except HTTPException as hte:
##        print "Failed submitting task: %s" % (hte.headers)
##except ClientException as cle:
##        print "Failed submitting task: %s" % (cle)
#
#### syVzNarrow
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_narrow.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#### syVzWide
#config.JobType.inputFiles = ['Hijing_8TeV_MB_eff_v4_wide.root']
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#
