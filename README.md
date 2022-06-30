# Jittor 可微渲染新视角生成 NeRF/NGP

## 简介

本项目为[第二届计图人工智能挑战赛](https://www.educoder.net/competitions/index/Jittor-3)-赛题二：可微渲染新视角生成的 A 榜提交代码。

队伍名称：sequence

队伍学校：清华大学

队伍人员：秦若愚（队长）、李正远

## 环境配置

本项目的所有训练及生成过程均可在 1 张 3090 GPU 上完成。由于针对不同场景使用了不同的算法，因此运行环境共有 2 套，下面分别介绍。

### NeRF

#### 运行环境

- ubuntu 20.04 LTS
- python >= 3.8
- jittor >= 1.3.3

#### 安装依赖

在 NeRF 目录下执行以下命令

```bash
python -m pip install -r requirements.txt
```

### NGP

#### 运行环境

- ubuntu 20.04 LTS
- python >= 3.8
- jittor >= 1.3.3

#### 安装依赖

在 NGP 目录下执行以下命令

```bash
sudo apt-get install tcl-dev tk-dev python3-tk
python -m pip install -r requirements.txt
cd python
python -m pip install -e .
```

## 训练&生成

###### Easyship

首先将 NeRF/configs/Easyship.txt 中 basedir（输出目录）、datadir（数据目录）修改为合适的目录，然后在 `NeRF` 环境下，进入 NeRF 目录并运行以下命令

```bash
python nerf.py --config ./configs/Easyship.txt
```

运行完成后便可在 basedir 下看到训练的 checkpoints 和生成结果。

###### Car

首先将 NeRF/configs/Car.txt 中 basedir、datadir 修改为合适的目录，然后在 `NeRF` 环境下，进入 NeRF 目录并运行以下命令

```bash
python nerf.py --config ./configs/Car.txt
```

运行完成后便可在 basedir 下看到训练的 checkpoints 和生成结果。

###### Coffee

首先将 NGP/projects/ngp/configs/coffee.py 中 dataset_dir（数据目录）、log_dir（输出目录）修改为合适的目录，然后在 `NGP` 环境下，进入 NGP 目录并运行以下命令

```bash
bash bash/run_coffee.sh
```

运行完成后便可在 log_dir下看到生成结果。

###### Scar

首先将 NGP/projects/ngp/configs/scar.py 中 dataset_dir、log_dir 修改为合适的目录，然后在 `NGP` 环境下，进入 NGP 目录并运行以下命令

```bash
bash bash/run_scar.sh
```

运行完成后便可在 log_dir下看到生成结果。

###### Scarf

首先将 NGP/projects/ngp/configs/scarf.py 中 dataset_dir、log_dir 修改为合适的目录，然后在 `NGP` 环境下，进入 NGP 目录并运行以下命令

```bash
bash bash/run_scarf.sh
```

运行完成后便可在 log_dir下看到生成结果。

## 致谢

### 代码框架

本项目代码基于以下两个项目完成：

1. https://github.com/Jittor/jrender
2. https://github.com/Jittor/JNeRF

### 参考文献

1. Mildenhall B, Srinivasan P P, Tancik M, et al. Nerf: Representing scenes as neural radiance fields for view synthesis[C]//European conference on computer vision. Springer, Cham, 2020: 405-421.
2. MüllerT, Evans A, Schied C, et al., Instant Neural Graphics Primitives with a Multiresolution Hash Encoding, arXiv: 2201.05989, 2022. 