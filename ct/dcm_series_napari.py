import numpy as np
import napari

volume = np.load("ct/ct_volume.npy")

viewer = napari.Viewer(ndisplay=3)
viewer.add_image(
    volume,
    name="VIC-3-1-demo",
    colormap="inferno",
    rendering="mip",
)

napari.run()
