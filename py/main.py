# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/15 (Created: 2025/01/14)'

""" 学食アイキャッチから画像を取得して、混雑度を計算し、htmlに反映する。 """


import os
from dotenv import load_dotenv
from downloader import execute_download
from crowded import calc_crowd_level, update_html_congestion_value
from path import (
    get_image_path, 
    get_base_image_path, 
    get_output_image_path,
    get_restaurant_name
)

def main():
    # 環境変数の読み込み
    load_dotenv()

    # 画像のダウンロード
    execute_download()

    # 混雑度の計算し、その結果をhtmlに反映する
    for i in range(12):
        diff_percentage = calc_crowd_level(get_image_path(i), get_base_image_path(i), get_output_image_path(i))
        update_html_congestion_value(os.environ['HTML_FILE_PATH'], get_restaurant_name(i), diff_percentage)


if __name__ == '__main__':
    main()