test_root = '/content/drive/MyDrive/datasets'

test_img_prefix1 = f'{test_root}'

test_ann_file1 = f'{test_root}/mmocr_val.txt'

test1 = dict(
    type='OCRDataset',
    img_prefix=test_img_prefix1,
    ann_file=test_ann_file1,
    loader=dict(
        type='AnnFileLoader',
        repeat=1,
        file_format='txt',
        file_storage_backend='disk',
        parser=dict(
            type='LineStrParser',
            keys=['filename', 'text'],
            keys_idx=[0, 1],
            separator=' ')),
    pipeline=None,
    test_mode=True)

test_list = [test1]