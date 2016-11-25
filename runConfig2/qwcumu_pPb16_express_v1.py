import FWCore.ParameterSet.Config as cms

process = cms.Process("CumuV3")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/pPb_8_FEVT.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIL1MinimumBiasHF2AND*",
	"HLT_HIL1MinimumBiasHF1AND*",
]
process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)


process.cumulantMB = cms.EDAnalyzer('QWCumuV3'
	, trackEta = cms.untracked.InputTag('QWEvent', "eta")
	, trackPhi = cms.untracked.InputTag('QWEvent', "phi")
	, trackPt = cms.untracked.InputTag('QWEvent', "pt")
	, trackWeight = cms.untracked.InputTag('QWEvent', "weight")
	, trackCharge = cms.untracked.InputTag('QWEvent', "charge")
	, vertexZ = cms.untracked.InputTag('QWEvent', "vz")
	, centrality = cms.untracked.InputTag('Noff')
	, minvz = cms.untracked.double(-15.0)
	, maxvz = cms.untracked.double(15.0)
	, rfpmineta = cms.untracked.double(-2.4)
	, rfpmaxeta = cms.untracked.double(2.4)
	, rfpminpt = cms.untracked.double(0.3)
	, rfpmaxpt = cms.untracked.double(3.0)
	, poimineta = cms.untracked.double(-2.4)
	, poimaxeta = cms.untracked.double(2.4)
	, poiminpt = cms.untracked.double(0.3)
	, poimaxpt = cms.untracked.double(20.0)
	, b2PartGap = cms.untracked.bool(True)
	, dEtaGap = cms.untracked.double(2.0)
	, cmode = cms.untracked.int32(1)
	, nvtx = cms.untracked.int32(100)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)



process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
 applyfilter = cms.untracked.bool(True),
 debugOn = cms.untracked.bool(False),
 numtrack = cms.untracked.uint32(10),
 thresh = cms.untracked.double(0.25)
)


process.eventSelection = cms.Sequence(process.PAprimaryVertexFilter * process.NoScraping * process.pileupVertexFilterCutGplus)

process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')
process.ppNoffFilter0 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(2, 30)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter30 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(30, 60)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter60 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(60, 90)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter90 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(90, 120)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter120 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(120, 150)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter150 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(150, 200)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter200 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(200, 300)
			),
		BinLabel = cms.InputTag("Noff")
		)

process.ppNoffFilter300 = process.centralityFilter.clone(
		selectedBins = cms.vint32(
			*range(300, 500)
			),
		BinLabel = cms.InputTag("Noff")
		)
process.load('PbPb_HIMB5_ppReco_noeff')
process.QWEvent.ptMax = cms.untracked.double(20.0)

process.ana = cms.Path(process.eventSelection*process.Noff*process.QWEvent*process.vectMon*process.cumulantMB)
#process.ana0 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter0*process.QWEvent*process.cumulantMB)
#process.ana30 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter30*process.QWEvent*process.cumulantMB)
#process.ana60 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter60*process.QWEvent*process.cumulantMB)
#process.ana90 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter90*process.QWEvent*process.cumulantMB)
#process.ana120 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter120*process.QWEvent*process.cumulantMB)
#process.ana150 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter150*process.QWEvent*process.cumulantMB)
#process.ana200 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter200*process.QWEvent*process.cumulantMB)
#process.ana300 = cms.Path(process.eventSelection*process.Noff*process.ppNoffFilter300*process.QWEvent*process.cumulantMB)

process.schedule = cms.Schedule(
	process.ana,
)
