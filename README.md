# Official Code for MIRROR (NDSS 2022)

This is the PyTorch implementation for NDSS 2022 paper "MIRROR: Model Inversion for Deep Learning Network with High Fidelity".

Note: we only uploaded the scripts and cache files for resnet50 model. Others will be updated soon.

## Environment

```
conda env create -f environment.yml
conda activate mirror

```

## Usage

### 1. Download cache files

```
python my_download_cache.py
```

### 2. White-box invert ResNet50

Conduct the inversion.

```
zsh scripts/run_vggface2_resnet50.sh

```

Test the inversion.

```
zsh scripts/run_vggface2_resnet50_test.sh
```

### 3. Black-box invert ResNet50

Conduct the inversion.

```
zsh scripts/run_vggface2_resnet50_ge.sh

```

Test the inversion.

```
zsh scripts/run_vggface2_resnet50_ge_test.sh
```

## Reference

```
@inproceedings{taog2022better,
    title={MIRROR: Model Inversion for Deep Learning Network with High Fidelity},
    author={An, Shengwei and Tao, Guanhong and Xu, Qiuling and Liu, Yingqi and Shen, Guangyu and Yao, Yuan and Xu, Jingwei and Zhang, Xiangyu},
    booktitle={Proceedings of the Network and Distributed Systems Security Symposium (NDSS 2022)},
    year={2022}
}
```
