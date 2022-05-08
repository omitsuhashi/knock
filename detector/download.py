import tarfile
import urllib.request
from pathlib import Path
from typing import Optional

from tqdm import tqdm

root_dir = Path.cwd()
data_dir = root_dir.joinpath('data')
data_dir.mkdir(exist_ok=True)
weight_dir = root_dir.joinpath('weights')
weight_dir.mkdir(exist_ok=True)

pbar: Optional[tqdm] = None


def _progress(block_count: int, block_size: int, total_size: int):
    global pbar
    if pbar is None:
        pbar = tqdm(total=total_size)
    else:
        size = block_size * block_count
        pbar.update(size)
        # reset global bar
        if pbar.total == total_size:
            pbar = None


def download_voc_dataset():
    voc_filename = 'voc-2012.tar'
    voc_path = data_dir.joinpath(voc_filename)
    if not voc_path.exists():
        url = 'http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar'
        urllib.request.urlretrieve(url, voc_path, _progress)
        with tarfile.TarFile(voc_path) as tar:
            tar.extractall(data_dir)


def download_weight():
    target_path = weight_dir.joinpath('vgg16.pth')
    if not target_path.exists():
        url = 'https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth'
        urllib.request.urlretrieve(url, target_path, _progress)


def download_sdd_300():
    url = 'https://s3.amazonaws.com/amdegroot-models/ssd300_mAP_77.43_v2.pth'
    target_path = weight_dir.joinpath('ssd300.pth')

    if not target_path.exists():
        urllib.request.urlretrieve(url, target_path, _progress)


if __name__ == '__main__':
    download_voc_dataset()
    download_weight()
    download_sdd_300()
