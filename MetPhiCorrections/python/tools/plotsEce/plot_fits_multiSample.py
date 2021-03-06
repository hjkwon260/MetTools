import ROOT
import os,sys

#ROOT.setTDRStyle()plot_vars = ["hHFPlus", "hHFMinus","egammaHFPlus" , "egammaHFMinus","hEtaPlus" , "hEtaMinus" , "h0Barrel" , "h0EndcapPlus" , "h0EndcapMinus" , "gammaBarrel", "gammaEndcapPlus" , "gammaEndcapMinus" ] #"h_HF_Plus" , "h_HF_Minus" ,  "egamma_HF_Plus" , "egamma_HF_Minus"
#plot_vars = ["hHFPlus", "hHFMinus","egammaHFPlus" , "egammaHFMinus","hEtaPlus" , "h0Barrel" , "h0EndcapPlus" , "h0EndcapMinus" , "gammaBarrel", "gammaEndcapPlus" , "gammaEndcapMinus" ] #"h_HF_Plus" , "h_HF_Minus" ,  "egamma_HF_Plus" , "egamma_HF_Minus"
plot_vars = ["hEtaMinus"]
#plot_vars = ["hHFPlus", "hHFMinus","egammaHFPlus" , "egammaHFMinus"]
#plot_vars = ["h0Barrel","h0EndcapPlus","h0EndcapMinus"]
p_vars = ["x","y"]
#p_vars = ["y"]
#h_var = "multiplicity" #sumPt , ngoodVertices
h_var = "ngoodVertices" #sumPt , ngoodVertices
#h_var = "sumPt"
file_var = "ngoodVertices" #"mult" # sumPt 
#file_var = "sumPt" 
#axis_var = "multiplicity"
#axis_var = "#Sigma p_{T}"
axis_var = "ngoodVertices"
for p_var in p_vars:
  for var in plot_vars:
    print "Now: " , var , " P" , p_var  
    DYsm30_file   = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/MCMoriond2017_8025/DY_metsm30/"+var+"_"+file_var+".root")
    DY30_file     = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/MCMoriond2017_8025/DY_met30/"+var+"_"+file_var+".root")
    DY70_file     = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/MCMoriond2017_8025/DY_met70/"+var+"_"+file_var+".root")
    #TTJets_file = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/MCMoriond2017_8025/TTJets/"+var+"_"+file_var+".root")
    #WJets_file  = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/MCMoriond2017_8025/WJets/"+var+"_"+file_var+".root")
    #Data_file    = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/Data_80X/onZ_10Aug/"+var+"_"+file_var+".root")

    #TTJets_fall_file = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/TTJets_Fall15/"+var+"_"+file_var+".root")
    #WJets_fall_file  = ROOT.TFile("/afs/hephy.at/user/e/easilar/www/METPhiCorr/WJets_Fall15/"+var+"_"+file_var+".root")
    
    #var = var.split("_")
    #var = var[0]+var[1]+var[2]
    #c_dysm30 = DYsm30_file.Get('c1_n2')
    c_dysm30 = DYsm30_file.Get('c1')
    c_dy30   = DY30_file.Get('c1')
    c_dy70   = DY70_file.Get('c1')
    #c_tt = TTJets_file.Get('c1_n2')
    #c_w  = WJets_file.Get('c1_n2')
    #c_data = Data_file.Get('c1_n2')

    #c_tt_f = TTJets_fall_file.Get('c1_n2')
    #c_w_f  = WJets_fall_file.Get('c1_n2')
    print "metPhiCorrInfoWriter_"+h_var+"_"+var+"_P"+p_var
    h_dysm30 = c_dysm30.GetPrimitive("metPhiCorrInfoWriter_"+h_var+"_"+var+"_P"+p_var)
    h_dy30 = c_dy30.GetPrimitive("metPhiCorrInfoWriter_"+h_var+"_"+var+"_P"+p_var)
    h_dy70 = c_dy70.GetPrimitive("metPhiCorrInfoWriter_"+h_var+"_"+var+"_P"+p_var)
    #print h_tt_f , "we have tt fall" 

    histo_list = [\
    #{"histo":h_dy,    "name":"DY Fall15",      "line":2,"color":ROOT.kBlue},\
    {"histo":h_dysm30,    "name":"MET<30 GeV",      "line":2,"color":ROOT.kBlue},\
    {"histo":h_dy30,    "name":"MET>30","line":2,"color":ROOT.kRed},\
    #{"histo":h_tt_f,  "name":"TTJets Fall15",  "line":4,"color":ROOT.kMagenta},\
    {"histo":h_dy70,     "name":"MET>70", "line":2,"color":ROOT.kGreen},\
    #{"histo":h_data,   "name":"Data Run2016B",   "line":2,"color":ROOT.kBlack},\
    ]

    path = "/afs/hephy.at/user/e/easilar/www/METPhiCorr/MCMoriond2017_8025/plots_DYMETTests/" 
    if not os.path.exists(path):
      os.makedirs(path)
    cb = ROOT.TCanvas("cb","cb",600,600,600,600)
    #h_dy.Draw()
    leg = ROOT.TLegend(0.6,0.6,0.8,0.7)
    leg.SetTextSize(0.05)
    leg.SetBorderSize(1)
    for histo in histo_list :
      print histo["name"]
      histo["histo"].SetLineColor(histo["color"])
      histo["histo"].SetLineWidth(histo["line"])
      histo["histo"].GetXaxis().SetRangeUser(0, 200)
      histo["histo"].GetYaxis().SetRangeUser(-4, 4)
      #histo["histo"].GetXaxis().Set(25,0,250)
      histo["histo"].SetTitle("")
      histo["histo"].GetYaxis().SetTitle("<#slash{E}_{"+p_var+"}> (GeV)")
      histo["histo"].GetXaxis().SetTitle(""+axis_var+" in "+var)
      histo["histo"].GetXaxis().SetTitleOffset(0.9)
      histo["histo"].SetStats(0)
      leg.AddEntry(histo["histo"], histo["name"],"l") 
      histo["histo"].Draw("same")
    leg.SetFillColor(0)
    leg.SetLineColor(0)
    leg.Draw()
    cb.Draw()
    cb.SaveAs(path+var+"_P"+p_var+"_"+file_var+"_.pdf")
    cb.SaveAs(path+var+"_P"+p_var+"_"+file_var+"_.png")
