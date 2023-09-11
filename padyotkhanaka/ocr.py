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
    """Returns the OCR content from the response line by line."""

    if texts:
        content = texts[0].description.split("\n")
        return [line.strip() for line in content if line]
    else:
        raise ValueError("No text found.")


def get_text_from_page_range(
    image_diractory: str, start_page: int, end_page: int
) -> list[str]:
    """Returns the OCR content from specified page range."""

    texts = []
    for i in range(start_page, end_page + 1):
        print("Processing page: ", i)
        text = ocr_single(image_diractory + "/page_" + str(i).zfill(3) + ".png")
        text = get_ocr_lines(text)
        texts.extend(text)
    return texts
