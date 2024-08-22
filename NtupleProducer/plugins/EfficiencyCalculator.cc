#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/Scouting/interface/Run3ScoutingElectron.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/EgammaObject.h"
//#include "L1Trigger/L1TGlobal/plugins/L1TGlobalProducer.h"
//#include "HLTrigger/Egamma/plugins/HLTEgammaL1TMatchFilterRegional.cc"
#include "CondFormats/DataRecord/interface/L1TGlobalParametersRcd.h"
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include <vector>
#include <string>
#include <iostream>
#include <TH1F.h>
#include <TH2D.h>
#include <TFile.h>
#include <TLorentzVector.h>
#include <TTree.h>
#include "Math/VectorUtil.h"
#include <stdlib.h>

#define TWOPI 6.283185308
int globCounter = 0;
/****************************************************************************
 Simple example on how to access the L1 decision via  l1t::L1TGlobalUtil
 To make things easier it uses HLTPrescaleProvider to obtain the  
 l1t::L1TGlobalUtil object

 note, its very important that you run with the correct global tag as it
 retrieves the menu from this

 

 author Sam  Harper (RAL), 2019
*****************************************************************************/

class EfficiencyCalculator : public edm::one::EDAnalyzer<edm::one::WatchRuns> {
 
private:
  
  std::string hltProcess_; //name of HLT process, usually "HLT"
  edm::EDGetTokenT<std::vector<trigger::EgammaObject> > eleToken_;
  edm::EDGetTokenT<std::vector<trigger::EgammaObject> > eleUnseededToken_;
  edm::EDGetTokenT<std::vector<reco::RecoEcalCandidate> > recoEcalUnseededToken_;
  edm::EDGetTokenT<std::vector<reco::RecoEcalCandidate> > recoEcalToken_;
  edm::EDGetTokenT<edm::TriggerResults > hltToken_;
  edm::EDGetTokenT<trigger::TriggerEvent > hltsevtToken_;
  //edm::EDGetTokenT<std::vector<reco::GenParticle> > genToken_;
  edm::EDGetTokenT<trigger::TriggerFilterObjectWithRefs > L1Token_;
  //edm::EDGetTokenT<std::vector<PileupSummaryInfo> > pileupSummaryToken_;
  edm::Service<TFileService> fs;
  double endcap_end_ = 2.5;
  TH1D* num_ele_pt_EB1;
  TH1D* num_ele_pt_EB2;
  TH1D* num_ele_pt_EE1;
  TH1D* num_ele_pt_EE2;
  TH1D* num_ele_eta;
  TH1D* num_ele_phi;
  TH1D* num_ele_pu;
  
  TH1D* num_ele_pt;
  TH1D* den_ele_pt;

  TH1D* den_ele_pt_EB1;
  TH1D* den_ele_pt_EB2;
  TH1D* den_ele_pt_EE1;
  TH1D* den_ele_pt_EE2;
  TH1D* den_ele_eta;
  TH1D* den_ele_phi;
  TH1D* den_ele_pu;
  float barrel_end_ = 1.4442;
  TH2D* occupancy_phi_eta_all;

public:
  explicit EfficiencyCalculator(const edm::ParameterSet& iConfig);
  ~EfficiencyCalculator(){}
  
 private:
  virtual void beginRun(const edm::Run& run,const edm::EventSetup& iSetup);
  virtual void endRun(edm::Run const&, edm::EventSetup const&) override{}
  virtual void analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup);
  virtual void endJob(){}
};


EfficiencyCalculator::EfficiencyCalculator(const edm::ParameterSet& iConfig):
  hltProcess_("HLTX")
{
  eleUnseededToken_     = consumes<std::vector<trigger::EgammaObject> >(edm::InputTag("hltEgammaHLTExtra","Unseeded","HLTX"));
  eleToken_     = consumes<std::vector<trigger::EgammaObject> >(edm::InputTag("hltEgammaHLTExtra","","HLTX"));
  hltToken_     = consumes<edm::TriggerResults>(edm::InputTag("TriggerResults","","HLTX"));
  hltsevtToken_ = consumes<trigger::TriggerEvent>(edm::InputTag("hltTriggerSummaryAOD","","HLT"));
  recoEcalUnseededToken_ = consumes<std::vector<reco::RecoEcalCandidate> >(edm::InputTag("hltEgammaCandidatesUnseeded","","HLTX"));
  recoEcalToken_ = consumes<std::vector<reco::RecoEcalCandidate> >(edm::InputTag("hltEgammaCandidates","","HLTX"));
  //genToken_     = consumes<std::vector<reco::GenParticle> >(edm::InputTag("genParticles"));
  //pileupSummaryToken_ = consumes<std::vector<PileupSummaryInfo> >(edm::InputTag("addPileupInfo"));
  

  // pT
  num_ele_pt_EB1 = fs->make<TH1D>("num_ele_pt_EB1",";pT (GeV);Events",50,0,500);
  num_ele_pt_EB2 = fs->make<TH1D>("num_ele_pt_EB2",";pT (GeV);Events",50,0,500);
  num_ele_pt_EE1 = fs->make<TH1D>("num_ele_pt_EE1",";pT (GeV);Events",50,0,500);
  num_ele_pt_EE2 = fs->make<TH1D>("num_ele_pt_EE2",";pT (GeV);Events",50,0,500);

  den_ele_pt_EB1 = fs->make<TH1D>("den_ele_pt_EB1",";pT (GeV);Events",50,0,500);
  den_ele_pt_EB2 = fs->make<TH1D>("den_ele_pt_EB2",";pT (GeV);Events",50,0,500);
  den_ele_pt_EE1 = fs->make<TH1D>("den_ele_pt_EE1",";pT (GeV);Events",50,0,500);
  den_ele_pt_EE2 = fs->make<TH1D>("den_ele_pt_EE2",";pT (GeV);Events",50,0,500);

  // eta
  num_ele_eta = fs->make<TH1D>("num_ele_eta",";eta;Events",53,-2.65,2.65);
  den_ele_eta = fs->make<TH1D>("den_ele_eta",";eta;Events",53,-2.65,2.65);
  // pt
  num_ele_pt = fs->make<TH1D>("num_ele_pt",";pt;Events",50,0,500);
  den_ele_pt = fs->make<TH1D>("den_ele_pt",";pt;Events",50,0,500);

  // phi
  num_ele_phi = fs->make<TH1D>("num_ele_phi",";phi;Events",63,-3.15,3.15);
  den_ele_phi = fs->make<TH1D>("den_ele_phi",";phi;Events",63,-3.15,3.15);
  occupancy_phi_eta_all = fs->make<TH2D>("occupancy_phi_eta_all",";#eta_{SC};#phi",50,-2.5,2.5,32,-3.2,3.2);
}


const int getFilterIndex(const trigger::TriggerEvent& trigEvt, const std::string filterName){
  for(auto i=0; i < trigEvt.sizeFilters(); i++){

    //if("hltEle32WPTightGsfTrackIsoFilter"==trigEvt.filterLabel(i))  {
    //std::cout << trigEvt.filterLabel(i) << std::endl;
    //globCounter++;}
    if(filterName==trigEvt.filterLabel(i)) return i;
  }
  return trigEvt.sizeFilters();  
}

std::vector<const trigger::TriggerObject*> getListFilterPassedObj(const std::string filterName,const trigger::TriggerEvent& hlts){
  std::vector<const trigger::TriggerObject*> eg_trig_objs;
  const int filterIndex = getFilterIndex(hlts,filterName);
  if(filterIndex < hlts.sizeFilters() ){
    for(auto filterKey : hlts.filterKeys(filterIndex)){
      auto& obj = hlts.getObjects()[filterKey];
      eg_trig_objs.push_back(&obj);
    }
  }
  return eg_trig_objs;
}


std::vector<const trigger::TriggerObject*> matchTrigObjs(const float eta,const float phi,const float pT,std::vector<const trigger::TriggerObject*> trigObjs,const float maxDeltaR=0.1, const float maxDpT=0.1)
{
  std::vector<const trigger::TriggerObject*> matchedObjs;
  const float maxDR2 = maxDeltaR*maxDeltaR;
  for(auto& trigObj : trigObjs){
    const float deltaR2 = reco::deltaR2(eta, phi, trigObj->eta(), trigObj->phi());
    if(deltaR2 < maxDR2 && (fabs(pT - trigObj->pt())/pT) < maxDpT) matchedObjs.push_back(trigObj);
  }
  return matchedObjs;
}

const bool matchDRAndpT(const float eta1,const float phi1,const float pT1,const float eta2,const float phi2,const float pT2,const float maxDeltaR=0.1, const float maxDpT=0.1){
  
  bool isMatched = false;
  const float maxDR2 = maxDeltaR*maxDeltaR;
  const float deltaR2 = reco::deltaR2(eta1, phi1, eta2, phi2);
  const float deltaPt = fabs(pT1-pT2)/pT1;
  if(deltaR2 < maxDR2 && deltaPt < maxDpT) isMatched = true;
  return isMatched;
}

std::vector<const reco::GenParticle*> getGenparts(const std::vector<reco::GenParticle>& genparts,const int pid=11, bool antipart=true, const int status=1){

  std::vector<const reco::GenParticle*> selected;
  if(genparts.empty()) return selected;

  for(auto& part : genparts){
    const int pdg_id = part.pdgId();
    if(pdg_id == pid || (antipart && abs(pdg_id) == abs(pid))){
      if(part.isHardProcess() && status == 1){
	selected.push_back(&part);
      }
    }
  }
  return selected;
}



float matchToGen(const float eta,const float phi,const std::vector<reco::GenParticle>& genparts,const int pid=11,bool antipart=true,const float max_dr=0.1,const int status=1){

  float best_dr2 = max_dr*max_dr;
  float best_pt = -999999;
  auto selected_parts = getGenparts(genparts,pid,antipart,status);
  for(auto part : selected_parts){
    const float dr2 = reco::deltaR2(eta, phi, part->eta(), part->phi());
    if(dr2 < best_dr2){
      best_dr2 = dr2;
      best_pt = part->pt();
    }
  }
  return best_pt;
}


float matchToScoutingElectrons(const float eta,const float phi,const std::vector<Run3ScoutingElectron>& scout_ele,const float max_dr=0.1){

  float best_dr2 = max_dr*max_dr;
  float best_pt = -999999;
  //auto selected_parts = getGenparts(genparts,pid,antipart,status);
  for(auto part : scout_ele){
    const float dr2 = reco::deltaR2(eta, phi, part.eta(), part.phi());
    if(dr2 < best_dr2){
      best_dr2 = dr2;
      best_pt = part.pt();
    }
  }
  return best_pt;
}

float matchToRecoEcalCandidate(const float eta,const float phi,const std::vector<reco::RecoEcalCandidate>& ecalCand,const float max_dr=0.1){

  float best_dr2 = max_dr*max_dr;
  float best_pt = -999999;
  //auto selected_parts = getGenparts(genparts,pid,antipart,status);
  for(auto part : ecalCand){
    const float dr2 = reco::deltaR2(eta, phi, part.eta(), part.phi());
    if(dr2 < best_dr2){
      best_dr2 = dr2;
      best_pt = part.pt();
    }
  }
  return best_pt;
}

std::vector<trigger::EgammaObject> matchRecoObjs(const float eta,const float phi,const float pT,const std::vector<trigger::EgammaObject>* trigObjs,const float maxDeltaR=0.1, const float maxDpT=0.1)
{
  std::vector<trigger::EgammaObject> matchedObjs;
  const float maxDR2 = maxDeltaR*maxDeltaR;
  for(auto& trigObj : *trigObjs){
    const float deltaR2 = reco::deltaR2(eta, phi, trigObj.eta(), trigObj.phi());
    if(deltaR2 < maxDR2 && (fabs(pT - trigObj.pt())/pT) < maxDpT) matchedObjs.push_back(trigObj);
  }
  return matchedObjs;
}


float calculateInvMass(const trigger::EgammaObject tagElectron, const trigger::EgammaObject probeCandidate) {

  TLorentzVector tag;
  TLorentzVector probe;

  tag.SetPxPyPzE(tagElectron.px(),tagElectron.py(),tagElectron.pz(),tagElectron.energy());
  probe.SetPxPyPzE(probeCandidate.px(),probeCandidate.py(),probeCandidate.pz(),probeCandidate.energy());

  float invMass = (tag + probe).M();

  return invMass;

}



//we need to initalise the menu each run (menu can and will change on run boundaries)
void EfficiencyCalculator::beginRun(const edm::Run& run,const edm::EventSetup& setup)
{
  //bool changed=false;
  //hltPSProv_.init(run,setup,hltProcess_,changed);
}

void EfficiencyCalculator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle<std::vector<trigger::EgammaObject> > eleUnseeded;
  iEvent.getByToken(eleUnseededToken_,eleUnseeded);

  edm::Handle<std::vector<trigger::EgammaObject> > ele;
  iEvent.getByToken(eleToken_,ele);
  
  edm::Handle<std::vector<reco::RecoEcalCandidate> > superClusUnseeded;
  iEvent.getByToken(recoEcalUnseededToken_,superClusUnseeded);
  
  edm::Handle<std::vector<reco::RecoEcalCandidate> > superClus;
  iEvent.getByToken(recoEcalToken_,superClus);
  
  edm::Handle<edm::TriggerResults > hlt;
  iEvent.getByToken(hltToken_,hlt);

  edm::Handle<trigger::TriggerEvent > hltsevt;
  iEvent.getByToken(hltsevtToken_,hltsevt);

  //edm::Handle<std::vector<reco::GenParticle> > gen;
  //iEvent.getByToken(genToken_,gen);

  // edm::Handle<std::vector<PileupSummaryInfo> >  PUInfo;
  // iEvent.getByToken(pileupSummaryToken_, PUInfo);
  
  // float nPU = -1;
 
  // std::vector<PileupSummaryInfo>::const_iterator PUi; 
 
  // for(PUi = PUInfo->begin(); PUi != PUInfo->end(); ++PUi) {
  //   const int BX = PUi->getBunchCrossing();
  //   if(BX == 0){
  //     nPU = PUi->getTrueNumInteractions(); //Corresponding to the in-time PU
  //   }
  // }
  
//auto eg_trig_objs_filter = getListFilterPassedObj("hltEle32WPTightGsfTrackIsoFilter",*hltsevt.product());
  //auto eg_trig_objs_filter = getListFilterPassedObj("hltEG30EBTightIDTightIsoTrackIsoFilter",*hltsevt.product());
  auto eg_trig_objs_filter = ele.product();

  //auto electrons = ele.product();
  auto scProd = superClus.product();
 
  if(scProd->size() < 2) return;
  std::cout<<"scProd->size()\t"<<scProd->size()<<std::endl;

  //std::cout << globCounter << std::endl;

  std::vector<reco::RecoEcalCandidate> listOfTags;
  
  for(auto& el : *scProd){

    if(fabs(el.eta()) > barrel_end_ || el.pt() < 30) continue;

    //auto matched = matchTrigObjs(el.eta(),el.phi(),el.pt(),eg_trig_objs_filter);
    auto matched = matchRecoObjs(el.eta(),el.phi(),el.pt(),eg_trig_objs_filter);
    std::cout<<"matched.size()\t"<<matched.size()<<std::endl; 
    if(matched.size() > 0) listOfTags.push_back(el);
  }
   
  std::cout<<"listOfTags.size():\t"<<listOfTags.size()<<std::endl;
  for(auto& el : *scProd){

    if(fabs(el.eta()) > endcap_end_) continue;

    for(auto tag : listOfTags){

      float invMass = calculateInvMass(tag, el);
      if(fabs(invMass - 91.1876) < 30. && tag.charge()*el.charge() < 0) break;
      else return;
    }
    //if(!matchToGen(el.eta(),el.phi(),*(gen.product()))) continue;

    //auto matched_objs_filter = matchTrigObjs(el.eta(),el.phi(),el.pt(),eg_trig_objs_filter);
    auto matched_objs_filter = matchRecoObjs(el.eta(),el.phi(),el.pt(),eg_trig_objs_filter);
    auto nmatch_filter = matched_objs_filter.size();
    std::cout<<"nmatch_filter probes:\t"<<nmatch_filter<<std::endl; 

    //Fill denominators
      //den_ele_pt_EB1->Fill(el.pt());
      //den_ele_pt_EB2->Fill(el.pt());
      den_ele_pt->Fill(el.pt());

      if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.0) den_ele_pt_EE1->Fill(el.pt());
      if (fabs(el.eta()) > 2.00 && fabs(el.eta()) < 2.5) den_ele_pt_EE2->Fill(el.pt());

      if (el.pt() > 32.) {
    	den_ele_eta->Fill(el.eta());
    	den_ele_phi->Fill(el.phi());
      }
      

    //Fill numerators                                                                                                                                
    if(nmatch_filter>0){
        num_ele_pt->Fill(el.pt());

      if (fabs(el.eta()) < 1.0 ) num_ele_pt_EB1->Fill(el.pt());
      if (fabs(el.eta()) > 1.0 && fabs(el.eta()) < 1.44) num_ele_pt_EB2->Fill(el.pt());

      if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.0) num_ele_pt_EE1->Fill(el.pt());
      if (fabs(el.eta()) > 2.00 && fabs(el.eta()) < 2.5) num_ele_pt_EE2->Fill(el.pt());

      if (el.pt() > 32.) {
    	num_ele_eta->Fill(el.eta());
    	num_ele_phi->Fill(el.phi());
	occupancy_phi_eta_all->Fill(el.eta(),el.phi());
      }

    }
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(EfficiencyCalculator);
