import uproot
import ROOT
import awkward as ak
import matplotlib.pyplot as plt
import glob
import os

# Directory name
directory = "plots"

# Check if the directory exists
if not os.path.exists(directory):
    # Create the directory
    os.makedirs(directory)
    print(f"Directory '{directory}' created.")
else:
    print(f"Directory '{directory}' already exists.")

# Create a canvas
canvas = ROOT.TCanvas("canvas", "canvas", 10, 10, 1200, 800)

# Divide it into a 2x2 grid
canvas.Divide(2, 2)

# Create histograms
hmu_pt = ROOT.TH1F("hpt_1", "Muon pT; pT (GeV); Events", 50, 0, 100)
he_pt = ROOT.TH1F("he-_1", "Electron pT; pT (GeV); Events", 50, 0, 100)

# Open the ROOT file using uproot
root_files = glob.glob("./nanoAODfiles/*.root")
print(root_files)
for root_file_name in root_files:
    file = uproot.open(root_file_name)

    # Access the TTree (assuming the tree is named "Events")
    tree = file["Events"]

    # Extract the branches for Muon_pt and Electron_pt
    muon_pt = tree["Muon_pt"].array(library="ak")  # awkward array
    electron_pt = tree["Electron_pt"].array(library="ak")  # awkward array

    # Loop over the events and fill the histograms
    for event_muon_pt, event_electron_pt in zip(muon_pt, electron_pt):
        # Fill the histograms for each event
        for pt in event_muon_pt:
            hmu_pt.Fill(pt)
        for pt in event_electron_pt:
            he_pt.Fill(pt)

# Draw the histograms on the canvas
canvas.cd(1)
hmu_pt.Draw()

canvas.cd(2)
he_pt.Draw()

# Update the canvas
ROOT.gPad.Update()

# Save the canvas as an image
canvas.SaveAs("plots/TEST_muon_plots.png")

# # Open the NanoAOD ROOT file
# file = uproot.open("nanoAOD.root")  # Replace with your filename

# # Load the Events tree
# events = file["Events"]

# # Read branches (e.g., GenPart_pt and GenPart_pdgId for MC truth)
# pt = events["GenPart_pt"].arrays(library="ak")["GenPart_pt"]
# pdgId = events["GenPart_pdgId"].arrays(library="ak")["GenPart_pdgId"]

# # Flatten and select particles (example: muons, pdgId = ±13)
# muon_mask = (abs(pdgId) == 13)
# muon_pt = pt[muon_mask]

# # Flatten the pt array for histogramming
# flat_pt = ak.flatten(muon_pt)

# # Plot
# plt.hist(flat_pt, bins=50, range=(0, 100), histtype='step', label='Gen muons')
# plt.xlabel("Muon $p_T$ [GeV]")
# plt.ylabel("Counts")
# plt.title("Generated Muon $p_T$ Distribution")
# plt.legend()
# plt.grid(True)
# plt.show()
