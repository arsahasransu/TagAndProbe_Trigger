import FWCore.ParameterSet.Config as cms
import glob
import os

process = cms.Process("USER")

reRunL1 = False

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '131X_mcRun3_2023_realistic_forEGamma_v1') 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


# dir1Name = "/afs/cern.ch/user/r/rselvati/work/private/testBPIX/CMSSW_13_0_10/src/SteamRatesEdmWorkflow/Prod/hltModified/"
# dir2Name = "/eos/cms/store/mc/Run3Summer22EEDR/ZprimeToEE_M-6000_TuneCP5_13p6TeV-pythia8/GEN-SIM-RAW/Poisson70KeepRAW_124X_mcRun3_2022_realistic_postEE_v1-v1/720000/"
# fileList1 = filter(os.path.isfile, glob.glob(dir1Name + "*.root"))
# fileList2 = filter(os.path.isfile, glob.glob(dir2Name + "*.root"))
# fList = []
# for f in fileList1:
#      fs = str(f).replace("/afs/","file:/afs/")
#      fList.append(fs)
# for f in fileList2:
#     fs = str(f).replace("/eos/","file:/eos/")
#     fList.append(fs)
# print(fList)
#from list_relval import fileList
process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(#fList
                                    'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_1.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_2.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_3.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_4.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_5.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_6.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_7.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_8.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_9.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_10.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_11.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_12.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_13.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_14.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_15.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_16.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_17.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_18.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_19.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_20.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_21.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_22.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_23.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_24.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_25.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_26.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_27.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_28.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_29.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_30.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_31.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_32.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_33.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_34.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_35.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_36.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_37.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_38.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_39.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_40.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_41.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_42.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_43.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_44.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_45.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_46.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_47.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_48.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_49.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_50.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_51.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_52.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_53.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_54.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_55.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_56.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_57.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_58.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_59.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_60.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_61.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_62.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_63.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_64.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_65.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_66.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_67.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_68.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_69.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_70.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_71.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_72.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_73.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_74.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_75.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_76.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_77.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_78.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_79.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_80.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_81.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_82.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_83.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_84.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_85.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_86.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_87.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_88.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_89.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_90.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_91.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_92.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_93.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_94.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_95.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_96.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_97.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_98.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_99.root',
'root://cms-xrd-global.cern.ch//store/user/asahasra/EphemeralHLTPhysics0/EphemeralHLT0_240821_14014_ReRunScoutSingleEG_Before/240821_140945/0000/outputScoutingPF_100.root',
                                    #'file:outputScoutingPF_before.root'
                                    #'root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver2-v1/80000/FEAB7D8A-048C-E811-A513-AC1F6B1AEFFC.root'
                )
                            )
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
#Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string("Efficiency_Modified.root")
)


# process.hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
#     scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
#     scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
#     recoEcalCandidateCollection = cms.string( "" )
# )

# process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
#     recordName = cms.string('L1TGlobalParametersRcd'),
#     iovIsRunNotTime = cms.bool(True),
#     firstValid = cms.vuint32(1)
# )

# process.GlobalParameters = cms.ESProducer("StableParametersTrivialProducer", 
#     # bx in event
#     #NumberBxInEvent = cms.int32(5),
                                    
#     # trigger decision
                                            
#     # number of physics trigger algorithms
#     NumberPhysTriggers = cms.uint32(512),
                                              
                                              
#     # trigger objects

#     # muons
#     NumberL1Muon = cms.uint32(8),
    
#     # e/gamma and isolated e/gamma objects
#     NumberL1EGamma = cms.uint32(12),

#     #  jets
#     NumberL1Jet = cms.uint32(12),

#     # taus
#     NumberL1Tau = cms.uint32(12),

#     # hardware
                                            
#     # number of maximum chips defined in the xml file
#     NumberChips = cms.uint32(1),

#     # number of pins on the GTL condition chips
#     PinsOnChip = cms.uint32(512),

#     # correspondence "condition chip - GTL algorithm word" in the hardware
#     # e.g.: chip 2: 0 - 95;  chip 1: 96 - 128 (191)
#     OrderOfChip = cms.vint32(1),
# )

# process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
#     CTP7 = cms.untracked.bool( False ),
#     DmxFWId = cms.uint32( 0 ),
#     FWId = cms.uint32( 0 ),
#     FWOverride = cms.bool( False ),
#     FedIds = cms.vint32( [ 1404 ] ),
#     InputLabel = cms.InputTag( "rawDataCollector" ),
#     MTF7 = cms.untracked.bool( False ),
#     MinFeds = cms.uint32( 0 ),
#     Setup = cms.string( "stage2::GTSetup" ),
#     TMTCheck = cms.bool( True ),
#     debug = cms.untracked.bool( False ),
#     lenAMC13Header = cms.untracked.int32( 8 ),
#     lenAMC13Trailer = cms.untracked.int32( 8 ),
#     lenAMCHeader = cms.untracked.int32( 8 ),
#     lenAMCTrailer = cms.untracked.int32( 0 ),
#     lenSlinkHeader = cms.untracked.int32( 8 ),
#     lenSlinkTrailer = cms.untracked.int32( 8 )
# )

# process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
#     AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     AlgorithmTriggersUnmasked = cms.bool( True ),
#     AlgorithmTriggersUnprescaled = cms.bool( True ),
#     AlternativeNrBxBoardDaq = cms.uint32( 0 ),
#     BstLengthBytes = cms.int32( -1 ),
#     EGammaInputTag = cms.InputTag( "hltGtStage2Digis","EGamma" ),
#     EmulateBxInEvent = cms.int32( 1 ),
#     EtSumInputTag = cms.InputTag( "hltGtStage2Digis","EtSum" ),
#     ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     GetPrescaleColumnFromData = cms.bool( False ),
#     JetInputTag = cms.InputTag( "hltGtStage2Digis","Jet" ),
#     L1DataBxInEvent = cms.int32( 5 ),
#     MuonInputTag = cms.InputTag( "hltGtStage2Digis","Muon" ),
#     MuonShowerInputTag = cms.InputTag( "hltGtStage2Digis","MuonShower" ),
#     PrescaleSet = cms.uint32( 1 ),
#     PrintL1Menu = cms.untracked.bool( False ),
#     ProduceL1GtDaqRecord = cms.bool( True ),
#     ProduceL1GtObjectMapRecord = cms.bool( True ),
#     RequireMenuToMatchAlgoBlkInput = cms.bool( True ),
#     TauInputTag = cms.InputTag( "hltGtStage2Digis","Tau" ),
#     TriggerMenuLuminosity = cms.string( "startup" ),
#     Verbosity = cms.untracked.int32( 0 ),
#     resetPSCountersEachLumiSec = cms.bool( True ),
#     semiRandomInitialPSCounters = cms.bool( False ),
#     useMuonShowers = cms.bool( True )
# )


# process.hltL1sSingleEGor = cms.EDFilter( "HLTL1TSeed",
#     saveTags = cms.bool( True ),
#     L1SeedsLogicalExpression = cms.string( "L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5"), #opt4
#     L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
#     L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
#     L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
#     L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
#     L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
#     L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
#     L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
# )

# process.hltL1sSingleAndDoubleEG = cms.EDFilter( "HLTL1TSeed",
#     saveTags = cms.bool( True ),
#     L1SeedsLogicalExpression = cms.string( "L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5 OR L1_DoubleEG_22_10_er2p5 OR L1_DoubleEG_25_12_er2p5 OR L1_DoubleEG_25_14_er2p5 OR L1_DoubleEG_LooseIso22_12_er2p5" ),
#     L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
#     L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
#     L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
#     L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
#     L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
#     L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
#     L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
# )

# process.hltL1sSingleEG40to50 = cms.EDFilter( "HLTL1TSeed",
#     saveTags = cms.bool( True ),
#     L1SeedsLogicalExpression = cms.string( "L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5"),
#     L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
#     L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
#     L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
#     L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
#     L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
#     L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
#     L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
# )

# process.hltL1sSingleJet170IorSingleJet180IorSingleJet200 = cms.EDFilter( "HLTL1TSeed",
#     saveTags = cms.bool( True ),
#     L1SeedsLogicalExpression = cms.string( "L1_SingleJet180 OR L1_SingleJet200"),
#     L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
#     L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
#     L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
#     L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
#     L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
#     L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
#     L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
# )

# process.hltL1sSingleEGNonIsoOrWithJetAndTau = cms.EDFilter( "HLTL1TSeed",
#     saveTags = cms.bool( True ),
#     L1SeedsLogicalExpression = cms.string( "L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleJet180 OR L1_SingleJet200 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60"),
#     L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
#     L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
#     L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
#     L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
#     L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
#     L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
#     L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
# )

# process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau = cms.EDFilter( "HLTL1TSeed",
#     saveTags = cms.bool( True ),
#     L1SeedsLogicalExpression = cms.string( "L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_DoubleEG_22_10_er2p5 OR L1_DoubleEG_25_12_er2p5 OR L1_DoubleEG_25_14_er2p5 OR L1_SingleJet180 OR L1_SingleJet200 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1"),
#     L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
#     L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" ),
#     L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
#     L1MuonShowerInputTag = cms.InputTag( 'hltGtStage2Digis','MuonShower' ),
#     L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
#     L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
#     L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
#     L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' )
# )

# # process.hltL1sSingleEGorFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
# #     saveTags = cms.bool( True ),
# #     candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
# #     l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
# #     candNonIsolatedTag = cms.InputTag( "" ),
# #     l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
# #     L1SeedFilterTag = cms.InputTag( "hltL1sSingleEGor" ),
# #     l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
# #     l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
# #     ncandcut = cms.int32( 1 ),
# #     doIsolated = cms.bool( False ),
# #     region_eta_size = cms.double( 0.522 ),
# #     region_eta_size_ecap = cms.double( 1.0 ),
# #     region_phi_size = cms.double( 1.044 ),
# #     barrel_end = cms.double( 1.4791 ),
# #     endcap_end = cms.double( 2.65 )
# # )


process.EfficiencyCalculator = cms.EDAnalyzer('EfficiencyCalculator',
                                              stageL1Trigger = cms.uint32(2)
)



if reRunL1:
    process.myTask = cms.Task(process.GlobalParametersRcdSource,process.GlobalParameters,process.hltGtStage2Digis,process.hltGtStage2ObjectMap)
    process.t = cms.Path(process.myTask)
    #process.p = cms.Path(process.hltL1sSingleEGor + process.EfficiencyCalculator)
    #process.p = cms.Path(process.hltL1sSingleAndDoubleEG + process.EfficiencyCalculator)
    #process.p = cms.Path(process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau + process.EfficiencyCalculator)
    #process.p = cms.Path(process.hltL1sSingleEGNonIsoOrWithJetAndTau + process.EfficiencyCalculator)
    process.p = cms.Path(process.hltL1sSingleEG40to50 + process.EfficiencyCalculator)
    process.schedule = cms.Schedule(process.t,process.p)
else:
    process.p = cms.Path(process.EfficiencyCalculator)
    process.schedule = cms.Schedule(process.p)
