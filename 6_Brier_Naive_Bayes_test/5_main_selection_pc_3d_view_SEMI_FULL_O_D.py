"""
VIEW: BRIER TEST - SEMI_FULL -Origin and Destination
"""

# IMPORTS

import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


file = Path(__file__).resolve()
sys.path.append(file.parents[0])


# PARAMETERS
# EXPERIMENT_NAME = "EXP_1M_UNI"
DATA_ORIGIN = f"{file.parents[2]}/MNHN_RESULT/6_TEST_BRIER_NAIVE_BAYES/EXP_1M_SEMI_FULL"
DATA_DESTINATION = f"{file.parents[2]}/MNHN_RESULT/6_TEST_BRIER_NAIVE_BAYES/EXP_1M_SEMI_FULL_D"


L = 6

LIST_PSEUDO_COUNTER_3D = [pow(10, 0)]

# PROGRAM

# LOAD RESULT
dict_3D_ORIGIN = np.load(f"{DATA_ORIGIN}/SCORE_SEMI_FULL_O.npy", allow_pickle='True').item()
dict_3D_DESTINATION = np.load(f"{DATA_DESTINATION}/SCORE_SEMI_FULL_D.npy", allow_pickle='True').item()

# GET X, Y

plt.figure(figsize=(9, 8), dpi=400)

list_position_origin = []
for pseudo_counter_3D in LIST_PSEUDO_COUNTER_3D:
    list_position = []
    list_score_origin = []
    list_score_destination = []

    for position in range(0, L+1):
        list_position.append(position)
        list_score_origin.append(np.mean(dict_3D_ORIGIN[position][pseudo_counter_3D]))
        list_score_destination.append(np.mean(dict_3D_DESTINATION[position][pseudo_counter_3D]))
          
            
    plt.plot(list_position, list_score_origin, label="ORIGINE")
    plt.plot(list_position, list_score_destination, label="DESTINATION", linestyle='dashed')

plt.legend(fontsize=17)
plt.xlabel("POSITION RELATIVE", fontsize=17)
plt.xticks(range(0, L + 1), fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('SCORE DE BRIER', fontsize=17)
plt.grid(color='lightgrey', linestyle='--', linewidth=1)
title_fig = f"Calcul du score de Brier sur 1 million d'exemples test\navec la méthode SEMI-FULL"
plt.title(title_fig , loc='center', fontsize=20)
title_fig = f"PC_3D_FULL_1M_ORIGIN_DESTINATION"
plt.savefig(f"{DATA_DESTINATION}/{title_fig}.png")
