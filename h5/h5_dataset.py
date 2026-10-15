import h5py

data_path = "data/260617_PK_Dino.h5"

with h5py.File(data_path, "r") as f:
    group = f["calibrated images 1/calibrated 1"]

    for name, dataset in group.items():
        if isinstance(dataset, h5py.Dataset):
            print(f"Dataset: {name}")
            print(f"Shape: {dataset.shape}")
            print(f"Dtype: {dataset.dtype}")
