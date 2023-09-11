"""Module to extract each page of a PDF as a separate image."""

import os
import shutil
from typing import Any

from pdf2image import convert_from_path


def convert_pdf_to_images(pdf_path) -> list[Any]:
    """Convert each page of a PDF to a separate image."""

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File {pdf_path} does not exist.")

    if not pdf_path.endswith(".pdf"):
        raise ValueError(f"File {pdf_path} is not a PDF.")

    print(f"Reading pdf from {pdf_path}...")

    images = convert_from_path(pdf_path)

    print(f"Extracted {len(images)}.")

    return images


def save_images(images, output_dir) -> None:
    """Save each image in a list to a directory."""

    if not images:
        raise ValueError("List of images is empty.")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.makedirs(output_dir, exist_ok=True)

    print("Saving images...")

    str_len = len(str(len(images)))

    for i, image in enumerate(images):
        output_file = os.path.join(output_dir, f"page_{str(i+1).zfill(str_len)}.png")
        image.save(output_file, "PNG")

    print(f"Saved {len(images)} pages to {output_dir}.")
