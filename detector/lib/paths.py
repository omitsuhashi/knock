from pathlib import Path


def make_filepath_list() -> (list[Path], list[Path], list[Path], list[Path]):
    data_path = Path.cwd().parent.joinpath('data')
    voc_path = data_path.joinpath('VOCdevkit', 'VOC2012')
    img_dir = voc_path.joinpath('JPEGImages')
    anno_dir = voc_path.joinpath('Annotations')

    train_list_path = voc_path.joinpath('ImageSets', 'Main', 'train.txt')
    val_list_path = voc_path.joinpath('ImageSets', 'Main', 'val.txt')

    train_img_list = list()
    train_anno_list = list()
    val_img_list = list()
    val_anno_list = list()

    with open(train_list_path, 'r') as f:
        for train in f:
            img_name = f'{train}.jpg'
            anno_name = f'{train}.xml'
            train_img_list.append(img_dir.joinpath(img_name))
            train_anno_list.append(anno_dir.joinpath(anno_name))
    with open(val_list_path, 'r') as f:
        for val in f:
            img_name = f'{val}.jpg'
            anno_name = f'{val}.xml'
            val_img_list.append(img_dir.joinpath(img_name))
            val_anno_list.append(anno_dir.joinpath(anno_name))

    return train_img_list, train_anno_list, val_img_list, val_anno_list


if __name__ == '__main__':
    make_filepath_list()
