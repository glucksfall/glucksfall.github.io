Rule('complex_assembly_rule_0',
	prot(name = 'BETAGALACTOSID_MONOMER', up = None, dw = None) +
	prot(name = 'BETAGALACTOSID_MONOMER', up = None, dw = None) |
	prot(name = 'BETAGALACTOSID_MONOMER', up = 1, dw = None) %
	prot(name = 'BETAGALACTOSID_MONOMER', up = None, dw = 1),
	Parameter('fwd_complex_assembly_rule_0', 1),
	Parameter('rvs_complex_assembly_rule_0', 0))

Rule('complex_assembly_rule_1',
	prot(name = 'BETAGALACTOSID_MONOMER', up = 1, dw = None) %
	prot(name = 'BETAGALACTOSID_MONOMER', up = None, dw = 1) +
	prot(name = 'BETAGALACTOSID_MONOMER', up = 1, dw = None) %
	prot(name = 'BETAGALACTOSID_MONOMER', up = None, dw = 1) |
	prot(name = 'BETAGALACTOSID_MONOMER', up = 1, dw = None) %
	prot(name = 'BETAGALACTOSID_MONOMER', up = 2, dw = 1) %
	prot(name = 'BETAGALACTOSID_MONOMER', up = 3, dw = 2) %
	prot(name = 'BETAGALACTOSID_MONOMER', up = None, dw = 3),
	Parameter('fwd_complex_assembly_rule_1', 1),
	Parameter('rvs_complex_assembly_rule_1', 0))

Rule('complex_assembly_rule_2',
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = None, dw = None) +
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = None, dw = None) |
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = 1, dw = None) %
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = None, dw = 1),
	Parameter('fwd_complex_assembly_rule_2', 1),
	Parameter('rvs_complex_assembly_rule_2', 0))

Rule('complex_assembly_rule_3',
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = None, dw = None) +
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = 1, dw = None) %
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = None, dw = 1) |
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = 1, dw = None) %
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = 2, dw = 1) %
	prot(name = 'GALACTOACETYLTRAN_MONOMER', up = None, dw = 2),
	Parameter('fwd_complex_assembly_rule_3', 1),
	Parameter('rvs_complex_assembly_rule_3', 0))
