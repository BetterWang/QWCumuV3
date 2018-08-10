import FWCore.ParameterSet.Config as cms

process = cms.Process("CumuV3")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/himc/HINXeXeFall17GS/XeXeMinBias_5p44TeV-AMPT-withmelt/GEN/GENonly_92X_upgrade2017_realistic_v11-v1/20000/000A8BBE-33D0-E711-8BB1-FA163EEB2766.root")
)


process.cumulantMB = cms.EDAnalyzer('QWCumuV3'
	, trackEta = cms.untracked.InputTag('QWEvent', "eta")
	, trackPhi = cms.untracked.InputTag('QWEvent', "phi")
	, trackPt = cms.untracked.InputTag('QWEvent', "pt")
	, trackWeight = cms.untracked.InputTag('QWEvent', "weight")
	, trackCharge = cms.untracked.InputTag('QWEvent', "charge")
	, vertexZ = cms.untracked.InputTag('QWEvent', "vz")
	, centrality = cms.untracked.InputTag('centralityBin', 'AMPT')
	, minvz = cms.untracked.double(-15.0)
	, maxvz = cms.untracked.double(15.0)
	, rfpmineta = cms.untracked.double(-2.4)
	, rfpmaxeta = cms.untracked.double(2.4)
	, rfpminpt = cms.untracked.double(0.3)
	, rfpmaxpt = cms.untracked.double(3.0)
	, poimineta = cms.untracked.double(-2.4)
	, poimaxeta = cms.untracked.double(2.4)
	, poiminpt = cms.untracked.double(0.3)
	, poimaxpt = cms.untracked.double(10.0)
	, b2PartGap = cms.untracked.bool(True)
	, dEtaGap = cms.untracked.double(2.0)
	, cmode = cms.untracked.int32(1)
	, nvtx = cms.untracked.int32(100)
	, ptBin = cms.untracked.vdouble(0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0)
	, etaBin = cms.untracked.vdouble(-2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4)
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)


process.QWEvent = cms.EDProducer("QWGenEventProducer",
		trackSrc  = cms.untracked.InputTag("genParticles"),
		ptMin = cms.untracked.double(0.3),
		ptMax = cms.untracked.double(10.),
		isPrompt  = cms.untracked.bool(True)
		)

process.QWHIEvent = cms.EDProducer("QWHepMCProducer",
		src = cms.untracked.InputTag("generatorSmeared")
		)

process.centralityBin = cms.EDProducer('QWXeXeB2CentProducer',
                src = cms.untracked.InputTag("QWHIEvent", "b")
		)


# monitoring
process.histCent = cms.EDAnalyzer('QWHistAnalyzer',
		src = cms.untracked.InputTag("centralityBin", 'AMPT'),
		Nbins = cms.untracked.int32(200),
		start = cms.untracked.double(0),
		end = cms.untracked.double(200),
		)


process.vectPhi = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "phi"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(-3.14159265358979323846),
		cend = cms.untracked.double(3.14159265358979323846),
		)

process.vectPt = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "pt"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(0),
		cend = cms.untracked.double(5),
		)

process.vectEta = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "eta"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(-2.5),
		cend = cms.untracked.double(2.5),
		)

process.PhiEta2D = cms.EDAnalyzer('QWVCorrAnalyzer',
		srcX = cms.untracked.InputTag('QWEvent', 'eta'),
		NbinsX = cms.untracked.int32(48),
		hstartX = cms.untracked.double(-2.4),
		hendX = cms.untracked.double(2.4),
		srcY = cms.untracked.InputTag('QWEvent', 'phi'),
		NbinsY = cms.untracked.int32(48),
		hstartY = cms.untracked.double(-3.14159265358979323846),
		hendY = cms.untracked.double(3.14159265358979323846),
		)


process.vectMon = cms.Sequence(process.histCent * process.vectPhi * process.vectPt * process.vectEta * process.PhiEta2D )

process.ana = cms.Path(
		process.QWHIEvent *
		process.centralityBin *
		process.QWEvent *
		process.cumulantMB *
		process.vectMon 
		)

process.RECO = cms.OutputModule("PoolOutputModule",
		outputCommands = cms.untracked.vstring('keep *'),
		SelectEvents = cms.untracked.PSet(
			SelectEvents = cms.vstring('ana')
			),
		fileName = cms.untracked.string('reco.root')
		)

process.out = cms.EndPath(process.RECO)

process.schedule = cms.Schedule(
	process.ana,
)
