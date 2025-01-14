# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/14 (Created: 2025/01/14)'

import os
import requests
from dotenv import load_dotenv

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    else:
        print("Failed to download image")

def main():
    load_dotenv()
    download_image(os.environ['YASAI_URL'], "../download_image/yasai/yasai.png")
    download_image(os.environ['MIYAKO_1_URL'], "../download_image/miyako1/miyako1.png")
    download_image(os.environ['MIYAKO_2_URL'], "../download_image/miyako2/miyako2.png")
    download_image(os.environ['FUJI_1_URL'], "../download_image/fujikatsu/fuji1.png")
    download_image(os.environ['MUSUBI_1_URL'], "../download_image/musubi1/musubi1.png")
    download_image(os.environ['MUSUBI_2_URL'], "../download_image/musubi2/musubi2.png")
    download_image(os.environ['ICHIBARIKI_URL'], "../download_image/ichibariki/ichibariki.png")
    download_image(os.environ['LIBRE_1_URL'], "../download_image/libre/libre1.png")
    download_image(os.environ['LIBRE_2_URL'], "../download_image/libre/libre2.png")
    download_image(os.environ['SUN_URL'], "../download_image/sun/sun.png")
    download_image(os.environ['SUKIYA_URL'], "../download_image/sukiya/sukiya.png")
    download_image(os.environ['TENCHI_URL'], "../download_image/tenchi/tenchi.png")


if __name__ == '__main__':
    main()