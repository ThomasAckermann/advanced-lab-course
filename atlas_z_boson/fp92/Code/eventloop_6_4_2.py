# Lines beginning with "#" are comments in python.
# Start your program by importing Root and some other handy modules
import ROOT 
import math
import sys
import os
import os.path

# The argparse module makes it easy to write user-friendly command-line interfaces. 
import argparse

# we add the flags -f and -n to the scripts, so we can pass arguments in the command line:
# e.g.   python eventloop.py -f someFile.root -n 10
parser = argparse.ArgumentParser(description='Analysis of Z events.')
parser.add_argument('-f', metavar='inputFile', type=str, nargs=1, help='Input ROOT file', required=True)
parser.add_argument('-n', metavar='numEvents', type=int, nargs=1, help='Number of events to process (default all)')

args = parser.parse_args()
fileName = str(args.f[0])
numEvents = -1
if args.n != None :
	numEvents = int(args.n[0])

# from now on, fileName contains the string with the path to our input file and 
# numEvents the integer of events we want to process



# Some ROOT global settings and styling
ROOT.TH1.SetDefaultSumw2()

# The execution starts here
print "Starting the analysis"

# Open the input file. The name can be hardcoded, or given from commandline as argument
myfile = None
if os.path.isfile(fileName) and os.access(fileName, os.R_OK):
	myfile = ROOT.TFile(fileName)
else:
	sys.exit("Error: Input file does not exist or is not readable")

print "Openend file %s"%myfile.GetName()

# Now you have access to everything you can also see by using the TBrowser
# Load the tree containing all the variables
myChain = ROOT.gDirectory.Get( 'mini' )
print 'myChain: ', myChain 
# Open an output file to save your histograms in (we build the filename such that it contains the name of the input file)
# RECREATE means, that an already existing file with this name would be overwritten
outfile = ROOT.TFile.Open("analysis_final"+myfile.GetName().split('/')[-1], "RECREATE")
outfile.cd()


if numEvents<0:
	nEntries = myChain.GetEntriesFast()
else:
	nEntries = numEvents 


def make_hist(bool_list, bool_events):	

	# To look at each entry in the tree, loop over it.
	# Either loop over a fixed amount of events, or over all entries (nEntries)

	weight_list = []
	for jentry in range(0, nEntries):
		# python uses indention to show which code belongs into the loop. Thus, every line that should be executed within this loop should 
		# start with at least two spaces
		nb = myChain.GetEntry(jentry)	
		if nb <= 0: continue
		weight = myChain.mcWeight
		if weight == 0:
			weight_list.append(1)
		else:
			weight_list.append(weight)
		
		if bool_list[0] == True:
			cutflow_hist.Fill("All", weight_list[-1]) 
		if bool_list[0] == True:
			cutflow_hist.Fill("Weights", weight_list[-1]) 

		# will need to be changed for Monte Carlo events
		if bool_list[0] and bool_events[jentry] == True:
			if (not myChain.trigM) and (not myChain.trigE):
				bool_events[jentry] = False
			else:
				cutflow_hist.Fill("Trigger", weight_list[-1])					
		if bool_list[1] and bool_events[jentry] == True:
			if (not myChain.passGRL):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("GRL", weight_list[-1])				
		if bool_list[2] and bool_events[jentry] == True:
			if (not myChain.hasGoodVertex):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("Vertex", weight_list[-1])					
		if bool_list[3] and bool_events[jentry] == True:
			if (myChain.lep_n != 2):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("= 2 Leptons", weight_list[-1])					
		if bool_list[4] and bool_events[jentry] == True:
			if (not myChain.lep_type[0] in [11, 13]) or (not myChain.lep_type[1] in [11, 13]) and (myChain.lep_type[0] != myChain.lep_type[1]):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("PDGID", weight_list[-1])					
		if bool_list[5] and bool_events[jentry] == True:
			if (not (myChain.lep_charge[0] == -1 * myChain.lep_charge[1])):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("Charge", weight_list[-1])					
		if bool_list[6] and bool_events[jentry] == True:
			if (myChain.lep_pt[0] < 25000) or (myChain.lep_pt[1] < 25000):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("Pt Cut", weight_list[-1])					
		if bool_list[7] and bool_events[jentry] == True:
			if ((myChain.lep_etcone20[0]/myChain.lep_pt[0] > 0.1) or (myChain.lep_etcone20[1]/myChain.lep_pt[1] > 0.1)):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("Et Isolation", weight_list[-1])					
		if bool_list[8] and bool_events[jentry] == True:
			if  (myChain.lep_ptcone30[0]/myChain.lep_pt[0] > 0.1) or (myChain.lep_ptcone30[1]/myChain.lep_pt[1] > 0.1):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("Pt Isolation", weight_list[-1])					
		if bool_list[9] and bool_events[jentry] == True:
			if  (myChain.lep_flag[0] & (1 << 9) == 0) or (myChain.lep_flag[1] & (1 << 9) == 0):
				bool_events[jentry] = False
			else:
				 cutflow_hist.Fill("Tight ID", weight_list[-1])					
		if bool_list[10] and bool_events[jentry] == True:
			l1, l2 = ROOT.TLorentzVector(),ROOT.TLorentzVector()
			l1.SetPtEtaPhiE(myChain.lep_pt[0], myChain.lep_eta[0], myChain.lep_phi[0], myChain.lep_E[0])
			l2.SetPtEtaPhiE(myChain.lep_pt[1], myChain.lep_eta[1], myChain.lep_phi[1], myChain.lep_E[1])
			l3 = l1 + l2
			mass_z = l3.M()/1000
			if (mass_z > 100) or (mass_z < 40):
				bool_events[jentry] = False				
			else:
				cutflow_hist.Fill("Z Mass", weight_list[-1])					
			# Some entries are stored in vectors, meaning they have several entries themselves
			# another loop is needed for these objects
			# e.g.:
			#print "lep_pt: ", lep_pt
			#print "lep_n: ",   myChain.lep_n

			# might be helpful, to access all 32 bits of a 32 bit integer flag individually:	
			# for bit in range ( 32 ):
			   # flagBit = lep_flag & (1 << bit)
			   # print "flagBit: ", flagBit
	return bool_events, weight_list 


# Book histograms within the output file
mass_cz, mass_lz = [1]*12, [1]*12

cutflow_hist = ROOT.TH1D("cutflow_hist",   "Total number of events selected by the consecutive criteria; ; Entries", 13, 0, 13)

canvas = ROOT.TCanvas("myCanvas", 'Analysis Plots', 200, 10, 700, 500 )
canvas.cd()

cutflow_hist.GetXaxis().FindBin("All")
cutflow_hist.GetXaxis().FindBin("Weights")
cutflow_hist.GetXaxis().FindBin("Trigger")
cutflow_hist.GetXaxis().FindBin("GRL")
cutflow_hist.GetXaxis().FindBin("Vertex")
cutflow_hist.GetXaxis().FindBin("= 2 Leptons")
cutflow_hist.GetXaxis().FindBin("PDGID")
cutflow_hist.GetXaxis().FindBin("Charge")
cutflow_hist.GetXaxis().FindBin("Pt Cut")
cutflow_hist.GetXaxis().FindBin("Et Isolation")
cutflow_hist.GetXaxis().FindBin("Pt Isolation")
cutflow_hist.GetXaxis().FindBin("Tight ID")
cutflow_hist.GetXaxis().FindBin("Z Mass")

data = [True] * nEntries
a  = [False]*12
for i in range(0, 12):
	mass_cz[i] = ROOT.TH1D("mass_c_{}".format(i),   "Distribution of the mass with {} cut(s); mass [GeV/c^2]; Entries".format(i), 100, 0, 120)
	mass_lz[i] = ROOT.TH1D("mass_l_{}".format(i),   "Distribution of the mass with {} cut(s); mass [GeV/c^2]; Entries".format(i), 100, 0, 120)
	data, weight_list = make_hist(a, data)
	for j in range(0, nEntries):
		nb = myChain.GetEntry(j)	
		if nb <= 0: continue	
		if data[j] and i >= 4:
			l1, l2 = ROOT.TLorentzVector(), ROOT.TLorentzVector()
			l1.SetPtEtaPhiE(myChain.lep_pt[0], myChain.lep_eta[0], myChain.lep_phi[0], myChain.lep_E[0])
			l2.SetPtEtaPhiE(myChain.lep_pt[1], myChain.lep_eta[1], myChain.lep_phi[1], myChain.lep_E[1])
			mass_l = l1 + l2
			mass_c = myChain.lep_E[0]**2 + myChain.lep_E[1]**2 + 2*myChain.lep_E[0]*myChain.lep_E[1] - myChain.lep_pt[0]**2 * math.cosh(myChain.lep_eta[0])**2 - 2 *  myChain.lep_pt[0] * myChain.lep_pt[1] * ( math.cos(myChain.lep_phi[0] - myChain.lep_phi[1]) + math.sinh(myChain.lep_eta[0]) * math.sinh(myChain.lep_eta[1])) - myChain.lep_pt[1]**2 * math.cosh(myChain.lep_eta[1])**2 
			if mass_c > 0:
				mass_cz[i].Fill(math.sqrt(mass_c)/1000, weight_list[j])
				mass_lz[i].Fill(mass_l.M()/1000, weight_list[j])

	mass_cz[i].Draw()
	mass_lz[i].Draw()
	a[i] = True
	if i >= 1:
		a[i-1] = False

##########################################################################
#end of the event loop
##########################################################################

# l = ROOT.TLegend(0.5, 0.5, 0.7, 0.7)
# l.AddEntry(mass_cz, "lep", "mass_cz")
# l.AddEntry(mass_lz, "lep", "mass_lz")
### The Wrap-up code (writing the files, etc) goes here
# Let's look at the histogram; create a canvas to draw it on
cutflow_hist.Draw()
#########################################################################
#########################################################################

outfile.cd()
print "Writing output to %s"%outfile.GetName()
outfile.Write()

#useful command to pause the execution of the code. Allows to see the plot before python finishes
ROOT.TPython.Prompt()
