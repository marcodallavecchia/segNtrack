# segNtrack
## A pipeline for the segmentation and tracking of single cells in 2D coltures

## Introduction
This repository is a showcase of a pipeline of single cell segmentation and tracking to extract useful information (such as intensity over time) from fluorescence intensity images. This data was acquired during my PhD and the pipeline was used to analyze it. I present it here with two example datasets (an _easy_ one as default and a _difficult_ one), hoping it might be useful for me and others in the future.

## Example results
### Nuclear segmentation
<img src="results/nuclei_boundaries.png" alt="nuclei" width="450"/>

### Cell segmentation
<img src="results/cell_boundaries.png" alt="cells" width="450"/>

### Segmentation and tracking
<img src="results/segmentation_animation.gif" alt="tracking-animation" width="450"/>

## Summary workflow
The main goal was to extract average fluorescence intensity over time of single cells in different conditions. In order to do this the pipeline involves the following steps:

1. Load data with [Tifffile](https://pypi.org/project/tifffile/). Each _channel_ is loaded independently as a separate 3D numpy array. Visualize that data -> scripts/01_image_exploration.ipynb
2. Segment the nuclei using Hoechst stain _channel_ using [StarDist](https://github.com/stardist/stardist) model. This segmentation is also done for every frame independently. -> scripts/02_stardist_nuclear_segmentation_plus_tracking.ipynb
3. Segment the appropriate _channel_ using [Cellpose](https://www.cellpose.org/) (cyto2 model). This segmentation is done for every frame (slice of 3D array) independently -> scripts/03_cellpose_segmentation.ipynb
4. Track every segmented cell and every segmented nucleus in time using [BayesianTracker](https://github.com/quantumjot/BayesianTracker) 
5. Filter and / or select only cells and nuclei that you want for the analysis -> I have integrated point 4 and 5 in corresponding notebooks 02 and 03
6. Calculate average fluorescence intensities for desider _channels_ in cytoplasmatic and nuclear regions -> scripts/04_nuclear_cytoplasmatic_props.ipynb
7. Optional: Manipulate / plot data as needed  -> scripts/04_nuclear_cytoplasmatic_props.ipynb

## Installation
I admit this my first time deploying a relatively-large project, and this onen is not exactly dependency-light. I have tried my best to create a conda environment that can be reproduced.

To run the pipeline create an environment using the env.yml file using conda.

```
conda env create --file env.yml
```

Then start a jupyter lab instance:

```
jupyter lab
```

## Tested on
- Python 3.7.6
- Windows 10.0.19043 Build 19043 (Windows 10 Pro)