"""The main file for the project."""

import os
import re

from akshara.varnakaarya import count_svaras

from padyotkhanaka import ocr
from padyotkhanaka import page_extractor


if not os.path.exists("resources/images"):
    images = page_extractor.convert_pdf_to_images("resources/Meghadootam.pdf")
    page_extractor.save_images(images, "resources/images")

texts = ocr.ocr_single("resources/images/page_020.png")

with open("scratch.txt", "w", encoding="utf-8") as file:
    texts = ocr.get_text_from_page_range("resources/images", 20, 25)
    punctuation_pattern = r'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0-9\'"]'

    for text in texts:
        try:
            count = count_svaras(text)
            if count == 17:
                file.write(text + "\n")
        except AssertionError:
            pass

    print(len(texts))
