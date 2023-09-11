"""Module to test the OCR API from Google Cloud Vision."""

from typing import Any

from google.cloud import vision  # pylint: disable=import-error


def ocr_single(in_path: str) -> None | list[Any]:
    """Detects text in a single image."""

    client = vision.ImageAnnotatorClient()

    with open(in_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)  # pylint: disable=no-member
    texts = response.text_annotations

    return texts
