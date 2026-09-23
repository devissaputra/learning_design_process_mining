import numpy as np, pandas as pd

def make_design_log(n_cases=80,seed=29):
    rng=np.random.default_rng(seed); rows=[]; base=['goals','assessment','activity','content','review','release']
    for c in range(n_cases):
        seq=base.copy()
        if rng.random()<.55: seq.insert(4,'activity')
        if rng.random()<.35: seq.insert(-1,'assessment')
        minute=0
        for i,stage in enumerate(seq):
            minute+=int(rng.integers(8,55)); rows.append({'case_id':f'D{c:03d}','event_index':i,'timestamp':pd.Timestamp('2026-01-01')+pd.Timedelta(minutes=minute+c*500),'stage':stage,'actor':rng.choice(['designer','designer','ai_assistant'])})
    return pd.DataFrame(rows)
