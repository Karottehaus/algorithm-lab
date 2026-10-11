from pathlib import Path
import pydicom
import matplotlib.pyplot as plt
import json

dcm_path = Path("data/ct_series/VIC-3-100001.dcm")
dataset = pydicom.dcmread(dcm_path)
# print(dataset.dir())

# Read metadata
metadata = {
    key: str(getattr(dataset, key))
    for key in dataset.dir()
    if key != "PixelData"
}

with open("ct/dicom_metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

# Extract image data
image = dataset.pixel_array
print(f"Shape: {image.shape}")
print(f"Data type: {image.dtype}")

# Visualize image
plt.imshow(image, cmap="gray")
plt.colorbar(label="Pixel value")
plt.axis("off")
plt.savefig("ct/dicom_image.png", dpi=600, bbox_inches="tight")
