#!/usr/bin/env python3
# coding=utf-8
import os
import subprocess

from my_utils import create_folder

ALL_CACHE = {
    'resnet50_scratch_dag.pth': 'https://purdue0-my.sharepoint.com/:u:/g/personal/an93_purdue_edu/EZOXU_L8CQdHvWdWnRfV7F4BCE-JGamMjKYwBWuPk5pyVQ?e=Hmzguu&download=1',
    'stylegan_sample_z_stylegan_celeba_partial256_0.7_8_all_ws.pt': 'https://purdue0-my.sharepoint.com/:u:/g/personal/an93_purdue_edu/Eee2Fvs7269DoZ8bRVKbBjEBY6bi0z02eLc6ApOiTc-wwA?e=Bz7Zzy&download=1',
    'blackbox_attack_data/stylegan/resnet50/no_dropout/all_logits.pt': 'https://purdue0-my.sharepoint.com/:u:/g/personal/an93_purdue_edu/EVqqJuJLAu5ElAlfikeYfjkBdL2P35AwPuNkth_GoPIZNA?e=vl320x&download=1',
    'centroid_data/resnet50/test/centroid_logits.pt': 'https://purdue0-my.sharepoint.com/:u:/g/personal/an93_purdue_edu/ETW3GDEXXMtAj16IGee3nmEBJ4CcUTcQ5GEsiZVd25FOXQ?e=kMdQHp&download=1',
}


def download(filename, url):
    if not os.path.exists(filename):
        print('Downloading', filename)
        dirname = os.path.dirname(filename)
        if dirname:
            create_folder(dirname)
        subprocess.call(['wget', '--quiet', '-O', filename, url])


def main():
    for filename, url in ALL_CACHE.items():
        download(filename, url)


if __name__ == '__main__':
    main()
