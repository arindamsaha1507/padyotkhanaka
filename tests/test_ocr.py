"""Test the ocr module."""

import os
import shutil

from unittest.mock import Mock

import pytest

from padyotkhanaka.ocr import ocr_single, get_ocr_content, get_ocr_lines
from padyotkhanaka.page_extractor import convert_pdf_to_images, save_images


class DictToClass:
    """Convert a dictionary to a class."""

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)


# Define a fixture for the mock OCR client
@pytest.fixture
def mock_ocr_client(mocker):
    """Mock the OCR client."""

    return mocker.patch("padyotkhanaka.ocr.vision.ImageAnnotatorClient")


def test_ocr_single(mock_ocr_client):  # pylint: disable=redefined-outer-name
    """Test the ocr_single function."""

    mock_client_instance = Mock()
    mock_ocr_client.return_value = mock_client_instance
    mock_client_instance.text_detection.return_value.text_annotations = "dummy"

    # Call your OCR function
    images = convert_pdf_to_images("tests/test_pdf/test.pdf")
    os.makedirs("tests/test_images", exist_ok=True)
    save_images(images, "tests/test_images")
    result = ocr_single("tests/test_images/page_1.png")

    # Assert that the result is as expected
    assert result == "dummy"

    shutil.rmtree("tests/test_images")


def test_ocr_single_failure(mock_ocr_client):  # pylint: disable=redefined-outer-name
    """Test the ocr_single function raises FileNotFoundError."""

    mock_client_instance = Mock()
    mock_ocr_client.return_value = mock_client_instance
    mock_client_instance.text_detection.return_value.text_annotations = None

    images = convert_pdf_to_images("tests/test_pdf/test.pdf")
    os.makedirs("tests/test_images", exist_ok=True)
    save_images(images, "tests/test_images")

    with pytest.raises(FileNotFoundError):
        _ = ocr_single("tests/test_images/page_100.png")

    shutil.rmtree("tests/test_images")


def test_get_ocr_content():
    """Test the get_ocr_content function."""

    mock_client_instance = Mock()
    mock_ocr_client.return_value = mock_client_instance
    mock_response = [DictToClass({"description": "dummy \n content"})]
    mock_client_instance.text_detection.return_value.text_annotations = mock_response

    result = get_ocr_content(mock_response)

    assert result == "dummy \n content"


def test_get_ocr_lines():
    """Test the get_ocr_lines function."""

    mock_client_instance = Mock()
    mock_ocr_client.return_value = mock_client_instance
    mock_response = [DictToClass({"description": "dummy \n content"})]
    mock_client_instance.text_detection.return_value.text_annotations = mock_response

    result = get_ocr_lines(mock_response)

    assert result == ["dummy", "content"]
