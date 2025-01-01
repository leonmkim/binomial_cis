#%%
import binomial_cis as bc
import numpy as np
#%%
k = 2 # number of successes
n = 5 # number of trials
alpha = 0.05 # miscoverage prob
lb = bc.binom_ci(k, n, alpha, 'lb')
print(lb)
#%%
ub = bc.binom_ci(k, n, alpha, 'ub')
print(ub)
# %%
lb,ub = bc.binom_ci(k, n, alpha, 'lb,ub')
print(lb, ub)
# %%
ub_es, lb_es, p_lb_es, num_iters_es = bc.max_expected_shortage(alpha, n)
print(ub_es, lb_es, p_lb_es, num_iters_es)
# %%
ub_ee, lb_ee, p_lb_ee, num_iters_ee = bc.max_expected_excess(alpha, n)
print(ub_ee, lb_ee, p_lb_ee, num_iters_ee)

# %%
print(lb, ub, p_lb_es, p_lb_ee)
# %%
alpha_range = [0.01, 0.025, .05, .1]
for alpha in alpha_range:
    print(bc.binom_ci(k, n, alpha, 'lb'))
    print(bc.binom_ci(k, n, alpha, 'ub'))
# %%
import wandb
api = wandb.Api()
#%%
run_filter={
"jobType": "eval", 
"state": "finished"
}
filtered_runs = api.runs("serialexperimentsleon/extrinsic_contact_downstream", filters=run_filter)
#%%