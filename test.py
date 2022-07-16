from ast import parse
import shutil
import jittor as jt
# from train import Trainer
# from model import NerfNetworks, HuberLoss
from tqdm import tqdm
# from utils.dataset import  NerfDataset
import argparse
import numpy as np
import os
from jnerf.runner import Runner 
from jnerf.utils.config import init_cfg
# jt.flags.gopt_disable=1
jt.flags.use_cuda = 1

def test(cfg_path):
    assert jt.flags.cuda_archs[0] >= 61, "Failed: Sm arch version is too low! Sm arch version must not be lower than sm_61!"
    parser = argparse.ArgumentParser(description="Jittor Object Detection Training")
    parser.add_argument(
        "--config-file",
        default=cfg_path,
        metavar="FILE",
        help="path to config file",
        type=str,
    )
    parser.add_argument(
        "--task",
        default="test",
        help="train,val,test",
        type=str,
    )
    parser.add_argument(
        "--save_dir",
        default="",
        type=str,
    )

    
    args = parser.parse_args()

    assert args.task in ["train","test","render"],f"{args.task} not support, please choose [train, test, render]"
    if args.config_file:
        init_cfg(args.config_file)
    runner = Runner()

    if args.task == "train":
        runner.train()
    elif args.task == "test":
        runner.test(True)
    elif args.task == "render":
        runner.render(True, args.save_dir)
        
def copy_file(src_folder,dst_folder):
    file_list = os.listdir(src_folder)
    for file in file_list:
        shutil.copyfile(os.path.join(src_folder,file), os.path.join(dst_folder,file))    

def main():
    test("./projects/ngp/configs/ngp_comp_car.py")
    copy_file('./logs/Car/test','./result')
    test("./projects/ngp/configs/ngp_comp_coffee.py")
    copy_file('./logs/Coffee/test','./result')
    test("./projects/ngp/configs/ngp_comp_easyship.py")
    copy_file('./logs/Easyship/test','./result')
    test("./projects/ngp/configs/ngp_comp_scar.py")
    copy_file('./logs/Scar/test','./result')
    test("./projects/ngp/configs/ngp_comp_scarf.py")
    copy_file('./logs/Scarf/test','./result')

if __name__ == "__main__":
    main()