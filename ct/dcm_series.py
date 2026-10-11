from pathlib import Path
import pydicom
import numpy as np

data_path = Path("data/ct_series")
datasets = [pydicom.dcmread(path) for path in data_path.iterdir()]

datasets.sort(key=lambda ds: float(ds.ImagePositionPatient[2]))

# Stack slices into a 3D volume
volume = np.stack([ds.pixel_array for ds in datasets])
print(f"Volume shape: {volume.shape}")
print(f"Data type: {volume.dtype}")
np.save("ct/ct_volume.npy", volume)
