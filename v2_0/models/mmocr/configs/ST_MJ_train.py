
train_root = '/content/drive/MyDrive/datasets'

train_img_prefix1 = f'{train_root}'
train_ann_file1 = f'{train_root}/mmocr_train.txt'

train1 = dict(
    type='OCRDataset',
    img_prefix=train_img_prefix1,
    ann_file=train_ann_file1,
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
    test_mode=False)


train_list = [train1]
