#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


class QWAchProducer : public edm::EDProducer {
public:
	explicit QWAchProducer(const edm::ParameterSet&);
	~QWAchProducer();
private:
//	virtual void beginRun(edm::Run const& run, const edm::EventSetup& iSetup) override;
	virtual void produce(edm::Event&, const edm::EventSetup&) override;

	edm::EDGetTokenT<reco::TrackCollection>		trackToken_;
	edm::InputTag fweight_;

	bool	bEff_;

	double	dzdzerror_;
	double	d0d0error_;
	double	chi2_;
	double	pterrorpt_;
	double	rfpmineta_, rfpmaxeta_;
	double	rfpptmin_, rfpptmax_;

	TH2D * hEff_cbin[200];
}

QWAchProducer::QWAchProducer(const edm::ParameterSet& iConfig)
	, trackToken_(consumes<reco::TrackCollection>(iConfig.getUntrackedParameter<edm::InputTag>("tracks")))
	, fweight_ ( iConfig.getUntrackedParameter<edm::InputTag>("fweight_", string("NA")) )
{
	bEff_ = iConfig.getUntrackedParameter<bool>("bEff", false);
	dzdzerror_ = iConfig.getUntrackedParameter<double>("dzdzerror", 3.);
	chi2_ = iConfig.getUntrackedParameter<double>("chi2_", 40);
	pterrorpt_ = iConfig.getUntrackedParameter<double>("pterrorpt_", 0.1);

	rfpmineta_ = iConfig.getUntrackedParameter<double>("rfpmineta_", -2.4);
	rfpmaxeta_ = iConfig.getUntrackedParameter<double>("rfpmaxeta_", 2.4);
	rfpptmin_ = iConfig.getUntrackedParameter<double>("rfpptmin_", 0.3);
	rfpptmax_ = iConfig.getUntrackedParameter<double>("rfpptmax_", 100);

	string streff = fweight_.label();
	if ( streff == string("NA") ) {
		bEff = false;
		fEffFak = 0;
	} else {
		fEffFak = new TFile(streff.c_str());
		if ( !fEffFak->IsOpen() ) {
			bFak = false;
			bEff = false;
		} else {
			cout << "!!! Using particle weight " << streff << endl;
			if ( bFak ) cout << "!!! Apply Fak correction" << endl;
			if ( bEff ) {
				cout << "!!! Apply Eff correction" << endl;
				for ( int i = 0; i < 20; i++ ) {
					if ( streff == string("PbPb_MB_TT_5TeV_v2.root") or streff == string("PbPb_dijet_TT_5TeV_v2.root") ) {
						TH2D * h = (TH2D*) fEffFak->Get("rTotalEff3D_0_5");
						for ( int c = 0; c < 10; c++ ) {
							hEff_cbin[c] = h;
						}
						h = (TH2D*) fEffFak->Get("rTotalEff3D_5_10");
						for ( int c = 10; c < 20; c++ ) {
							hEff_cbin[c] = h;
						}
						h = (TH2D*) fEffFak->Get("rTotalEff3D_10_30");
						for ( int c = 20; c < 60; c++ ) {
							hEff_cbin[c] = h;
						}
						h = (TH2D*) fEffFak->Get("rTotalEff3D_30_50");
						for ( int c = 60; c < 100; c++ ) {
							hEff_cbin[c] = h;
						}
						h = (TH2D*) fEffFak->Get("rTotalEff3D_50_100");
						for ( int c = 100; c < 200; c++ ) {
							hEff_cbin[c] = h;
						}
					}
				}
				cout << "!!! eff histo done" << endl;
			}
		}
	}
	produces<int>("Ach");
}

void
QWAchProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup);


DEFINE_FWK_MODULE(QWAchProducer);
