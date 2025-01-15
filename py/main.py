# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/14 (Created: 2025/01/14)'


import os
from dotenv import load_dotenv
from downloader import execute_download
from crowded import calc_crowd_level

def main():
    # 環境変数の読み込み
    load_dotenv()

    # パスの設定
    current = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current, os.pardir, os.pardir))
    base_dir = os.path.join(parent_dir, 'crowded-observation')
    download_image_dir = os.path.join(base_dir, 'download_image')

    # 画像のダウンロード
    execute_download(download_image_dir)

    # 混雑度の計算
    calc_crowd_level('download_image/fujikatsu/fuji.png', 'download_image/fujikatsu/fuji-base.png', 'download_image/fujikatsu/output.png')
    calc_crowd_level('download_image/ichibariki/ichibariki.png', 'download_image/ichibariki/ichibariki-base.png', 'download_image/ichibariki/output.png')
    calc_crowd_level('download_image/libre1/libre1.png', 'download_image/libre1/libre1-base.png', 'download_image/libre1/output.png')
    calc_crowd_level('download_image/libre2/libre2.png', 'download_image/libre2/libre2-base.png', 'download_image/libre2/output.png')
    calc_crowd_level('download_image/miyako1/miyako1.png', 'download_image/miyako1/miyako1-base.png', 'download_image/miyako1/output.png')
    calc_crowd_level('download_image/miyako2/miyako2.png', 'download_image/miyako2/miyako2-base.png', 'download_image/miyako2/output.png')
    calc_crowd_level('download_image/musubi1/musubi1.png', 'download_image/musubi1/musubi1-base.png', 'download_image/musubi1/output.png')
    calc_crowd_level('download_image/musubi2/musubi2.png', 'download_image/musubi2/musubi2-base.png', 'download_image/musubi2/output.png')
    calc_crowd_level('download_image/sukiya/sukiya.png', 'download_image/sukiya/sukiya-base.png', 'download_image/sukiya/output.png')
    calc_crowd_level('download_image/sun/sun.png', 'download_image/sun/sun-base.png', 'download_image/sun/output.png')
    calc_crowd_level('download_image/T1F/T1F.png', 'download_image/T1F/T1F-base.png', 'download_image/T1F/output.png')
    calc_crowd_level('download_image/yasai/yasai.png', 'download_image/yasai/yasai-base.png', 'download_image/yasai/output.png')

    # 計算結果をhtmlに反映


if __name__ == '__main__':
    main()