#include "IOMC/ParticleGuns/interface/BaseFlatGunProducer.h"

namespace edm
{
class FlowGunProducer : public BaseFlatGunProducer
{
	public:
		FlowGunProducer(const ParameterSet &pset);
		virtual ~FlowGunProducer();
		virtual void produce(Event & e, const EventSetup& es) override;
	private:
		int	szCluster;
		int	nCluster;
		double	fMinPt;
		double	fMaxPt;

		int		modmethod;
		// 0, flat
		// 1, complete rnd, without non-flow
		// 2, Newton method, with non-flow

		double 		fluct_v1;
		double 		fluct_v2;
		double 		fluct_v3;
		double 		fluct_v4;
		double 		fluct_v5;
		double 		fluct_v6;

		TF1 *		fv1;
		TF1 *		fv2;
		TF1 *		fv3;
		TF1 *		fv4;
		TF1 *		fv5;
		TF1 *		fv6;
		TF1 *		fCluster;

};

FlowGunProducer::FlowGunProducer(const ParameterSet &pset) : BaseFlatGunProducer(pset)
{
	ParameterSet pgun_params = pset.getParameter<ParameterSet>("PGunParameters") ;

	fMinPt = pgun_params.getParameter<double>("MinPt");
	fMaxPt = pgun_params.getParameter<double>("MaxPt");

	ParameterSet flow_params = pset.getParameter<ParameterSet>("FlowParameters") ;

	modCluster = flow_params.getParameter<edm::InputTag>("modCluster");

	fv1 = new TF1("fv1", flow_params.getParameter<edm::InputTag>("modv1").label().c_str());
	fv2 = new TF1("fv2", flow_params.getParameter<edm::InputTag>("modv2").label().c_str());
	fv3 = new TF1("fv3", flow_params.getParameter<edm::InputTag>("modv3").label().c_str());
	fv4 = new TF1("fv4", flow_params.getParameter<edm::InputTag>("modv4").label().c_str());
	fv5 = new TF1("fv5", flow_params.getParameter<edm::InputTag>("modv5").label().c_str());
	fv6 = new TF1("fv6", flow_params.getParameter<edm::InputTag>("modv6").label().c_str());
	fCluster = new TF1("fCluster", flow_params.getParameter<edm::InputTag>("modCluster").label().c_str());

	fluct_v1 = flow_params.getParameter<double>("fluct_v1");
	fluct_v2 = flow_params.getParameter<double>("fluct_v2");
	fluct_v3 = flow_params.getParameter<double>("fluct_v3");
	fluct_v4 = flow_params.getParameter<double>("fluct_v4");
	fluct_v5 = flow_params.getParameter<double>("fluct_v5");
	fluct_v6 = flow_params.getParameter<double>("fluct_v6");

	szCluster	= flow_params.getParameter<int>("szCluster");
	nCluster	= flow_params.getParameter<int>("nCluster");

	produces<HepMCProduct>();
	produces<GenEventInfoProduct>();
}

FlowGunProducer::~FlowGunProducer()
{
	// anything to clean up?
	delete fv1;
	delete fv2;
	delete fv3;
	delete fv4;
	delete fv5;
	delete fv6;
	delete fCluster;
}

void FlowGunProducer::produce(Event &e, const EventSetup& es)
{

	edm::Service<edm::RandomNumberGenerator> rng;
	CLHEP::HepRandomEngine* engine = &rng->getEngine(e.streamID());

	if ( fVerbosity > 0 )
	{
		cout << " FlowGunProducer : Begin New Event Generation" << endl ;
	}
	// event loop (well, another step in it...)

	// no need to clean up GenEvent memory - done in HepMCProduct
	//

	// here re-create fEvt (memory)
	//
	fEvt = new HepMC::GenEvent() ;

	// now actualy, cook up the event from PDGTable and gun parameters
	//
	// 1st, primary vertex
	//
	HepMC::GenVertex* Vtx = new HepMC::GenVertex(HepMC::FourVector(0.,0.,0.));

	// loop over particles
	//
	int barcode = 1 ;
	for (unsigned int ic=0; ic<nCluster; ++ic)
	{
		double pt     = CLHEP::RandFlat::shoot(engine, fMinPt, fMaxPt) ;
		double eta    = CLHEP::RandFlat::shoot(engine, fMinEta, fMaxEta) ;
		double phi    = CLHEP::RandFlat::shoot(engine, fMinPhi, fMaxPhi) ;
		int PartID = fPartIDs[ip] ;
		const HepPDT::ParticleData* 
			PData = fPDGTable->particle(HepPDT::ParticleID(abs(PartID))) ;
		double mass   = PData->mass().value() ;
		double theta  = 2.*atan(exp(-eta)) ;
		double mom    = pt/sin(theta) ;
		double px     = pt*cos(phi) ;
		double py     = pt*sin(phi) ;
		double pz     = mom*cos(theta) ;
		double energy2= mom*mom + mass*mass ;
		double energy = sqrt(energy2) ; 
		HepMC::FourVector p(px,py,pz,energy) ;
		HepMC::GenParticle* Part = 
			new HepMC::GenParticle(p,PartID,1);
		Part->suggest_barcode( barcode ) ;
		barcode++ ;
		Vtx->add_particle_out(Part);

	}

	fEvt->add_vertex(Vtx) ;
	fEvt->set_event_number(e.id().event()) ;
	fEvt->set_signal_process_id(20) ;

	if ( fVerbosity > 0 )
	{
		fEvt->print() ;
	}

	auto_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
	BProduct->addHepMCData( fEvt );
	e.put(BProduct);

	auto_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(fEvt));
	e.put(genEventInfo);

	if ( fVerbosity > 0 )
	{
		// for testing purpose only
		// fEvt->print() ; // prints empty info after it's made into edm::Event
		cout << " FlatRandomPtGunProducer : Event Generation Done " << endl;
	}
}

}
