# [crp, SMALL_CAMP, crp, SMALL_CAMP] interacts with BS_83_104
Rule('TranscriptionFactorMet_AssemblyRule_1',
	prot(name = 'crp', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', prot = 3) %
	prot(name = 'crp', dna = None, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', prot = 2) +
	dna(name = 'BS_83_104', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'crp', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', prot = 3) %
	prot(name = 'crp', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', prot = 2) %
	dna(name = 'BS_83_104', prot = 4, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_1', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_1', 0))

# [crp, SMALL_CAMP, crp, SMALL_CAMP] interacts with [BS_83_104, BS_araB_pro1]
Rule('TranscriptionFactorMet_AssemblyRule_2',
	prot(name = 'crp', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', prot = 3) %
	prot(name = 'crp', dna = None, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', prot = 2) +
	dna(name = 'BS_83_104', prot = None, free = 'True', up = WILD, dw = WILD) %
	dna(name = 'araB', type = 'pro1', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'crp', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', prot = 3) %
	prot(name = 'crp', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', prot = 2) %
	dna(name = 'BS_83_104', prot = 4, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araB', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_2', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_2', 0))

# araC interacts with BS_35_51
Rule('TranscriptionFactorMet_AssemblyRule_3',
	prot(name = 'araC', dna = None, met = None, up = None, dw = None) +
	dna(name = 'BS_35_51', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_35_51', prot = 1, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_3', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_3', 0))

# araC interacts with BS_56_72
Rule('TranscriptionFactorMet_AssemblyRule_4',
	prot(name = 'araC', dna = None, met = None, up = None, dw = None) +
	dna(name = 'BS_56_72', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_56_72', prot = 1, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_4', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_4', 0))

# araC interacts with BS_109_125
Rule('TranscriptionFactorMet_AssemblyRule_5',
	prot(name = 'araC', dna = None, met = None, up = None, dw = None) +
	dna(name = 'BS_109_125', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_109_125', prot = 1, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_5', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_5', 0))

# araC interacts with BS_130_146
Rule('TranscriptionFactorMet_AssemblyRule_6',
	prot(name = 'araC', dna = None, met = None, up = None, dw = None) +
	dna(name = 'BS_130_146', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_130_146', prot = 1, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_6', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_6', 0))

# araC interacts with BS_267_283
Rule('TranscriptionFactorMet_AssemblyRule_7',
	prot(name = 'araC', dna = None, met = None, up = None, dw = None) +
	dna(name = 'BS_267_283', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_267_283', prot = 1, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_7', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_7', 0))

# [araC, BS_56_72] interacts with [araC, BS_267_283, BS_araC_pro1]
Rule('TranscriptionFactorMet_AssemblyRule_8',
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_56_72', prot = 1, free = 'False', up = WILD, dw = WILD) +
	prot(name = 'araC', dna = 2, met = None, up = None, dw = None) %
	dna(name = 'BS_267_283', prot = 2, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araC', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = None, met = None, up = None, dw = 1) %
	dna(name = 'BS_56_72', prot = 2, free = 'False', up = WILD, dw = WILD) %
	prot(name = 'araC', dna = 2, met = None, up = 1, dw = None) %
	dna(name = 'BS_267_283', prot = None, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araC', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_8', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_8', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_35_51
Rule('TranscriptionFactorMet_AssemblyRule_9',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_35_51', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_35_51', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_9', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_9', 0))

# [araC, BS_56_72] interacts with SMALL_alpha_L_arabinopyranose
Rule('TranscriptionFactorMet_AssemblyRule_10',
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_56_72', prot = 1, free = 'False', up = WILD, dw = WILD) +
	met(name = 'alpha_L_arabinopyranose', prot = None) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	dna(name = 'BS_56_72', prot = 2, free = 'False', up = WILD, dw = WILD) %
	met(name = 'alpha_L_arabinopyranose', prot = 1),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_10', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_10', 0))

# [araC, BS_267_283] interacts with SMALL_alpha_L_arabinopyranose
Rule('TranscriptionFactorMet_AssemblyRule_11',
	prot(name = 'araC', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'BS_267_283', prot = 1, free = 'False', up = WILD, dw = WILD) +
	met(name = 'alpha_L_arabinopyranose', prot = None) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	dna(name = 'BS_267_283', prot = 2, free = 'False', up = WILD, dw = WILD) %
	met(name = 'alpha_L_arabinopyranose', prot = 1),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_11', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_11', 0))

# [araC, SMALL_alpha_L_arabinopyranose, BS_56_72] interacts with [araC, SMALL_alpha_L_arabinopyranose, BS_35_51, BS_araB_pro1]
Rule('TranscriptionFactorMet_AssemblyRule_12',
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_56_72', prot = 2, free = 'False', up = WILD, dw = WILD) +
	prot(name = 'araC', dna = 4, met = 3, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 3) %
	dna(name = 'BS_35_51', prot = 4, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araB', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', prot = 3) %
	dna(name = 'BS_56_72', prot = 4, free = 'False', up = WILD, dw = WILD) %
	prot(name = 'araC', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 2) %
	dna(name = 'BS_35_51', prot = None, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araB', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_12', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_12', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_158_174
Rule('TranscriptionFactorMet_AssemblyRule_13',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_158_174', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_158_174', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_13', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_13', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_137_153
Rule('TranscriptionFactorMet_AssemblyRule_14',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_137_153', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_137_153', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_14', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_14', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_83_99
Rule('TranscriptionFactorMet_AssemblyRule_15',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_83_99', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_83_99', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_15', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_15', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_62_78
Rule('TranscriptionFactorMet_AssemblyRule_16',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_62_78', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_62_78', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_16', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_16', 0))

# [araC, SMALL_alpha_L_arabinopyranose, BS_83_99] interacts with [araC, SMALL_alpha_L_arabinopyranose, BS_62_78, BS_araF_pro1]
Rule('TranscriptionFactorMet_AssemblyRule_17',
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_83_99', prot = 2, free = 'False', up = WILD, dw = WILD) +
	prot(name = 'araC', dna = 4, met = 3, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 3) %
	dna(name = 'BS_62_78', prot = 4, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araF', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', prot = 3) %
	dna(name = 'BS_83_99', prot = 4, free = 'False', up = WILD, dw = WILD) %
	prot(name = 'araC', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 2) %
	dna(name = 'BS_62_78', prot = None, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araF', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_17', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_17', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_57_73
Rule('TranscriptionFactorMet_AssemblyRule_18',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_57_73', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_57_73', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_18', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_18', 0))

# [araC, SMALL_alpha_L_arabinopyranose] interacts with BS_36_52
Rule('TranscriptionFactorMet_AssemblyRule_19',
	prot(name = 'araC', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) +
	dna(name = 'BS_36_52', prot = None, free = 'True', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_36_52', prot = 2, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_19', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_19', 0))

# [araC, SMALL_alpha_L_arabinopyranose, BS_57_73] interacts with [araC, SMALL_alpha_L_arabinopyranose, BS_36_52, BS_araE_pro1]
Rule('TranscriptionFactorMet_AssemblyRule_20',
	prot(name = 'araC', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 1) %
	dna(name = 'BS_57_73', prot = 2, free = 'False', up = WILD, dw = WILD) +
	prot(name = 'araC', dna = 4, met = 3, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 3) %
	dna(name = 'BS_36_52', prot = 4, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araE', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD) |
	prot(name = 'araC', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', prot = 3) %
	dna(name = 'BS_57_73', prot = 4, free = 'False', up = WILD, dw = WILD) %
	prot(name = 'araC', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', prot = 2) %
	dna(name = 'BS_36_52', prot = None, free = 'False', up = WILD, dw = WILD) %
	dna(name = 'araE', type = 'pro1', prot = None, free = 'False', up = WILD, dw = WILD),
	Parameter('fwd_TranscriptionFactorMet_AssemblyRule_20', 0),
	Parameter('rvs_TranscriptionFactorMet_AssemblyRule_20', 0))
