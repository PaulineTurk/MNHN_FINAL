"""
Brier Score comuting without contextual amico-acids
"""



# IMPORTS
import csv
import numpy as np


import sys
from pathlib import Path
file = Path(__file__).resolve()
sys.path.append(file.parents[0])

# FUNCTIONS

def score_brier_id(aa_origine, aa_destination, alphabet):
    # 2 si aa_origine != de aa_destination
    # 0 sinon
    score_brier = 0
    for aa in alphabet:
        if aa == aa_origine:
            proba = 1
        else:
            proba = 0
        score_brier += (proba - int(aa == aa_destination))**2
    return score_brier


def score_brier_stationnary(freq_aa, aa_destination, alphabet):
    # freq aa des tables 2D de fréq
    # aa_origine: not needed in fact
    
    score_brier = 0
    for aa in alphabet:
        score_brier += (freq_aa[aa] - int(aa == aa_destination))**2
    return score_brier


def score_brier_mix(aa_origine,freq_aa, aa_destination, alphabet):
    score_brier = 0
    if aa_origine == aa_destination:
        score_brier = score_brier_id(aa_origine, aa_destination, alphabet)
    else:
        score_brier = score_brier_stationnary(freq_aa, aa_destination, alphabet)
    
    return score_brier

def score_brier_mixte(pid, aa_origine,freq_aa, aa_destination, alphabet):

    # get freq normalised in case of change predicted
    freq_aa_change = freq_aa.copy()
    # print(freq_aa_change)

    freq_aa_change.pop(aa_origine)

    total = sum(freq_aa_change.values())
    freq_aa_change_normal = {key: value / total for key, value in freq_aa_change.items()}

    # total = sum(freq_aa_change_normal.values())
    # print(total)

    # Brier Score Computed
    score_brier = 0
    for aa in alphabet:
        if aa != aa_origine:
            proba = (1 - pid) * freq_aa_change_normal[aa]
        else:
            proba = pid

        score_brier += (proba - int(aa == aa_destination))**2
    
    return score_brier





def pid_local(row, L):
    count = 0

    for i in range(1,L+1):
        if row[f"aa_ol_{i}"] == row[f"aa_dl_{i}"]:
            count += 1
        if row[f"aa_or_{i}"] == row[f"aa_dr_{i}"]:
            count += 1
    return count/(2*L)


# PARAMETERS
L = 6
PID_INF = 40
PID_SUP = 50

# NAME_FILE_EXAMPLES = "subset_PID"
# NAME_FILE_EXAMPLES = "EX_BRIER_TEST_1M_PID"

# NAME_FILE_EXAMPLES = "subset"
NAME_FILE_EXAMPLES = "EX_BRIER_TEST_1M"

# PATH FOR THE PRE-PROCESSED DATA TEST EXAMPLES
# DATA_EXEMPLES = f"{file.parents[1]}/MNHN_RESULT/4_EXAMPLE_TEST_1M_PID/{L}_{PID_INF}_{PID_SUP}_PID"
DATA_EXEMPLES = f"{file.parents[1]}/MNHN_RESULT/4_EXAMPLE_TEST/{L}_{PID_INF}_{PID_SUP}"
path_examples = f"{DATA_EXEMPLES}/{NAME_FILE_EXAMPLES}.csv"

ALPHABET = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I",
            "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]

path_freq_aa =  f"{file.parents[1]}/MNHN_RESULT/3_TABLE_2D/6_40_50/freq_1d.npy"

param = "local_pid"






# PROGRAM
freq_aa = np.load(path_freq_aa, allow_pickle="TRUE").item()

list_score_brier_id = []
list_score_brier_stationary = []


pid_test = [round(value, 3) for value in np.arange(0.4, 0.51, 0.01)]

dico_brier_score_mixt_pid = {}
for pid in pid_test:
    dico_brier_score_mixt_pid[pid] = []


if param == "sensibility_pid":

    with open(path_examples, newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        


        for row in reader:
            # pid = float(row['pid'])/100              # approximation of a proba not to change from the PID

            aa_origin = row['aa_origin']
            aa_destination = row['aa_destination']
            
            # print(aa_origin, aa_destination)
            # print(f"pid: {pid}")

            # score = score_brier_id(aa_origin, aa_destination, ALPHABET)
            # list_score_brier_id.append(score)


            # score = score_brier_stationnary(freq_aa, aa_destination, ALPHABET)
            # list_score_brier_stationary.append(score)

            for pid in pid_test:
                # print(pid)
                score = score_brier_mixte(pid, aa_origin,freq_aa, aa_destination, ALPHABET)
                # print(score)
                dico_brier_score_mixt_pid[pid].append(score)
                # print(list_score_brier_mixte)

        # print(dico_brier_score_mixt_pid)
        for pid in pid_test:
            print(f"mean Brier Score mixte with pid = {pid}: {round(np.mean(dico_brier_score_mixt_pid[pid]), 5)}")


if param == "local_pid":

    list_brier_score_mixt_pid = []

    with open(path_examples, newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        


        for row in reader:

            aa_origin = row['aa_origin']
            aa_destination = row['aa_destination']

            # print(aa_origin, aa_destination)

            local_pid = pid_local(row, L)
            # print(local_pid)
            

            # score = score_brier_id(aa_origin, aa_destination, ALPHABET)
            # list_score_brier_id.append(score)


            # score = score_brier_stationnary(freq_aa, aa_destination, ALPHABET)
            # list_score_brier_stationary.append(score)


            score = score_brier_mixte(local_pid, aa_origin,freq_aa, aa_destination, ALPHABET)
            # print(score)
            list_brier_score_mixt_pid.append(score)
            # print(list_score_brier_mixte)

        
        print(f"mean Brier Score mixte with local pid: {round(np.mean(list_brier_score_mixt_pid), 5)}")



# # print(list_score_brier_id)
# print(f"mean Brier Score ID: {round(np.mean(list_score_brier_id), 5)}")  # mean Brier Score ID: 0.9391264521380692
# print("")
# # print(list_score_brier_stationary)
# print(f"mean Brier Score stationary: {round(np.mean(list_score_brier_stationary), 5)}")  # mean Brier Score stationary: 0.9344833873297678
# print("")
# print(list_score_brier_mixte)
# print(f"mean Brier Score mixte: {round(np.mean(list_score_brier_mixte), 5)}")
