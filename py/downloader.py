# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/14 (Created: 2025/01/14)'

""" 学食アイキャッチから画像を取得する。 """

import os
import requests
from path import get_image_path

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    else:
        print("Failed to download image")

def execute_download():
    download_image(os.environ['FUJI_1_URL'], get_image_path(0))
    download_image(os.environ['ICHIBARIKI_URL'], get_image_path(1))
    download_image(os.environ['LIBRE_1_URL'], get_image_path(2))
    download_image(os.environ['LIBRE_2_URL'], get_image_path(3))
    download_image(os.environ['MIYAKO_1_URL'], get_image_path(4))
    download_image(os.environ['MIYAKO_2_URL'], get_image_path(5))
    download_image(os.environ['MUSUBI_1_URL'], get_image_path(6))
    download_image(os.environ['MUSUBI_2_URL'], get_image_path(7))
    download_image(os.environ['SUKIYA_URL'], get_image_path(8))
    download_image(os.environ['SUN_URL'], get_image_path(9))
    download_image(os.environ['T1F_URL'], get_image_path(10))
    download_image(os.environ['YASAI_URL'], get_image_path(11))