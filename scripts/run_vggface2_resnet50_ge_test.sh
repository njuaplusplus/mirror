#!/bin/zsh
target="2,8"
python3 my_ge_blackbox_attack.py --arch_name="resnet50" --test_target=$target --test_only
