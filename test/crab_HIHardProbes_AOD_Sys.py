from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_v13'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2.py'
#config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
config.Data.inputDataset = '/HIHardProbes/HIRun2015-PromptReco-v1/AOD'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 25
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
# default
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)




config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysCalo_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2_sysCalo.py'
# sysCalo
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)





config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysTight_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2_sysTight.py'
## sysTight
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
#








config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysLoose_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2_sysLoose.py'
## sysLoose
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
#





config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysVz0_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2_sysVz0.py'
## sysVz0
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
#



config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysVz1_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2_sysVz1.py'
## sysVz1
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
#


config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysEff_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_v2_sysEff.py'
config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
## sysEff
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
#


