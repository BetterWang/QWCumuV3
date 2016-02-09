import FWCore.ParameterSet.Config as cms

process = cms.Process("CumuV3")

process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#process.load('Configuration.StandardSequences.Reconstruction_cff')
#process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
#process.load('Configuration.EventContent.EventContentHeavyIons_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

#fN = cms.untracked.vstring();
#for line in open('flist').read().splitlines():
#	fN.append('file:'+line);
#
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:pPb_HM_100.root")
)

#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#JSONfile = 'Cert_210498-211631_HI_PromptReco_Collisions13_JSON_v2.txt'
#myLumis = LumiList.LumiList(filename = JSONfile).getCMSSWString().split(',')
#process.source.lumisToProcess.extend(myLumis)
#
#
import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltHM60 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM60.HLTPaths = [
	"HLT_PixelTracks_Multiplicity60_v*"
]
process.hltHM60.andOr = cms.bool(True)
process.hltHM60.throw = cms.bool(False)

process.hltHM85 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM85.HLTPaths = [
	"HLT_PixelTracks_Multiplicity60_v*",
	"HLT_PixelTracks_Multiplicity85_v*"
]
process.hltHM85.andOr = cms.bool(True)
process.hltHM85.throw = cms.bool(False)

process.hltHM135 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM135.HLTPaths = [
	"HLT_PixelTracks_Multiplicity60_v*",
	"HLT_PixelTracks_Multiplicity85_v*",
	"HLT_PixelTracks_Multiplicity110_v*",
	"HLT_PixelTracks_Multiplicity135_v*"
]
process.hltHM135.andOr = cms.bool(True)
process.hltHM135.throw = cms.bool(False)



process.cumu60 = cms.EDAnalyzer('QWCumuV3'
	, tracks_ = cms.untracked.InputTag('generalTracks')
	, centrality_ = cms.InputTag("centralityBin", "HFtowers")
	, chi2_ = cms.untracked.double(40.)
	, vertexSrc_ = cms.untracked.InputTag('offlinePrimaryVertices', "")
	, rfpptmin_ = cms.untracked.double(0.3)
	, rfpptmax_ = cms.untracked.double(3.0)
	, rfpmineta_ = cms.untracked.double(-2.4)
	, rfpmaxeta_ = cms.untracked.double(2.4)
	, bPhiEta_ = cms.untracked.bool(True)
	, bCentNoff_ = cms.untracked.bool(True)
	, poimineta_ = cms.untracked.double(-2.4)
	, poimaxeta_ = cms.untracked.double(2.4)
	, poiptmin_ = cms.untracked.double(0.3)
	, poiptmax_ = cms.untracked.double(3.0)
	, pterrorpt_ = cms.untracked.double(0.1)
	, Noffmin_ = cms.untracked.int32(60)
	, Noffmax_ = cms.untracked.int32(105)
#	, fweight_ = cms.untracked.InputTag('TrackCorrections_HIJING_538_OFFICIAL_Mar24.root')
	, bEff_ = cms.untracked.bool(False)
	, cmode_ = cms.untracked.int32(1)
	, bFlipEta_ = cms.untracked.bool(False)
	, bEP = cms.untracked.bool(False)
	, EPlvl_ = cms.untracked.int32(0)
	, bCaloMaching = cms.untracked.bool(False)
	, reso = cms.untracked.double(0.2)
        , algoParameters = cms.vint32(4,5,6,7)
	, pfTag = cms.untracked.InputTag('particleFlowTmp')
)

process.cumu85 = process.cumu60.clone()
process.cumu85.Noffmin_ = cms.untracked.int32(105)
process.cumu85.Noffmax_ = cms.untracked.int32(130)

process.cumu135 = process.cumu60.clone()
process.cumu135.Noffmin_ = cms.untracked.int32(130)
process.cumu135.Noffmax_ = cms.untracked.int32(500)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)

#process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')

#process.eventSelection = cms.Sequence(
#        process.hfCoincFilter3
#        + process.primaryVertexFilter
#)
#
#process.p = cms.Path(process.PAcollisionEventSelection*process.pACentrality*process.cumulant)
process.p60 = cms.Path(process.hltHM60*process.cumu60)
process.p85 = cms.Path(process.hltHM85*process.cumu85)
process.p135 = cms.Path(process.hltHM135*process.cumu135)

process.schedule = cms.Schedule(
	process.p60,
	process.p85,
	process.p135,
)
