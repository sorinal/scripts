from pathlib import Path
import pandas as pd

dic = {}
path0 = Path.home() / 'Desktop' / 'text' / 'conc_txt'
path2save = Path.home() / 'Desktop' / 'text'
for f in Path(path0).iterdir():
    with open(f) as x:
        dic[f.stem] = x.read()
ds = pd.Series(dic)
pd.to_pickle(ds, 'series.pkl')