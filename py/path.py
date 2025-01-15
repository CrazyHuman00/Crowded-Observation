# /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Asakura Hiroto'
__version__ = '1.0.0'
__date__ = '2025/01/15 (Created: 2025/01/15)'

import os

""" パス関連の処理を行う。 """

path = [
    'fujikatsu',
    'ichibariki',
    'libre1',
    'libre2',
    'miyako1',
    'miyako2',
    'musubi1',
    'musubi2',
    'sukiya',
    'sun',
    'T1F',
    'yasai'
]

def get_restaurant_name(index):
    return path[index]


def get_base_dir():
    current = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current, os.pardir, os.pardir))
    return os.path.join(parent_dir, 'crowded-observation')


def get_download_image_dir():
    base_dir = get_base_dir()
    return os.path.join(base_dir, 'download_image')


def get_image_path(index):
    base_dir = get_base_dir()
    download_image_dir = os.path.join(base_dir, 'download_image')
    return download_image_dir + '/' + path[index] + '/' + path[index] + '.png'


def get_base_image_path(index):
    base_dir = get_base_dir()
    download_image_dir = os.path.join(base_dir, 'download_image')
    return download_image_dir + '/' + path[index] + '/' + path[index] + '-base.png'


def get_output_image_path(index):
    base_dir = get_base_dir()
    download_image_dir = os.path.join(base_dir, 'download_image')
    return download_image_dir + '/' + path[index] + '/output.png'