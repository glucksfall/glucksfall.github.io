# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoA_pro1
Rule('docking_1_rpoA_pro1',
	prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'rpoA', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'rpoA', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_docking_1_rpoA_rbs', 1),
	Parameter('rvs_docking_1_rpoA_pro1', 0))
