"""got my answers in a notebook so this may or may not run.. it's the weekend baby!"""

import numpy as np
from collections import Counter, deque

def preprocess(inp):
    data = inp.split("\n\n")
    return deque([int(_) for _ in data[0].split(",")]), [all_diags(cleanup_row(_)) for _ in data[1:]]

def cleanup_row(row):
    data = row.split("\n")
    return np.matrix([[int(_.strip()) for _ in x.split(" ") if _] for x in data if x])

def all_diags(m):
    horiz = [Counter(_[0].tolist()[0]) for _ in m]
    vert = [Counter(_[0].tolist()[0]) for _ in m.T]
    
    diag = Counter(np.diag(m))
    diag_T = Counter(np.diag(m.T))
    
    return horiz + vert + [diag] + [diag_T]

def run(h, boards):
    tally = Counter()
    while True:
        next_number = h.popleft()
        tally[next_number] += 1
        for player in boards:
            for possible_row in player:
                if len(possible_row - tally) == 0:
                    print("BINGO")
                    return player[:5], tally, next_number

def run_two(h, boards):
    tally = Counter()
    bingod = set()
    
    while True:
        next_number = h.popleft()
        tally[next_number] += 1
        for player_id, player in enumerate(boards):
            if player_id in bingod:
                continue
            for possible_row in player:
                if len(possible_row - tally) == 0:
                    print("BINGO")
                    bingod.add(player_id)
                    if len(bingod) == len(boards):
                        return player[:5], tally, next_number               

                
                
def counter_total(counter):
    return sum([k*v for k, v in counter.items()])
               
    
with open("input", "r") as r:
    h, t = preprocess(r.read())   
#h, t = preprocess(inp)
a, b, c = run_two(h, t)
