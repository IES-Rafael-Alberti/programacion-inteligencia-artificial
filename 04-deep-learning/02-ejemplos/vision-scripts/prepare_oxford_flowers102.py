from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.io import loadmat


ROOT = Path("data/oxford_flowers102")
JPG_DIR = ROOT / "jpg"
GRAY_OUTPUT_NPZ = ROOT / "oxford_flowers102_28x28_gray.npz"
GRAY_OUTPUT_JSON = ROOT / "oxford_flowers102_28x28_gray.json"
RGB_OUTPUT_NPZ = ROOT / "oxford_flowers102_64x64_rgb.npz"
RGB_OUTPUT_JSON = ROOT / "oxford_flowers102_64x64_rgb.json"


def load_split_gray(ids: np.ndarray, labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    images = np.empty((len(ids), 28, 28), dtype=np.float32)
    targets = np.empty((len(ids),), dtype=np.int64)

    for index, image_id in enumerate(ids):
        image_path = JPG_DIR / f"image_{image_id:05d}.jpg"
        with Image.open(image_path) as image:
            image = image.convert("L").resize((28, 28), Image.Resampling.BILINEAR)
            images[index] = np.asarray(image, dtype=np.float32) / 255.0
        targets[index] = labels[image_id - 1]

    return images, targets


def load_split_rgb(ids: np.ndarray, labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    images = np.empty((len(ids), 64, 64, 3), dtype=np.float32)
    targets = np.empty((len(ids),), dtype=np.int64)

    for index, image_id in enumerate(ids):
        image_path = JPG_DIR / f"image_{image_id:05d}.jpg"
        with Image.open(image_path) as image:
            image = image.convert("RGB").resize((64, 64), Image.Resampling.BILINEAR)
            images[index] = np.asarray(image, dtype=np.float32) / 255.0
        targets[index] = labels[image_id - 1]

    return images, targets


def main() -> None:
    labels = loadmat(ROOT / "imagelabels.mat")["labels"].squeeze().astype(np.int64) - 1
    setid = loadmat(ROOT / "setid.mat")
    train_ids = setid["trnid"].squeeze().astype(np.int64)
    valid_ids = setid["valid"].squeeze().astype(np.int64)
    test_ids = setid["tstid"].squeeze().astype(np.int64)
    trainval_ids = np.concatenate([train_ids, valid_ids])

    x_train_gray, y_train = load_split_gray(trainval_ids, labels)
    x_test_gray, y_test = load_split_gray(test_ids, labels)
    x_train_rgb, _ = load_split_rgb(trainval_ids, labels)
    x_test_rgb, _ = load_split_rgb(test_ids, labels)
    class_names = np.array([f"flower_{index:03d}" for index in range(102)], dtype="<U10")

    np.savez_compressed(
        GRAY_OUTPUT_NPZ,
        x_train=x_train_gray,
        y_train=y_train,
        x_test=x_test_gray,
        y_test=y_test,
        class_names=class_names,
    )
    np.savez_compressed(
        RGB_OUTPUT_NPZ,
        x_train=x_train_rgb,
        y_train=y_train,
        x_test=x_test_rgb,
        y_test=y_test,
        class_names=class_names,
    )

    gray_summary = {
        "train_images": int(x_train_gray.shape[0]),
        "test_images": int(x_test_gray.shape[0]),
        "image_shape": list(x_train_gray.shape[1:]),
        "num_classes": int(len(class_names)),
        "class_name_example": class_names[:5].tolist(),
        "split_note": "train = official train + validation; test = official test",
    }
    rgb_summary = {
        "train_images": int(x_train_rgb.shape[0]),
        "test_images": int(x_test_rgb.shape[0]),
        "image_shape": list(x_train_rgb.shape[1:]),
        "num_classes": int(len(class_names)),
        "class_name_example": class_names[:5].tolist(),
        "split_note": "train = official train + validation; test = official test",
    }
    GRAY_OUTPUT_JSON.write_text(json.dumps(gray_summary, indent=2), encoding="utf-8")
    RGB_OUTPUT_JSON.write_text(json.dumps(rgb_summary, indent=2), encoding="utf-8")
    print(json.dumps({"gray": gray_summary, "rgb": rgb_summary}, indent=2))


if __name__ == "__main__":
    main()
