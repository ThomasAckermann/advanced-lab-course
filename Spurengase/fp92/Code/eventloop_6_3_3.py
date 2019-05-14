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
outfile = ROOT.TFile.Open("analysis_redo"+myfile.GetName().split('/')[-1], "RECREATE")
outfile.cd()

# Book histograms within the output file


vxp_z = ROOT.TH1D("vxp_z",   "Distribution of the interaction vertex along the z-axis; z [mm]; Entries", 1000, -300, 300)
lep_n = ROOT.TH1D("lep_n",   "Distribution of the number of leptons; number; Entries", 10, 0, 10)
lep_pt = ROOT.TH1D("lep_pt",   "Distribution of the transversal momentum; p_t [GeV/c]; Entries", 1000, 0, 400)
lep_eta = ROOT.TH1D("lep_eta",   "Distribution of the pseudo rapidity; eta; Entries", 1000, -4, 4)
lep_flag = ROOT.TH1D("lep_flag",   "Distribution of the transversal momentum; p_t [GeV/c]; Entries", 1000, 0, 1000)
lep_E = ROOT.TH1D("lep_E",   "Distribution of the energy; E [GeV]; Entries", 1000, 0, 450)
lep_phi = ROOT.TH1D("lep_phi",   "Distribution of phi;phi [rad]; Entries", 1000, -4, 4)
mass_cz = ROOT.TH1D("mass_c",   "Distribution of the mass; mass [GeV/c^2]; Entries", 1000, 0, 120)



# To look at each entry in the tree, loop over it.
# Either loop over a fixed amount of events, or over all entries (nEntries)
if numEvents<0:
    nEntries = myChain.GetEntriesFast()
else:
    nEntries = numEvents 


for jentry in range(0, nEntries):
    # python uses indention to show which code belongs into the loop. Thus, every line that should be executed within this loop should 
    # start with at least two spaces 
    nb = myChain.GetEntry(jentry)
    if nb <= 0: continue
    # will need to be changed for Monte Carlo events
    weight = 1 
    for i in range(myChain.lep_n):
        if myChain.lep_n == 2:
            lep_pt.Fill(myChain.lep_pt[i]/1000, weight)
            lep_eta.Fill(myChain.lep_eta[i], weight) 
            lep_E.Fill(myChain.lep_E[i]/1000, weight)
            lep_phi.Fill(myChain.lep_phi[i], weight)
            vxp_z.Fill(myChain.vxp_z, weight)
            lep_n.Fill(myChain.lep_n, weight) 
            mass_c = 2 * myChain.lep_E[0]*myChain.lep_E[1] -2 * myChain.lep_pt[0] * myChain.lep_pt[1] * (math.cos(myChain.lep_phi[0]) * math.cos(myChain.lep_phi[1]) + math.sin(myChain.lep_phi[0]) * math.sin(myChain.lep_phi[1]) + math.sinh(myChain.lep_eta[0]) * math.sinh(myChain.lep_eta[1]))
            if mass_c > 0:
                mass_cz.Fill(math.sqrt(mass_c)/1000, weight)
       	    else:
                pass
        else:
            pass
    # Some entries are stored in vectors, meaning they have several entries themselves
    # another loop is needed for these objects
    # e.g.:
    #print "lep_pt: ", lep_pt
    #print "lep_n: ",   myChain.lep_n

    # might be helpful, to access all 32 bits of a 32 bit integer flag individually:	
    #for bit in range ( 32 ):
       # flagBit = lep_flag & (1 << bit)
       # print "flagBit: ", flagBit
##########################################################################
#end of the event loop
##########################################################################


### The Wrap-up code (writing the files, etc) goes here
# Let's look at the histogram; create a canvas to draw it on
canvas = ROOT.TCanvas("myCanvas", 'Analysis Plots', 200, 10, 700, 500 )
canvas.cd()
vxp_z.Draw()
lep_n.Draw()
lep_pt.Draw()
lep_eta.Draw()
lep_E.Draw()
lep_phi.Draw()
mass_cz.Draw()
#########################################################################
#########################################################################

outfile.cd()
print "Writing output to %s"%outfile.GetName()
outfile.Write()

#useful command to pause the execution of the code. Allows to see the plot before python finishes
ROOT.TPython.Prompt()
