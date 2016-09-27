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
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

#fN = cms.untracked.vstring();
#for line in open('flist').read().splitlines():
#	fN.append('file:'+line);
#
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/PbPb_HIMB3_AOD.root")
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

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIL1MinimumBiasHF2AND*",
	"HLT_HIL1MinimumBiasHF1AND*",
]
process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)


process.cumulantMB = cms.EDAnalyzer('QWCumuV3'
	, tracks_ = cms.untracked.InputTag('hiGeneralAndPixelTracks')
	, centrality_ = cms.InputTag("centralityBin", "HFtowers")
	, vertexSrc_ = cms.untracked.InputTag('hiSelectedVertex', "")
	, rfpptmin_ = cms.untracked.double(0.3)
	, rfpptmax_ = cms.untracked.double(3.0)
	, rfpmineta_ = cms.untracked.double(-2.4)
	, rfpmaxeta_ = cms.untracked.double(2.4)
	, bPhiEta_ = cms.untracked.bool(True)
	, bCentNoff_ = cms.untracked.bool(False)
	, poimineta_ = cms.untracked.double(-2.4)
	, poimaxeta_ = cms.untracked.double(2.4)
	, poiptmin_ = cms.untracked.double(0.3)
	, poiptmax_ = cms.untracked.double(10)
	, pterrorpt_ = cms.untracked.double(0.1)
	, Noffmin_ = cms.untracked.int32(0)
	, Noffmax_ = cms.untracked.int32(5000)
	, fweight_ = cms.untracked.InputTag('EffCorrectionsPixel_TT_pt_0_10_v2.root')
	, bEff_ = cms.untracked.bool(True)
	, cmode_ = cms.untracked.int32(1)
	, bFlipEta_ = cms.untracked.bool(False)
	, bEP = cms.untracked.bool(False)
	, EPlvl_ = cms.untracked.int32(0)
	, bCaloMaching = cms.untracked.bool(False)
	, reso = cms.untracked.double(0.5)
	, pfTag = cms.untracked.InputTag('particleFlowTmp')
	, b2PartGap = cms.untracked.bool(True)
	, dEtaGap = cms.untracked.double(2.0)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.clusterCompatibilityFilter.clusterPars = cms.vdouble(0.0,0.006)

process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
        + process.clusterCompatibilityFilter
)

process.ana = cms.Path(process.hltMB*process.eventSelection*process.centralityBin*process.cumulantMB)

process.schedule = cms.Schedule(
	process.ana,
)
