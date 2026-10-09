import h5py

data_path = "data/260617_PK_Dino.h5"

with h5py.File(data_path, "r") as f:
    print("Top-level keys:", list(f.keys()))
    group = f["calibrated images 1"]


    def inspect(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name}, shape={obj.shape}, dtype={obj.dtype}")
        elif isinstance(obj, h5py.Group):
            print(f"Group: {name}")


    group.visititems(inspect)
