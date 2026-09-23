from pathlib import Path
import json
from learning_design_process_mining.synthetic import make_design_log
from learning_design_process_mining.core import trace_variants,transition_table,rework_rate,transition_entropy
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
e=make_design_log(); v=trace_variants(e); t=transition_table(e); e.to_csv(root/'results'/'synthetic_design_log.csv',index=False); v.to_csv(root/'results'/'trace_variants.csv',index=False); t.to_csv(root/'results'/'transitions.csv',index=False)
metrics={'variant_count':int(len(v)),'transition_entropy':round(transition_entropy(e),3),'rework_rate':round(rework_rate(e),3),'ai_handoff_rate':round(float((e.actor=='ai_assistant').mean()),3)}; (root/'results'/'demo_metrics.json').write_text(json.dumps(metrics,indent=2)); print(json.dumps(metrics,indent=2))
