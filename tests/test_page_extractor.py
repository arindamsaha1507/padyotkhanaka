"""Test page extractor module."""

import os
import shutil

import pytest
from padyotkhanaka.page_extractor import convert_pdf_to_images, save_images


def test_convert_pdf_to_images():
    """Test convert_pdf_to_images function."""

    imgs = convert_pdf_to_images("tests/test_pdf/test.pdf")

    assert len(imgs) == 2


def test_convert_pdf_to_images_file_not_found():
    """Test convert_pdf_to_images function raises FileNotFoundError."""

    with pytest.raises(FileNotFoundError):
        convert_pdf_to_images("tests/test_pdf/does_not_exist.pdf")


def test_convert_pdf_to_images_file_not_pdf():
    """Test convert_pdf_to_images function raises ValueError."""

    with pytest.raises(ValueError):
        convert_pdf_to_images("tests/test_pdf/test.txt")


def test_save_images():
    """Test save_images function."""

    imgs = convert_pdf_to_images("tests/test_pdf/test.pdf")

    save_images(imgs, "tests/test_images")

    assert len(os.listdir("tests/test_images")) == 2

    shutil.rmtree("tests/test_images")


def test_save_images_output_path_not_found():
    """Test save_images function."""

    os.makedirs("tests/test_images", exist_ok=True)

    imgs = convert_pdf_to_images("tests/test_pdf/test.pdf")

    save_images(imgs, "tests/test_images")

    assert len(os.listdir("tests/test_images")) == 2

    shutil.rmtree("tests/test_images")


def test_save_images_output_images_list_empty():
    """Test save_images function raises ValueError."""

    with pytest.raises(ValueError):
        save_images([], "tests/test_images")


def test_save_images_output_images_names():
    """Test save_images function raises ValueError."""

    imgs = convert_pdf_to_images("tests/test_pdf/test.pdf")

    save_images(imgs, "tests/test_images")

    assert os.path.exists("tests/test_images/page_1.png")
    assert os.path.exists("tests/test_images/page_2.png")

    shutil.rmtree("tests/test_images")


def test_save_images_output_directory_check():
    """Test save_images function raises ValueError."""

    imgs = convert_pdf_to_images("tests/test_pdf/test.pdf")

    with pytest.raises(NotADirectoryError):
        save_images(imgs, "tests/test_pdf/test.pdf")
