#!/bin/bash


# bash 2_main_ex_save_pid.sh > 2_TEST_PID.out 2>&1 &


echo "TIME START"
date +'%d/%m/%Y %H:%M:%S'
echo
echo "PID:" $$
echo

# train_test="TRAIN"
train_test="TEST"
listFASTA=/home/pauline/Bureau/MNHN_RESULT/1_DATA/Pfam_split/Pfam_$train_test/
echo "listFASTA = /home/pauline/Bureau/MNHN_RESULT/1_DATA/Pfam_split/Pfam_$train_test/"


count=0
batch_size=99
n_file=0
start=`date +%s`

for entry in "$listFASTA"/*;
    do  
        if [ $count -lt $batch_size ];
        then 
            nohup python3 2_main_ex_save_pid.py $entry $train_test &
            let count=count+1
            
        else
            nohup python3 2_main_ex_save_pid.py $entry $train_test &
            let count=count+1
            wait
            n_file=$(($n_file + $count))
            count=0
        fi
    done


n_file_final=$(($n_file + $count))
echo "n_file_final:" $n_file_final

wait
end=`date +%s`
runtime=$((end-start))

echo
echo "DONE IN: $runtime s"
