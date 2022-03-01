# This is work-in-progress!
# I am slowly generalizing and testing the code for a broader use

## Introduction
This repository is a showcase of a pipeline of single cell segmentation and tracking to extra useful information (such as intensity over time) form fluorescence intensity images. This data was acquired during my PhD and the pipeline was used to analyze it. I present it here with an example dataset, hoping it might be useful for me and others in the future.

## Summary workflow
The main goal of this analysis was to extract average intensity values for different _channels_ over time of single cells for a [FRET measurement](https://en.wikipedia.org/wiki/F%C3%B6rster_resonance_energy_transfer), following pharmacological stimulations. It was of interest to verify the FRET response in the cytoplasmatic (cytoplasm only) and nuclear (nucleus only) regions. So, in order to do this the pipeline involves the following steps:

1. Load data with [Tifffile](https://pypi.org/project/tifffile/). Each _channel_ is loaded independently as a separate 3D numpy array.
2. Segment the appropriate _channel_ (in my case _DA_, i.e. acceptor excitation, acceptor emission _channel_) using [Cellpose](https://www.cellpose.org/) (cyto2 model). This segmentation is done for every frame (slice of 3D array) independently
3. Segment the nuclei using Hoechst stain _channel_ using [StarDist](https://github.com/stardist/stardist) model. This segmentation is also done for every frame independently.
4. Track every segmented cell and every segmented nucleus in time usign [BayesianTracker](https://github.com/quantumjot/BayesianTracker)
5. Filter and / or select only cells and nuclei that you want for the analysis
6. Calculate average fluorescence intensities for desider _channels_ in cytoplasmatic and nuclear regions
7. Optional: Manipulate / plot data as needed