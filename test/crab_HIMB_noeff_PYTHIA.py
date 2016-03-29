from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB_noeff_Pythia50'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_PYTHIA.py'
#config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet50_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 50
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)




# Pythia15
config.General.requestName = 'HIMB_noeff_Pythia15'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet15_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



# Pythia30
config.General.requestName = 'HIMB_noeff_Pythia30'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet30_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia80
config.General.requestName = 'HIMB_noeff_Pythia80'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia120
config.General.requestName = 'HIMB_noeff_Pythia120'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet120_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia170
config.General.requestName = 'HIMB_noeff_Pythia170'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet170_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia220
config.General.requestName = 'HIMB_noeff_Pythia220'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet220_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia280
config.General.requestName = 'HIMB_noeff_Pythia280'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet280_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia370
config.General.requestName = 'HIMB_noeff_Pythia370'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet370_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia460
config.General.requestName = 'HIMB_noeff_Pythia460'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet460_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# Pythia540
config.General.requestName = 'HIMB_noeff_Pythia540'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet540_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



