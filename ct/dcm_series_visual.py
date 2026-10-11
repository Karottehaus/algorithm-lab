import numpy as np
import pyvista as pv

volume = np.load("ct/ct_volume.npy")

# Create PyVista grid
grid = pv.ImageData()
grid.dimensions = volume.shape[::-1]
grid.point_data["VIC-3-1-demo"] = volume.ravel(order="C")

# 3D visualization
plotter = pv.Plotter()
plotter.add_volume(grid, cmap="inferno", opacity="sigmoid")
plotter.show()
