"""The main file for the project."""

import os

from akshara.varnakaarya import count_svaras

from padyotkhanaka import ocr
from padyotkhanaka import page_extractor


if not os.path.exists("resources/images"):
    images = page_extractor.convert_pdf_to_images("resources/Meghadootam.pdf")
    page_extractor.save_images(images, "resources/images")

with open("scratch.txt", "w", encoding="utf-8") as file:
    texts = ocr.get_text_from_page_range("resources/images", 20, 109)

    for text in texts:
        if len(text) < 17:
            continue
        text = text.replace("|", "।")
        text = text.replace("।।", "॥")
        text = text.replace("ँ", "")
        text = text.replace(":", "ः")
        text = text.replace("s", "ऽ")
        text = text.replace("ॉ", " ा")
        text = text.replace("३", "०")
        text = text.replace("ॅ", "")
        try:
            count = count_svaras(text)
            if count == 17:
                file.write(text + "\n")
        except AssertionError:
            if (
                "'" not in list(text)
                and "‘" not in list(text)
                and text[-1] in ["।", "॥"]
                and 15 < len(text) < 19
            ):
                file.write("***" + text + "\n")
                print(list(text))
                # print(get_vinyaasa(text))
