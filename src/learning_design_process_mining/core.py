# Calculation reading guide: ../CALCULATIONS.md (repository root).
# P(next|stage) = transition count / outgoing count; H(stage) = -sum p log2 p.
# Entropy is averaged equally across source stages. Rework is repeated-stage events divided by events within a case, then averaged over cases. Repetition may be productive revision rather than waste.

from __future__ import annotations
from collections import Counter
import math, pandas as pd

def trace_variants(events:pd.DataFrame)->pd.DataFrame:
    ordered=events.sort_values(['case_id','timestamp'])
    traces=ordered.groupby('case_id').stage.apply(lambda s:' > '.join(s)).reset_index(name='trace')
    counts=traces.trace.value_counts().rename_axis('trace').reset_index(name='cases'); return counts

def transition_table(events:pd.DataFrame)->pd.DataFrame:
    ordered=events.sort_values(['case_id','timestamp']).copy(); ordered['next_stage']=ordered.groupby('case_id').stage.shift(-1)
    t=ordered.dropna(subset=['next_stage']).groupby(['stage','next_stage']).size().reset_index(name='count'); t['share_from_stage']=t['count']/t.groupby('stage')['count'].transform('sum'); return t

def transition_entropy(events:pd.DataFrame)->float:
    t=transition_table(events); vals=[]
    for _,g in t.groupby('stage'):
        p=g.share_from_stage.to_numpy()
        vals.append(-float(sum(x * math.log2(x) for x in p if x > 0)))
    return float(sum(vals)/len(vals)) if vals else 0.0

def rework_rate(events:pd.DataFrame)->float:
    ordered=events.sort_values(['case_id','timestamp']); rates=[]
    for _,g in ordered.groupby('case_id'):
        stages=list(g.stage); rates.append(max(0,len(stages)-len(set(stages)))/max(1,len(stages)))
    return float(sum(rates)/len(rates))
