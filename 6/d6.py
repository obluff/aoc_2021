from collections import Counter

def prepro_input(inp):
    return [int(_) for _ in inp.split(",") if _]

def shift(inp):
    new = inp[1:]
    new[6] += inp[0]
    new += [inp[0]]
    return new 

def create_count_array(inp):
    count_arr = [0 for i in range(9)]
    for i, j in Counter(inp).items():
        count_arr[i] += j
    return count_arr

def run(days, count_arr):
    for i in range(days):
        count_arr = shift(count_arr)   
    return sum(count_arr)

with open("input", "r") as w:
    inp = create_count_array(prepro_input(w.read()))

print(run(80, inp))       
print(run(256, inp))    
