import csv

import sys
from pathlib import Path



file = Path(__file__).resolve()
sys.path.append(file.parents[0])



infile = f"{file.parents[1]}/MNHN_RESULT/4_EXAMPLE_TEST_1M_PID/6_40_50_PID/EX_BRIER_TEST_1M_PID.csv"
n_ex = 10


outfile = f"{file.parents[1]}/MNHN_RESULT/4_EXAMPLE_TEST_1M_PID/6_40_50_PID/subset_PID.csv"

with open(infile, encoding='utf-8') as f, open(outfile, 'w') as o:
    reader = csv.reader(f)
    writer = csv.writer(o, delimiter=',') # adjust as necessary
    count = 0
    for row in reader:
        count += 1
        if count <= n_ex:
            writer.writerow(row)
        else:
            break

# no need for close statements
print('Done')