from rsciio import bruker
import numpy as np

data_path = "data/260923_GRF17_B_slab1_11-18,4cm+18,4-26cm_20um_3ms_Crop1B.bcf"

xrf_datasets = bruker.file_reader(
    data_path,
    lazy=False,
    select_type="spectrum_image",
    index="all",
    downsample=1,
    cutoff_at_kV=None,
    instrument=None
)

# print(len(xrf_datasets))
xrf_dataset = xrf_datasets[0]

# print(xrf_dataset.keys())

for axis in xrf_dataset["axes"]:
    print(axis)

spectra = xrf_dataset["data"]

print(spectra.shape)

example_spectrum = spectra[10, 20, :]
print(example_spectrum)
print(len(example_spectrum))
print(np.sum(example_spectrum != 0))
