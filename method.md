# Method ~ 10h20min

## Preprocessing ~ 2h15min


### Step 1: Data-Preprocessing on Pfam ~ 1h
1. General folder processing + Visualisation ~ 3min
2. PID computing ~ 46min
3. Clustering > 99% + Visualisation + non-info seed count ~ 13min
4. Data split (90% train/10% test) ~ 2s


### Step 2: Example-Preprocessing ~ 11min / 1h14min
> up to 6 successive contextual amino-acids in each direction,
and with pid between 40 and 50%

#### Pfam_TRAIN (90%) ~ 1h14min
1. Selection of valid example positions ~ 5min
2. Store the valid examples ~ 1h5min
3. Store the fraction of examples per seed ~ 4min

#### Pfam_TEST (10%) ~ 11min
1. Selection of valid example positions ~ 6s
2. Store the valid examples ~ 10min
3. Store the fraction of examples per seed ~ 26s






## Training Phase ~ 5h 
> 5h compressible to 3h because Step 3.1 and 3.2 can be run in parallel

### Step 3.1: Table 2D computing ~ 2h

> 8 pseudo-counters computed: 0, 0.001, 0.01, 0.1, 1, 10, 100, 1000

1. 2D counts: ~ 1h54min
2. 2D version frequencies, probabilities with pseudo-counters and scores ~ 0.03 s
3. Visualisation 2D tables ~ 13s

### Step 3.2: Table 3D count ~ 3h

1. 3D counts: ~ 2h54min

### Step 3.3: Table 3D versions ~ 0s
> 14 pseudo-counters computed: 0, 0.001, 0.01, 0.1, 1, 10, 100, 1000,
> 0.2, 0.4, 0.8, 1.6, 3.2, 6.4
1. 3D frequencies ~ 0s
2. 3D probabilities with pseudo-counters ~ 0



## Pre-testing Phase ~ 2h40min 
### Step 4: Example selection ~ 13min

> 1 million examples selected repetition allowed

#### Example TRAIN
1. Store random examples ~ 11min

#### Example TEST
1. Store random examples ~ 2min


### Step 5: Pseudo-counter selection ~ 2h30min

> Brier with naive Bayes with each pseudo-counter tested

#### Evaluation with Example TRAIN ~ 1h40min
> 8 pseudo-counters computed: 0, 0.001, 0.01, 0.1, 1, 10, 100, 1000
1. Selection of pseudo-counter 2D + Visualisation ~ 2min
2. Selection of pseudo-counter 3D with one contextual amino acid (UNI) ~ 42min
3. Selection of pseudo-counter 3D with multiple contextual amino acids (MULTI) ~ 56min

#### Evaluation with Example TEST ~ 2h28min
> 8 pseudo-counters computed: 0, 0.001, 0.01, 0.1, 1, 10, 100, 1000
1. Selection of pseudo-counter 2D + Visualisation ~ 1min
2. Selection of pseudo-counter 3D with one contextual amino acid (UNI) ~ 42min

> 14 pseudo-counters computed: 0, 0.001, 0.01, 0.1, 1, 10, 100, 1000,
> 0.2, 0.4, 0.8, 1.6, 3.2, 6.4
3. Selection of pseudo-counter 3D with multiple contextual amino acids (MULTI) ~ 1h45min



## Testing Phase ~ 25min

### Step 6: Brier with naive Bayes

> pseudo-counters 2D and 3D fixed according to the results of step 5 and 1M exemple test

1. Brier Score test computing with one contextual amino acid (UNI) ~ 5min
2. Brier Score computing with multiple contextual amino acids (MULTI) ~ 7min
3. Brier Score computing with all saved contextual amino acids (FULL) ~ 13min


