#!/bin/bash

#SBATCH --partition=gpu
#SBATCH --gpus=1
#SBATCH --job-name=xmem_run
#SBATCH --mem=400000
#SBATCH --time=4-00:00:00
#SBATCH --output=xmem_run.txt
#SBATCH --error=xmem_run.txt

module load gcccore/12.2.0
module load python/3.10.8
module load cuda
export PYTHONPATH=/bigtemp/rgq5aw/xmemLibs:$PYTHONPATH

python eval.py --output output/d17 --dataset D17