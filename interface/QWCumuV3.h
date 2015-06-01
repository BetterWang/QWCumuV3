#include <correlations/Types.hh>
#include <correlations/Result.hh>
#include <correlations/QVector.hh>
#include <correlations/recursive/FromQVector.hh>
#include <correlations/recurrence/FromQVector.hh>
#include <correlations/closed/FromQVector.hh>
#include <TComplex.h>
#include <TH1.h>
#include <TH2.h>
#include <TTree.h>
#include <TNtupleD.h>
#include <TRandom3.h>
#include <TFile.h>
#include "QWConstV3.h"
//
// constants, enums and typedefs
//

//#define QW_DEBUG 1
//#define QW_PEREVENT 1

#define PRD(x) cout << "!!QW!! " << __LINE__ << " DEBUG OUTPUT " << (#x) << " = " << (x) << endl;
#define PR(x) cout << "!!QW!! " << __LINE__ << " DEBUG OUTPUT " << (#x) << endl;
//
// class declaration
//

const int NMAX_TRK = 300;
typedef struct QWEvent_ {
	int     Cent;
	int     Mult;
	float	vz;
	int	Noff;
	float	Pt[NMAX_TRK];
	float	Eta[NMAX_TRK];
	float	Phi[NMAX_TRK];
	char	Charge[NMAX_TRK];
	float	rEff[NMAX_TRK];
	float	rFak[NMAX_TRK];
	float	weight[NMAX_TRK];
	bool	RFP[NMAX_TRK];
	QWEvent_() {
		Cent = -1;
		Mult = -1;
		vz = -999.;
		Noff = -1;
		for ( int i = 0; i < NMAX_TRK; ++i ) {
			Pt[i] = 0;
			Eta[i] = -999;
			Phi[i] = -999;
			Charge[i] = -127;
			rEff[i] = 0.;
			rFak[i] = 0.;
			weight[i] = 0.;
			RFP[i] = false;
		}
	};
} QWEvent;

///////////////// Class ////////////////////////////

class QWCumuV3 : public edm::EDAnalyzer {
	public:
		explicit QWCumuV3(const edm::ParameterSet&);
		~QWCumuV3();

//		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		bool analyzeData(const edm::Event&, const edm::EventSetup&);
		bool analyzeGen(const edm::Event&, const edm::EventSetup&);
		virtual void endJob() override;

//		virtual void beginRun(edm::Run const&, edm::EventSetup const&);
//		virtual void endRun(edm::Run const&, edm::EventSetup const&);
//		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
//		virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

	/////////////////////////////////////////////
		int getNoffCent(const edm::Event&, const edm::EventSetup&, int& Noff);

		auto getMix(auto it, auto&& pool);
		// ----------member data ---------------------------
		edm::InputTag tracks_; //used to select what tracks to read from configuration file
		edm::InputTag centrality_;	// centrality
		edm::InputTag vertexSrc_;
		edm::InputTag correctHist_;

		edm::InputTag fweight_;
		edm::InputTag facceptance_;
	/////////////////////////////////////////////
		double 	minvz_, maxvz_;
		double 	dzdzerror_;
		double 	d0d0error_;
		double 	chi2_;
		double 	pterrorpt_;
		double 	rfpmineta_, rfpmaxeta_;
		double 	poimineta_, poimaxeta_;
		double 	rfpptmin_, rfpptmax_;
		double 	poiptmin_, poiptmax_;
		int 	charge_;

		int 	nmixed_;
		int 	ntry_;

		bool	bFak;
		bool	bEff;
		bool	bacc;
		bool	bPhiEta;
		bool	bCentNoff;
		bool	bSim_;
		int 	Noffmin_;
		int 	Noffmax_;
		int	cmode_;
		bool	bGen_;
		bool	bFlipEta_;

		unsigned int	nvtx_;

		double	effCut_;
		TFile	* fEffFak;
		TFile	* facc;
	/////////////////////////////////////////////
		TH1D * hPt[nCentBins];
		TH2D * hPhiEta[nCentBins][nPtBins][2];

		TH2D	* hdNdPtdEta[nCentBins];
		TH2D	* hdNdPtdEtaPt[nCentBins];

		TH2D * hEff_cbin[nCentBins];
		TH2D * hFak_cbin[nCentBins];

		TH2D * hacc[nCentBins][nPtBins][2];

		TH2D * h2DPhiDEta[nCentBins][nPtBins][nPtBins];
		TH2D * h2DPhiDEtaRFP[nCentBins];
		TH1D * h2NDPhiDEta[nCentBins][nPtBins][nPtBins];
		TH1D * h2NDPhiDEtaRFP[nCentBins];

		TH2D * h2DPhiDEtaMix[nCentBins][nPtBins][nPtBins];
		TH2D * h2DPhiDEtaRFPMix[nCentBins];
		TH1D * h2NDPhiDEtaMix[nCentBins][nPtBins][nPtBins];
		TH1D * h2NDPhiDEtaRFPMix[nCentBins];

//		TNtupleD * ntResult;
		TTree * trV;

		int gNoff;
		int gMult;

		double rQ[7][4];
		double iQ[7][4];
		double wQ[7][4];

		double rX[7][4];
		double iX[7][4];
		double wX[7][4];

		double rQp[7][4][24];
		double iQp[7][4][24];
		double wQp[7][4][24];

		double rQeta[7][4][24];
		double iQeta[7][4][24];
		double wQeta[7][4][24];

		double rQc[7][4][2];
		double iQc[7][4][2];
		double wQc[7][4][2];

		correlations::HarmonicVector 	hc[7];
		correlations::QVector		q[7];
		correlations::FromQVector 	*cq[7];

		void initQ();
		void doneQ();
		void Sim();

		std::vector<QWEvent> vEvt;
		std::vector<QWEvent>::iterator t;
};

