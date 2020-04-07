.. _Net-SFsPromoters:

Sigma Factor-Promoter Interaction Networks
==========================================

The Sigma Factor-Promoter network have two columns and for the former network, the first column lists using comma all components of a TF enclosed in brackets (optionally with small compounds) and in the second column declares the DNA binding site. Users should use the prefix “SMALL-” for small compounds and the prefix “BS-” to encode DNA binding sites using unique names. The second type of GRN shows in the first column the RNA polymerase holoenzyme complex (components in brackets) and in the second the promoter. Users should name promoters with the gene name followed by the suffix “-pro#” where # is an integer.

Examples:

.. code-block:: bash

	SOURCE	TARGET
	# Docking to promoters
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoA-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoB-pro1
	# [rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoC-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoD-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoE-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoH-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoN-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-rpoS-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-fliA-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoD]	BS-fecI-pro1

	[rpoA, rpoA, rpoB, rpoC, rpoE]	BS-rpoD-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoE]	BS-rpoE-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoE]	BS-rpoH-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoE]	BS-rpoN-pro1

	[rpoA, rpoA, rpoB, rpoC, rpoH]	BS-rpoA-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoH]	BS-rpoD-pro1

	[rpoA, rpoA, rpoB, rpoC, rpoN]	BS-rpoA-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoN]	BS-rpoD-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoN]	BS-rpoH-pro1

	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-fecI-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoA-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoB-pro1
	# [rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoC-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoD-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoE-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoH-pro1
	[rpoA, rpoA, rpoB, rpoC, rpoS]	BS-rpoN-pro1

	[rpoA, rpoA, rpoB, rpoC, fliA]	BS-rpoD-pro1
	[rpoA, rpoA, rpoB, rpoC, fliA]	BS-rpoN-pro1
	[rpoA, rpoA, rpoB, rpoC, fliA]	BS-fliA-pro1

Finally, execute the "*Rules from SigmaFactors x Architecture.ipynb*" to obtain the
*Rules* to model the defined interaction network. The complete rule-based
model can be found in the sigma folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/sigma/Model%20sigma.ipynb/>`_.

.. code:: python3

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
		Parameter('fwd_docking_1_rpoA_pro1', 0),
		Parameter('rvs_docking_1_rpoA_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoB_pro1
	Rule('docking_2_rpoB_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoB', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoB', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_2_rpoB_pro1', 0),
		Parameter('rvs_docking_2_rpoB_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoD_pro1
	Rule('docking_3_rpoD_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoD', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoD', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_3_rpoD_pro1', 0),
		Parameter('rvs_docking_3_rpoD_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoE_pro1
	Rule('docking_4_rpoE_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoE', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoE', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_4_rpoE_pro1', 0),
		Parameter('rvs_docking_4_rpoE_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoH_pro1
	Rule('docking_5_rpoH_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoH', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoH', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_5_rpoH_pro1', 0),
		Parameter('rvs_docking_5_rpoH_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoN_pro1
	Rule('docking_6_rpoN_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoN', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoN', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_6_rpoN_pro1', 0),
		Parameter('rvs_docking_6_rpoN_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_rpoS_pro1
	Rule('docking_7_rpoS_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoS', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoS', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_7_rpoS_pro1', 0),
		Parameter('rvs_docking_7_rpoS_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_fliA_pro1
	Rule('docking_8_fliA_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'fliA', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'fliA', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_8_fliA_pro1', 0),
		Parameter('rvs_docking_8_fliA_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoD] interacts with BS_fecI_pro1
	Rule('docking_9_fecI_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'fecI', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoD', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'fecI', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_9_fecI_pro1', 0),
		Parameter('rvs_docking_9_fecI_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoE] interacts with BS_rpoD_pro1
	Rule('docking_10_rpoD_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoD', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoD', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_10_rpoD_pro1', 0),
		Parameter('rvs_docking_10_rpoD_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoE] interacts with BS_rpoE_pro1
	Rule('docking_11_rpoE_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoE', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoE', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_11_rpoE_pro1', 0),
		Parameter('rvs_docking_11_rpoE_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoE] interacts with BS_rpoH_pro1
	Rule('docking_12_rpoH_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoH', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoH', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_12_rpoH_pro1', 0),
		Parameter('rvs_docking_12_rpoH_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoE] interacts with BS_rpoN_pro1
	Rule('docking_13_rpoN_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoN', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoE', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoN', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_13_rpoN_pro1', 0),
		Parameter('rvs_docking_13_rpoN_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoH] interacts with BS_rpoA_pro1
	Rule('docking_14_rpoA_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoH', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoA', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoH', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoA', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_14_rpoA_pro1', 0),
		Parameter('rvs_docking_14_rpoA_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoH] interacts with BS_rpoD_pro1
	Rule('docking_15_rpoD_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoH', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoD', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoH', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoD', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_15_rpoD_pro1', 0),
		Parameter('rvs_docking_15_rpoD_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoN] interacts with BS_rpoA_pro1
	Rule('docking_16_rpoA_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoN', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoA', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoN', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoA', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_16_rpoA_pro1', 0),
		Parameter('rvs_docking_16_rpoA_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoN] interacts with BS_rpoD_pro1
	Rule('docking_17_rpoD_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoN', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoD', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoN', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoD', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_17_rpoD_pro1', 0),
		Parameter('rvs_docking_17_rpoD_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoN] interacts with BS_rpoH_pro1
	Rule('docking_18_rpoH_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoN', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoH', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoN', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoH', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_18_rpoH_pro1', 0),
		Parameter('rvs_docking_18_rpoH_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_fecI_pro1
	Rule('docking_19_fecI_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'fecI', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'fecI', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_19_fecI_pro1', 0),
		Parameter('rvs_docking_19_fecI_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_rpoA_pro1
	Rule('docking_20_rpoA_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoA', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoA', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_20_rpoA_pro1', 0),
		Parameter('rvs_docking_20_rpoA_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_rpoB_pro1
	Rule('docking_21_rpoB_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoB', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoB', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_21_rpoB_pro1', 0),
		Parameter('rvs_docking_21_rpoB_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_rpoD_pro1
	Rule('docking_22_rpoD_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoD', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoD', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_22_rpoD_pro1', 0),
		Parameter('rvs_docking_22_rpoD_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_rpoE_pro1
	Rule('docking_23_rpoE_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoE', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoE', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_23_rpoE_pro1', 0),
		Parameter('rvs_docking_23_rpoE_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_rpoH_pro1
	Rule('docking_24_rpoH_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoH', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoH', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_24_rpoH_pro1', 0),
		Parameter('rvs_docking_24_rpoH_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, rpoS] interacts with BS_rpoN_pro1
	Rule('docking_25_rpoN_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoN', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'rpoS', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoN', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_25_rpoN_pro1', 0),
		Parameter('rvs_docking_25_rpoN_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, fliA] interacts with BS_rpoD_pro1
	Rule('docking_26_rpoD_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'fliA', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoD', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'fliA', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoD', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_26_rpoD_pro1', 0),
		Parameter('rvs_docking_26_rpoD_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, fliA] interacts with BS_rpoN_pro1
	Rule('docking_27_rpoN_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'fliA', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'rpoN', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'fliA', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'rpoN', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_27_rpoN_pro1', 0),
		Parameter('rvs_docking_27_rpoN_pro1', 0))

	# [rpoA, rpoA, rpoB, rpoC, fliA] interacts with BS_fliA_pro1
	Rule('docking_28_fliA_pro1',
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'fliA', dna = None, met = None, up = 4, dw = None) +
		dna(name = 'fliA', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
		prot(name = 'rpoA', dna = None, met = None, up = None, dw = 1) %
		prot(name = 'rpoA', dna = None, met = None, up = 1, dw = 2) %
		prot(name = 'rpoB', dna = None, met = None, up = 2, dw = 3) %
		prot(name = 'rpoC', dna = None, met = None, up = 3, dw = 4) %
		prot(name = 'fliA', dna = 5, met = None, up = 4, dw = None) %
		dna(name = 'fliA', type = 'pro1', prot = 5, free = 'False', up = WILD, dw = WILD),
		Parameter('fwd_docking_28_fliA_pro1', 0),
		Parameter('rvs_docking_28_fliA_pro1', 0))

.. note::
	**Reversibility of reactions**. Atlas writes dead *Rules* for each
	reaction declared in the network file. The ``Parameter('fwd_ReactionName', 0))``
	must be set to non-zero to activate the rule and ``Parameter('rvs_ReactionName', 0))``
	must be set to non-zero to define a reversible reaction.

.. note::
	**Simulation**. The model can be simulated only with the instantiation of
	``Monomers`` and ``Initials`` (`More here <https://pysb.readthedocs.io/en/stable/tutorial.html#introduction>`_).
	Run *Monomer+Initials+Observables from metabolic network.ipynb* to obtain
	automatically the necessary ``Monomers`` and ``Initials`` (including
	proteins and enzymatic complexes).

	**Plotting**. The model can be observed only with the instantation of
	``Observables`` (`More here <https://pysb.readthedocs.io/en/stable/tutorial.html#simulation-and-analysis>`_).
	Run *Monomer+Initials+Observables from metabolic network.ipynb* to obtain
	automatically the all possible ``Observables`` for metabolites.
