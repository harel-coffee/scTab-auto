import os


def get_paths(cluster: str, model: str):
    if cluster == 'jsc':
        return (
            os.path.join('/p/scratch/hai_cellnet/tb_logs/', model),
            os.path.join('/p/scratch/hai_cellnet/tb_logs', model),
            '/p/scratch/hai_cellnet/merlin_cxg_2023_05_15_sf-log1p'
        )
    elif cluster == 'lrz':
        return (
            os.path.join('/mnt/dssfs02/tb_logs/', model),
            os.path.join('/mnt/dssfs02/tb_logs/', model),
            '/mnt/dssmcmlfs01/merlin_cxg_2023_05_15_sf-log1p'
        )
    elif cluster == 'icb':
        return (
            os.path.join('/lustre/scratch/users/felix.fischer/tb_logs', model),
            os.path.join('/lustre/scratch/users/felix.fischer/tb_logs', model),
            '/lustre/scratch/users/felix.fischer/merlin_cxg_2023_05_15_sf-log1p'
        )
    else:
        raise ValueError(f'Only "jsc", "icb" or "lrz" are supported as cluster. You supplied: {cluster}')


def get_model_checkpoint(checkpoint_path, checkpoint):
    if checkpoint is None:
        return None
    else:
        return os.path.join(checkpoint_path, 'default', checkpoint)
