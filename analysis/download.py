import urllib.request
import zipfile
from pathlib import Path

root_dir = Path.cwd()
data_dir = root_dir.joinpath('data')
data_dir.mkdir(exist_ok=True)


def download():
    url = 'https://www.shuwasystem.co.jp/support/download/5875/sample_100knocks.zip'
    target_path = data_dir.joinpath('analyze.zip')
    if not target_path.exists():
        urllib.request.urlretrieve(url, target_path)

    with zipfile.ZipFile(target_path) as zf:
        for f in zf.namelist():
            zf.extract(f, data_dir)
            break


if __name__ == '__main__':
    download()
