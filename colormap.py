from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import matplotlib.pyplot as plt

my_colormap = LinearSegmentedColormap.from_list('my_colormap', ['#89d173', '#7fdeff', '#7f5539', '#7161ef', '#efabcd'],N = 5)


# data_to_plot = np.random.rand(5,5)
# cmap = my_colormap

# plt.imshow(data_to_plot, cmap=cmap)
# plt.colorbar()
