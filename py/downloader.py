# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/14 (Created: 2025/01/14)'

import os
import requests

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    else:
        print("Failed to download image")

def execute_download(download_image_dir):
    download_image(os.environ['YASAI_URL'], os.path.join(download_image_dir, 'yasai/yasai.png'))
    download_image(os.environ['MIYAKO_1_URL'], os.path.join(download_image_dir, 'miyako1/miyako1.png'))
    download_image(os.environ['MIYAKO_2_URL'], os.path.join(download_image_dir, 'miyako2/miyako2.png'))
    download_image(os.environ['FUJI_1_URL'], os.path.join(download_image_dir, 'fujikatsu/fuji.png'))
    download_image(os.environ['MUSUBI_1_URL'], os.path.join(download_image_dir, 'musubi1/musubi1.png'))
    download_image(os.environ['MUSUBI_2_URL'], os.path.join(download_image_dir, 'musubi2/musubi2.png'))
    download_image(os.environ['ICHIBARIKI_URL'], os.path.join(download_image_dir, 'ichibariki/ichibariki.png'))
    download_image(os.environ['LIBRE_1_URL'], os.path.join(download_image_dir, 'libre1/libre1.png'))
    download_image(os.environ['LIBRE_2_URL'], os.path.join(download_image_dir, 'libre2/libre2.png'))
    download_image(os.environ['SUN_URL'], os.path.join(download_image_dir, 'sun/sun.png'))
    download_image(os.environ['SUKIYA_URL'], os.path.join(download_image_dir, 'sukiya/sukiya.png'))
    download_image(os.environ['T1F_URL'], os.path.join(download_image_dir, 'T1F/T1F.png'))