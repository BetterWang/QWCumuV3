import FWCore.ParameterSet.Config as cms

process = cms.Process("GEN")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.AfterBurnerGenerator_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(200000))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("EmptySource")

process.generator = cms.EDFilter("HijingGeneratorFilter",
		rotateEventPlane = cms.bool(True),
		frame = cms.string('CMS     '),
		targ = cms.string('A       '),
		izp = cms.int32(82),
		bMin = cms.double(5),
		izt = cms.int32(82),
		proj = cms.string('A       '),
		comEnergy = cms.double(5023.0),
		iat = cms.int32(208),
		bMax = cms.double(15),
		iap = cms.int32(208)
		)

configurationMetadata = cms.untracked.PSet(
		version = cms.untracked.string('$Revision: 1.3 $'),
		annotation = cms.untracked.string('HIJING generator'),
		name = cms.untracked.string('$Source: QW $')
		)

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('keep *'),
    fileName = cms.untracked.string('Hijing.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

process.AftBurner.modv1 = cms.InputTag("0.0")
#process.AftBurner.modv2 = cms.InputTag("fEllP_8pct_v2")
process.AftBurner.modv2 = cms.InputTag("pBG_4pct_v2")
#process.AftBurner.modv3 = cms.InputTag("pBG_2pct_v3")
process.AftBurner.modmethod = cms.int32(2)

################ comment this out to run without QWNtrkOfflineProducer
process.QWEvent = cms.EDProducer("QWGenEventProducer",
		trackSrc  = cms.untracked.InputTag("genParticles"),
		ptMin = cms.untracked.double(0.3),
		ptMax = cms.untracked.double(3.0),
		Etamin = cms.untracked.double(-2.4),
		Etamax = cms.untracked.double(2.4)
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

process.TFileService = cms.Service("TFileService",
		fileName = cms.string('cumu.root')
		)

process.centralityBin = cms.EDProducer('QWIntProducer',
		src = cms.untracked.int32(2)
		)

process.cumulantMB = cms.EDAnalyzer('QWCumuV3'
	, trackEta = cms.untracked.InputTag('QWEvent', "eta")
	, trackPhi = cms.untracked.InputTag('QWEvent', "phi")
	, trackPt = cms.untracked.InputTag('QWEvent', "pt")
	, trackWeight = cms.untracked.InputTag('QWEvent', "weight")
	, trackCharge = cms.untracked.InputTag('QWEvent', "charge")
	, vertexZ = cms.untracked.InputTag('QWEvent', "vz")
	, centrality = cms.untracked.InputTag('centralityBin')
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

process.hepmc = cms.EDProducer('QWHepMCProducer',
		src = cms.untracked.InputTag('generator')
		)

process.Ntrk = cms.EDProducer('QWVectCounter',
		src = cms.untracked.InputTag('QWEvent', 'phi')
		)

process.NtrkVsB = cms.EDAnalyzer('QWCorrAnalyzer',
		srcX = cms.untracked.InputTag('hepmc', 'b'),
		srcY = cms.untracked.InputTag('Ntrk'),
		NbinsX = cms.untracked.int32(100),
		hstartX = cms.untracked.double(0.),
		hendX = cms.untracked.double(15),
		NbinsY = cms.untracked.int32(100),
		hstartY = cms.untracked.double(0.),
		hendY = cms.untracked.double(3000)
		)
#process.pgen = cms.Sequence(cms.SequencePlaceholder("randomEngineStateProducer")+process.AfterBurner+process.GeneInfo + process.QWEvent + process.vectPhi + process.centralityBin + process.cumulantMB)
process.pgen = cms.Sequence(cms.SequencePlaceholder("randomEngineStateProducer")+process.GeneInfo + process.hepmc + process.QWEvent + process.vectPhi 
		+ process.Ntrk + process.NtrkVsB)
################ comment END
#process.pgen = cms.Sequence(cms.SequencePlaceholder("randomEngineStateProducer")+process.AfterBurner+process.GeneInfo)

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()

process.generation_step = cms.Path(process.pgen)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)


process.schedule = cms.Schedule(
	process.generation_step,
#	process.RAWSIMoutput_step
)


for path in process.paths:
                getattr(process,path)._seq = process.generator * getattr(process,path)._seq

