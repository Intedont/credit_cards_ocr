_base_ = [
    './default_runtime.py',
    './satrn_pipeline.py',
    './ST_MJ_train.py',
    './academic_test.py',
    './schedule_adam_step_6e.py',
]

train_list = {{_base_.train_list}}
test_list = {{_base_.test_list}}

train_pipeline = {{_base_.train_pipeline}}
test_pipeline = {{_base_.test_pipeline}}

label_convertor = dict(
    type='AttnConvertor', dict_list=list('0123456789 '), with_unknown=False)

model = dict(
    type='SATRN',
    backbone=dict(type='ShallowCNN', input_channels=3, hidden_dim=512),
    encoder=dict(
        type='SatrnEncoder',
        n_layers=12,
        n_head=8,
        d_k=512 // 8,
        d_v=512 // 8,
        d_model=512,
        n_position=100,
        d_inner=512 * 4,
        dropout=0.1),
    decoder=dict(
        type='NRTRDecoder',
        n_layers=6,
        d_embedding=512,
        n_head=8,
        d_model=512,
        d_inner=512 * 4,
        d_k=512 // 8,
        d_v=512 // 8),
    loss=dict(type='TFLoss'),
    label_convertor=label_convertor,
    max_seq_len=16)

# optimizer
optimizer = dict(type='Adam', lr=3e-4)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='step', step=[3, 4])

data = dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    val_dataloader=dict(samples_per_gpu=1),
    test_dataloader=dict(samples_per_gpu=1),
    train=dict(
        type='UniformConcatDataset',
        datasets=train_list,
        pipeline=train_pipeline),
    val=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline),
    test=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline))

evaluation = dict(interval=1, metric='acc')
