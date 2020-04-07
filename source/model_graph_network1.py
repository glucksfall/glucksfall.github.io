Rule('docking_araB_pro1',
	cplx(name = 'RNAP', dna = None) + dna(name = 'araB', type = 'pro1', prot = None, free = 'True') |
	cplx(name = 'RNAP', dna = 1) % dna(name = 'araB', type = 'pro1', prot = 1, free = 'False'),
	Parameter('fwd_docking_araB_pro1', 1), Parameter('rvs_docking_araB_pro1', 1))
