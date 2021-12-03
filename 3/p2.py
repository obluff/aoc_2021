import pandas as pd


def get_mode(ser, neg):
    mode = ser.mode()
    m = int(mode) if len(mode) == 1 else 1
    return not m if neg else m


def run(df, neg=False, col=0):
    if len(df) == 1:
        return int("".join(df.astype(str).iloc[0]), 2)
    return df.loc[lambda x: x[col] == get_mode(x[col], neg)].pipe(run, neg, col + 1)


with open("input.txt", "r") as r:
    df = pd.DataFrame(data=[[int(x) for x in _] for _ in r.read().strip().split("\n")])

print(df.pipe(run) * df.pipe(run, neg=True))
