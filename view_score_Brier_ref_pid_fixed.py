
# IMPORTS 
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

file = Path(__file__).resolve()
sys.path.append(file.parents[0])


# PARAMETERS
DATA = f"{file.parents[1]}/FIG_RAPPORT_STAGE"

# PROGRAM
plt.figure(figsize=(9, 8), dpi=400)

list_pid = [round(value, 4) for value in np.arange(0.4,0.51,0.01)]
print(list_pid)

# manually reported
list_score_brier = [0.72127, 0.71861, 0.71617, 0.71393, 0.71191, 0.71011, 0.70851, 0.70713, 0.70597, 0.70501, 0.70427]



plt.xlabel("POURCENTAGE D'IDENTITÉ", fontsize=17)
plt.xticks(list_pid, fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('SCORE DE BRIER', fontsize=17)
plt.grid(color='lightgrey', linestyle='--', linewidth=1)
title_fig = f"Calcul du score de Brier sur 1 million d'exemples test\navec le prédicteur MIXT et en faisant varier le pid"
plt.title(title_fig , loc='center', fontsize=20)
plt.plot(list_pid, list_score_brier, marker='o')
plt.savefig(f"{DATA}/ref_score_brier_mxit_pid_fixed.png")
