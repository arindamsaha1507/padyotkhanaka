"""Module to test the OCR API from Google Cloud Vision."""

from typing import Any

from google.cloud import vision  # pylint: disable=import-error


def ocr_single(in_path: str) -> list[Any]:
    """Detects text in a single image."""

    client = vision.ImageAnnotatorClient()

    with open(in_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)  # pylint: disable=no-member
    texts = response.text_annotations

    return texts


def get_ocr_content(texts: list[Any]) -> str:
    """Returns the OCR content from the response."""

    if texts:
        return texts[0].description
    else:
        raise ValueError("No text found.")


def get_ocr_lines(texts: list[Any]) -> list[str]:
    """Returns the OCR content from the response."""

    if texts:
        content = texts[0].description.split("\n")
        return [line.strip() for line in content if line]
    else:
        raise ValueError("No text found.")
