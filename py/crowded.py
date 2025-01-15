# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/15 (Created: 2025/01/14)'

""" 混雑度の計算を行う。 """

import cv2
import numpy as np
import re

def calc_crowd_level(image1_path, image2_path, diff_image_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1 is None or image2 is None:
        print("Error: One or both images could not be loaded.")
        return
    
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    difference = cv2.absdiff(gray_image1, gray_image2)

    cv2.imwrite(diff_image_path, difference)
    cv2.imwrite(diff_image_path, difference)

    diff_value = np.sum(difference)
    total_pixels = gray_image1.size
    diff_percentage = (diff_value / (total_pixels * 255)) * 100

    print(f"Difference image saved to {diff_image_path}")
    print(f"Total difference value: {diff_value}")
    print(f"Difference percentage: {diff_percentage:.2f}%")

    return diff_percentage


def update_html_congestion_value(html_file_path, name, new_congestion_value):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # congestionクラスの値を更新
    updated_html_content = re.sub(
        r'<td class="{name}">\d+%<\/td>',
        f'<td class="{name}">{new_congestion_value:.2f}%</td>',
        html_content
    )

    # print (r'<td class="{name}">\d+%<\/td>')
    # print (f'<td class="{name}">{new_congestion_value:.2f}%</td>')

    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_html_content)

# calc_crowd_level("download_image/libre2/S-HE3F-libre-2-0.jpg", "download_image/libre2/S-HE3F-libre-2-1.jpg", "download_image/libre2/output.png")