Initial(
	dna(name = 'rpoB', type = 'pro1', free = 'True', prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoB', type = 'rbs', free = 'True', prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoB', type = 'cds', free = 'True', prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoC', type = 'rbs', free = 'True', prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'rpoC', type = 'cds', free = 'True', prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'rpoC', type = 'ter1', free = 'True', prot = None, rna = None, up = 5, dw = None),
	Parameter('t0_rpoBC_operon', 1))
