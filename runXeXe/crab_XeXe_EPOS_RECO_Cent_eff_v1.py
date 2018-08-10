from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'XeXe1_CumuV3_EPOS_RECO_v1'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuV3_XeXe_EPOS_RECO_Cent_eff_v1.py'
config.Data.inputDataset = '/XeXeMinBias_5p44TeV-ReggeGribovPartonMC_EposLHC/HINXeXeFall17DR-94X_mc2017_realistic_ForXeXe_v7-v1/GEN-SIM-RECO'
config.JobType.inputFiles = ['XeXe_eff_table_94x_cent.root']
config.JobType.maxJobRuntimeMin = 2500
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/XeXe/'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/HI/Cert_304899-304907_5TeV_PromptReco_XeXe_Collisions17_JSON.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
config.Site.ignoreGlobalBlacklist = True
#config.Data.allowNonValidInputDataset = True
try:
	crabCommand('submit', config = config)
except HTTPException as hte:
	print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
	print "Failed submitting task: %s" % (cle)


