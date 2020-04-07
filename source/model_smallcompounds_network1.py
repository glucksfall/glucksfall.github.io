Rule('ProtMet_RuleAssembly_1',
	prot(name = 'araF', loc = 'per', met = None, up = None, dw = None) +
	met(name = 'alpha_L_arabinofuranose', loc = 'per', prot = None) |
	prot(name = 'araF', loc = 'per', met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinofuranose', loc = 'per', prot = 1),
	Parameter('fwd_ProtMet_RuleAssembly_1', 1),
	Parameter('rvs_ProtMet_RuleAssembly_1', 1))

Rule('ProtMet_RuleAssembly_2',
	prot(name = 'araF', loc = 'per', met = None, up = None, dw = None) +
	met(name = 'beta_L_arabinofuranose', loc = 'per', prot = None) |
	prot(name = 'araF', loc = 'per', met = 1, up = None, dw = None) %
	met(name = 'beta_L_arabinofuranose', loc = 'per', prot = 1),
	Parameter('fwd_ProtMet_RuleAssembly_2', 1),
	Parameter('rvs_ProtMet_RuleAssembly_2', 1))

Rule('ProtMet_RuleAssembly_3',
	prot(name = 'araF', loc = 'per', met = None, up = None, dw = None) +
	met(name = 'alpha_L_arabinopyranose', loc = 'per', prot = None) |
	prot(name = 'araF', loc = 'per', met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'per', prot = 1),
	Parameter('fwd_ProtMet_RuleAssembly_3', 1),
	Parameter('rvs_ProtMet_RuleAssembly_3', 1))

Rule('ProtMet_RuleAssembly_4',
	prot(name = 'araF', loc = 'per', met = None, up = None, dw = None) +
	met(name = 'beta_L_arabinopyranose', loc = 'per', prot = None) |
	prot(name = 'araF', loc = 'per', met = 1, up = None, dw = None) %
	met(name = 'beta_L_arabinopyranose', loc = 'per', prot = 1),
	Parameter('fwd_ProtMet_RuleAssembly_4', 1),
	Parameter('rvs_ProtMet_RuleAssembly_4', 1))

Rule('ProtMet_RuleAssembly_5',
	prot(name = 'crp', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'crp', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'CAMP', loc = 'cyt', prot = None) |
	prot(name = 'crp', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'crp', loc = 'cyt', met = 2, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', prot = 2),
	Parameter('fwd_ProtMet_RuleAssembly_5', 1),
	Parameter('rvs_ProtMet_RuleAssembly_5', 1))

Rule('ProtMet_RuleAssembly_6',
	prot(name = 'crp', loc = 'cyt', met = 2, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', prot = 2) %
	prot(name = 'crp', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'CAMP', loc = 'cyt', prot = None) |
	prot(name = 'crp', loc = 'cyt', met = 2, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', prot = 2) %
	prot(name = 'crp', loc = 'cyt', met = 3, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', prot = 3),
	Parameter('fwd_ProtMet_RuleAssembly_6', 1),
	Parameter('rvs_ProtMet_RuleAssembly_6', 1))

Rule('ProtMet_RuleAssembly_7',
	prot(name = 'lacI', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None) |
	prot(name = 'lacI', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', met = 2, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 2),
	Parameter('fwd_ProtMet_RuleAssembly_7', 1),
	Parameter('rvs_ProtMet_RuleAssembly_7', 1))

Rule('ProtMet_RuleAssembly_8',
	prot(name = 'lacI', loc = 'cyt', met = 2, up = None, dw = 1) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 2) %
	prot(name = 'lacI', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None) |
	prot(name = 'lacI', loc = 'cyt', met = 2, up = None, dw = 1) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 2) %
	prot(name = 'lacI', loc = 'cyt', met = 3, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 3),
	Parameter('fwd_ProtMet_RuleAssembly_8', 1),
	Parameter('rvs_ProtMet_RuleAssembly_8', 1))

Rule('ProtMet_RuleAssembly_9',
	prot(name = 'araG', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'araG', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'ATP', loc = 'cyt', prot = None) |
	prot(name = 'araG', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'araG', loc = 'cyt', met = 2, up = 1, dw = None) %
	met(name = 'ATP', loc = 'cyt', prot = 2),
	Parameter('fwd_ProtMet_RuleAssembly_9', 1),
	Parameter('rvs_ProtMet_RuleAssembly_9', 1))

Rule('ProtMet_RuleAssembly_10',
	prot(name = 'araC', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'araC', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) |
	prot(name = 'araC', loc = 'cyt', met = None, up = None, dw = 1) %
	prot(name = 'araC', loc = 'cyt', met = 2, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2),
	Parameter('fwd_ProtMet_RuleAssembly_10', 1),
	Parameter('rvs_ProtMet_RuleAssembly_10', 1))

Rule('ProtMet_RuleAssembly_11',
	prot(name = 'araC', loc = 'cyt', met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2) %
	prot(name = 'araC', loc = 'cyt', met = None, up = 1, dw = None) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) |
	prot(name = 'araC', loc = 'cyt', met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2) %
	prot(name = 'araC', loc = 'cyt', met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3),
	Parameter('fwd_ProtMet_RuleAssembly_11', 1),
	Parameter('rvs_ProtMet_RuleAssembly_11', 1))
