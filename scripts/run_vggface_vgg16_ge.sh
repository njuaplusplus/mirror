#!/bin/zsh
for target in 108 180
do
  python3 my_ge_blackbox_attack.py --arch_name="vgg16" --target=$target --population_size=1000 --exp_name="gpu_vggface_vgg16_$target" --use_cache
done
