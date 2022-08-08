#!/bin/bash

# bash 1_main_3d_count.sh > 1.out 2>&1 &

echo "TIME START"
date +'%d/%m/%Y %H:%M:%S'
echo
echo "PID:" $$
echo

start=`date +%s`

name_folder=OUTPUT_CUBE_6_40_50_$$
mkdir $name_folder

listDirection=("ol" "or" "dl" "dr")

for direction in ${listDirection[@]};
    do
    nohup python3 1_main_3d_count.py $direction > $name_folder/"$direction".out 2>&1 &
    done;

wait
end=`date +%s`
runtime=$((end-start))
echo
echo "3D COUNT"
echo "DONE IN: $runtime s"
