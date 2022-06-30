from ast import parse
import jittor as jt
# from train import Trainer
# from model import NerfNetworks, HuberLoss
from tqdm import tqdm
# from utils.dataset import  NerfDataset
import argparse
import numpy as np
import os
from jnerf.runner import Runner 
from jnerf.utils.config import get_cfg, init_cfg, save_cfg
from jnerf.utils.registry import build_from_cfg,NETWORKS,SCHEDULERS,DATASETS,OPTIMS,SAMPLERS,LOSSES
import gc
# jt.flags.gopt_disable=1
jt.flags.use_cuda = 1


def main():
    assert jt.flags.cuda_archs[0] >= 61, "Failed: Sm arch version is too low! Sm arch version must not be lower than sm_61!"
    parser = argparse.ArgumentParser(description="Jittor Object Detection Training")
    parser.add_argument(
        "--config-file",
        default="",
        metavar="FILE",
        help="path to config file",
        type=str,
    )
    parser.add_argument(
        "--task",
        default="train",
        help="train,val,test",
        type=str,
    )
    
    args = parser.parse_args()

    if args.config_file:
        init_cfg(args.config_file)
        if not os.path.exists(get_cfg().log_dir):
            os.makedirs(get_cfg().log_dir)
        save_cfg(get_cfg().save_cfg)

    runner = Runner()

    if args.task == "train":
        runner.train()
    elif args.task == "test":
        runner.test()
    elif args.task == "render":
        runner.render_test(save_img=True, save_path=None, load_model=True)
    
if __name__ == "__main__":
    main()