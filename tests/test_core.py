from learning_design_process_mining.synthetic import make_design_log
from learning_design_process_mining.core import trace_variants,transition_table,rework_rate,transition_entropy

def test_process_functions():
    e=make_design_log(10,2)
    assert not trace_variants(e).empty
    assert abs(transition_table(e).groupby('stage').share_from_stage.sum().iloc[0]-1)<1e-9
    assert 0<=rework_rate(e)<=1
    assert transition_entropy(e)>=0
