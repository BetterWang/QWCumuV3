from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'Pythia8_Dijet15'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_PYTHIA_QCD_pthat_rfp24_poieta10_cent_noacc_noeff_Prompt_cm1.py'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet15_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
#config.Data.lumiMask = 'json_DCSONLY.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#


config.General.requestName = 'Pythia8_Dijet30'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet30_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#

config.General.requestName = 'Pythia8_Dijet50'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet50_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#



config.General.requestName = 'Pythia8_Dijet80'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)




config.General.requestName = 'Pythia8_Dijet120'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet120_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



config.General.requestName = 'Pythia8_Dijet170'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet170_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)




config.General.requestName = 'Pythia8_Dijet220'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet220_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



config.General.requestName = 'Pythia8_Dijet280'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet280_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'Pythia8_Dijet370'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet370_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)




config.General.requestName = 'Pythia8_Dijet460'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet460_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)




config.General.requestName = 'Pythia8_Dijet540'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet540_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)



#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet15_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet30_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet50_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet120_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet170_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet220_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet280_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet370_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet460_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
#/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet540_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER
