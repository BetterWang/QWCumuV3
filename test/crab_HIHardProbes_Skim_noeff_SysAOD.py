from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysCaloAOD_v11'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_poieta10_cent_noeff_sysCalo.py'
#config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
config.Data.inputDataset = '/HIHardProbes/HIRun2015-PromptReco-v1/AOD'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
# sysCalo
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)






config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysTightAOD_v11'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_poieta10_cent_noeff_sysTight.py'
config.Data.lumiMask = 'sysTight.json'
# sysTight
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)









config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysLooseAOD_v11'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_poieta10_cent_noeff_sysLoose.py'
config.Data.lumiMask = 'sysLoose.json'
# sysLoose
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)






config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysVz0AOD_v11'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_poieta10_cent_noeff_sysVz0.py'
config.Data.lumiMask = 'sysVz0.json'
# sysVz0
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)




config.General.requestName = 'HIHardProbes_Skim_cumu_noeff_sysVz1AOD_v11'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIHP_rfp24_poieta10_cent_noeff_sysVz1.py'
config.Data.lumiMask = 'sysVz1.json'
# sysVz1
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


