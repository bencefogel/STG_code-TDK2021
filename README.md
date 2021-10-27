# TDK2021
code of STG model network with currentscape visualization and current contribution calculations

This code was used to generate Figure 1.

For currentscape visualization and current contribution calculations we used AB5, LP4 and PY5 neurons in the network. These can be selected in plot_threeComp _and_currentContributions.py. To run this file, first integrate_and_getCurrents_threeComp.py needs to be run and currents_visualization_threeComp.py needs to be in the working directory.

colormap.py and currents_comparison.py create the comparative barplots of current contributions. Similarly to Currentscape visualization, first integrate_and_getCurrents_threeComp.py needs to be run.

Keep in mind that currentscape visualization might take a lot of time depending on the temporal resolution and simulation duration.
