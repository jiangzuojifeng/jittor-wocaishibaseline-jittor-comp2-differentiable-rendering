<!-- # JNeRF -->
<div align="center">
<img src="docs/logo.png" height="200"/>
</div>

## Introduction
本项目是第二届计图挑战赛的正式赛题项目，赛题为可微渲染新视角生成赛题，项目使用官方baseline代码JNeRF，针对部分场景提出方法调整，可给予给定数据集完成NeRF训练和新视角图像生成。
JNeRF is an NeRF benchmark based on [Jittor](https://github.com/Jittor/jittor). JNeRF supports Instant-NGP capable of training NeRF in 5 seconds and achieves similar performance and speed to the paper.

## Install
JNeRF environment requirements:

* System: **Linux**(e.g. Ubuntu/CentOS/Arch), **macOS**, or **Windows Subsystem of Linux (WSL)**
* Python version >= 3.7
* CPU compiler (require at least one of the following)
    * g++ (>=5.4.0)
    * clang (>=8.0)
* GPU compiler (optional)
    * nvcc (>=10.0 for g++ or >=10.2 for clang)
* GPU library: cudnn-dev (recommend tar file installation, [reference link](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#installlinux-tar))
* GPU supporting:
  * sm arch >= sm_61 (GTX 10x0 / TITAN Xp and above)
  * to use fp16: sm arch >= sm_70 (TITAN V / V100 and above). JNeRF will automatically use original fp32 if the requirements are not meet.
  * to use FullyFusedMLP: sm arch >= sm_75 (RTX 20x0 and above). JNeRF will automatically use original MLPs if the requirements are not meet.

**Step 1: Install the requirements**
```shell
sudo apt-get install tcl-dev tk-dev python3-tk
git clone https://github.com/Jittor/JNeRF
cd JNeRF
python -m pip install -r requirements.txt
```
If you have any installation problems for Jittor, please refer to [Jittor](https://github.com/Jittor/jittor)

**Step 2: Install JNeRF**

JNeRF is a benchmark toolkit and can be updated frequently, so installing in editable mode is recommended.
Thus any modifications made to JNeRF will take effect without reinstallation.

```shell
cd python
python -m pip install -e .
```

After installation, you can ```import jnerf``` in python interpreter to check if it is successful or not.

## Getting Started

### Datasets

项目使用官方给定的数据集，如`./data/Car`.

#### Customized Datasets

针对新数据的训练，新数据集的目录格式需与现有格式一致。指定目录下包括 `test、train、val` 三种数据，并给定相对应的参数文件（相机参数）。

### Config

训练相关配置位于`./projects/ngp/configs/`

### Train from scratch

项目基础版本的训练基于JNeRF使用如下命令进行。

```shell
python tools/run_net.py --config-file ./projects/ngp/configs/ngp_base_car.py
```

针对赛题部分场景的渲染难题，本项目提出二次渲染的方法。
首先，使用如下命令将`train`数据变化为黑色图像，根据对应数据改变python文件中的目录

```shell
python image_black.py
```

变化结果保存在`./data/Car/train_b`等文件夹，将其复制于`./data/Car/train`文件夹，对于二值化数据进行训练，将`./data/Car/transforms_train.json`中数据复制到`./data/Car/transforms_test.json`，并对于`train`数据完成渲染。

```shell
python tools/run_net.py --config-file ./projects/ngp/configs/ngp_base_car.py
```

使用如下命令对于训练图像序列进行筛选，生成筛选参数，根据对应数据改变python文件中的目录

```shell
python image_select.py
```

将`./data/Car/train`以及`./data/Car/transforms_test.json`恢复为原数据，在`./projects/ngp/configs/ngp_base_car.py`配置文件中`dataset/train/`增加`train_select = True`,参数，使用如下命令进行渲染。

```shell
python tools/run_net.py --config-file ./projects/ngp/configs/ngp_base_car.py
```

### Test with pre-trained model

训练生成的参数信息被保存在`./logs/Car/`等目录下，基于保存的参数针对`test`数据完成渲染使用以下命令，结果保存在`./logs/Car/test/`等目录下。

```shell
python tools/run_net.py --config-file ./projects/ngp/configs/ngp_base.py --task test
```

针对赛题完成所有场景`test`渲染使用以下命令，结果保存在`./result/`目录下。

```shell
python test.py
```

## Acknowledgements

The original implementation comes from the following cool project:
* [Instant-NGP](https://github.com/NVlabs/instant-ngp)
* [tiny-cuda-nn](https://github.com/NVlabs/tiny-cuda-nn)
* [Eigen](https://github.com/Tom94/eigen) ([homepage](https://eigen.tuxfamily.org/index.php?title=Main_Page))

Their licenses can be seen at `licenses/`, many thanks for their nice work!


## Citation

```
@article{hu2020jittor,
  title={Jittor: a novel deep learning framework with meta-operators and unified graph execution},
  author={Hu, Shi-Min and Liang, Dun and Yang, Guo-Ye and Yang, Guo-Wei and Zhou, Wen-Yang},
  journal={Science China Information Sciences},
  volume={63},
  number={222103},
  pages={1--21},
  year={2020}
}
@article{mueller2022instant,
    author = {Thomas M\"uller and Alex Evans and Christoph Schied and Alexander Keller},
    title = {Instant Neural Graphics Primitives with a Multiresolution Hash Encoding},
    journal = {ACM Trans. Graph.},
    issue_date = {July 2022},
    volume = {41},
    number = {4},
    month = jul,
    year = {2022},
    pages = {102:1--102:15},
    articleno = {102},
    numpages = {15},
    url = {https://doi.org/10.1145/3528223.3530127},
    doi = {10.1145/3528223.3530127},
    publisher = {ACM},
    address = {New York, NY, USA},
}
@inproceedings{mildenhall2020nerf,
  title={NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis},
  author={Ben Mildenhall and Pratul P. Srinivasan and Matthew Tancik and Jonathan T. Barron and Ravi Ramamoorthi and Ren Ng},
  year={2020},
  booktitle={ECCV},
}
```
