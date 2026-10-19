from pathlib import Path
import pydicom
import numpy as np
from tqdm import tqdm

data_path = Path("data/ct_series")
output_path = Path("ct/ct_volume.npy")

files = sorted(
    data_path.iterdir(),
    key=lambda p: float(
        pydicom.dcmread(
            p, stop_before_pixels=True
        ).ImagePositionPatient[2]
    )
)

# Read first slice to determine shape and dtype
first_slice = pydicom.dcmread(files[0]).pixel_array

volume = np.lib.format.open_memmap(
    output_path,
    mode="w+",
    dtype=first_slice.dtype,
    shape=(len(files), *first_slice.shape)
)

for i, path in enumerate(tqdm(files, desc="Writing CT slices", unit="slice")):
    volume[i] = first_slice if i == 0 else pydicom.dcmread(path).pixel_array

volume.flush()
del volume
