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
#include <RecoHI/HiEvtPlaneAlgos/interface/HiEvtPlaneList.h>
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

const int NMAX_TRK = 10000;
typedef struct QWEvent_ {
	int     Cent;
	int     Mult;
	double  vz;
	int	Noff;
	double  Pt[NMAX_TRK];
	double  Eta[NMAX_TRK];
	double  Phi[NMAX_TRK];
	int     Charge[NMAX_TRK];
	double	rEff[NMAX_TRK];
	double	rFak[NMAX_TRK];
	double	weight[NMAX_TRK];
	int	RFP[NMAX_TRK];
	int     RunId;
	int     EventId;
} QWEvent;

///////////////// Class ////////////////////////////

class QWCumuV3 : public edm::EDAnalyzer {
	public:
		explicit QWCumuV3(const edm::ParameterSet&);
		~QWCumuV3();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() ;
		virtual void analyze(const edm::Event&, const edm::EventSetup&);
		void analyzeData(const edm::Event&, const edm::EventSetup&);
		void analyzeGen(const edm::Event&, const edm::EventSetup&);
		void analyzeEP(const edm::Event&, const edm::EventSetup&);
		virtual void endJob() ;

		virtual void beginRun(edm::Run const&, edm::EventSetup const&);
		virtual void endRun(edm::Run const&, edm::EventSetup const&);
		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
		virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

	/////////////////////////////////////////////
		int getNoffCent(const edm::Event&, const edm::EventSetup&, int& Noff);
		//TRandom3 * gRandom;
		// ----------member data ---------------------------
		edm::InputTag					trackTag_;
		edm::EDGetTokenT<reco::TrackCollection>		trackToken_;
		edm::EDGetTokenT<reco::GenParticle>		trackGenToken_;
		edm::EDGetTokenT<int>				centralityToken_;
		edm::EDGetTokenT<reco::VertexCollection>	vertexToken_;
		edm::EDGetTokenT<reco::EvtPlaneCollection>	epToken_;
		//edm::InputTag tracks_; //used to select what tracks to read from configuration file
		//edm::InputTag centrality_;	// centrality
		///edm::InputTag vertexSrc_;

		edm::InputTag fweight_;
		edm::InputTag facceptance_;
	/////////////////////////////////////////////
		double	minvz_, maxvz_;
		double	dzdzerror_;
		double	d0d0error_;
		double	chi2_;
		double	pterrorpt_;
		double	rfpmineta_, rfpmaxeta_;
		double	poimineta_, poimaxeta_;
		double	rfpptmin_, rfpptmax_;
		double	poiptmin_, poiptmax_;
		int	charge_;

		bool	bFak;
		bool	bEff;
		bool	bacc;
		bool	bPhiEta;
		bool	bCentNoff;
		bool	bSim_;
		bool	bCaloMatching_;
		int	Noffmin_;
		int	Noffmax_;
		int	cmode_;
		bool	bGen_;
		bool	bFlipEta_;
		bool	bEP_;
		int	EPlvl_;
		std::vector<int> algoParameters_;

		unsigned int	nvtx_;
		int	sGenPreset_;

		double	effCut_;
		QWEvent * t;
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

		TH2D * hEP[nPtBins][7];
		TH2D * hSP[nPtBins][7];
		TH2D * iEP[nPtBins][7];
		TH2D * iSP[nPtBins][7];
		TH2D * hMult;

		TH2D * hEPresAB;
		TH2D * hEPresAC;
		TH2D * hEPresBC;

		TH2D * hSPresAB;
		TH2D * hSPresAC;
		TH2D * hSPresBC;

		TH2D * hMultRes;

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

		correlations::HarmonicVector	hc[7];
		correlations::QVector		q[7];
		correlations::FromQVector	*cq[7];

		void initQ();
		void doneQ();
		void Sim();

		bool QWCumuV3::CaloMatch();
};



