.. _Net-TFsDNABindingSites:

Transcription Factor-DNA Binding Site Interaction Networks
==========================================================

The transcription factor-DNA binding site network represents the physical
interaction bewteen proteins and DNA. The network have two columns and for the
former network, the first column lists using comma all components of a TF
enclosed in brackets (optionally with small compounds) and in the second column
declares the DNA binding site. Users should use the prefix “SMALL-” for small
compounds and the prefix “BS-” to encode DNA binding sites using unique names.
The second type of GRN shows in the first column the RNA polymerase holoenzyme
complex (components in brackets) and in the second the promoter. Users should
name promoters with the gene name followed by the suffix “-pro#” where # is an
integer.

Examples:

.. code-block:: bash

	SOURCE	TARGET
	# araBAD and araC
	[crp, SMALL-CAMP, crp, SMALL-CAMP]	BS-83-104
	[crp, SMALL-CAMP, crp, SMALL-CAMP]	[BS-83-104, BS-araB-pro1]

	araC	BS-35-51
	araC	BS-56-72
	araC	BS-109-125
	araC	BS-130-146
	araC	BS-267-283

	[araC, BS-56-72]	[araC, BS-267-283, BS-araC-pro1]

	[araC, SMALL-alpha-L-arabinopyranose]	BS-35-51
	[araC, BS-56-72]	SMALL-alpha-L-arabinopyranose
	[araC, BS-267-283]	SMALL-alpha-L-arabinopyranose

	[araC, SMALL-alpha-L-arabinopyranose, BS-56-72]	[araC, SMALL-alpha-L-arabinopyranose, BS-35-51, BS-araB-pro1]

	# araFGH
	[araC, SMALL-alpha-L-arabinopyranose]	BS-158-174
	[araC, SMALL-alpha-L-arabinopyranose]	BS-137-153
	[araC, SMALL-alpha-L-arabinopyranose]	BS-83-99
	[araC, SMALL-alpha-L-arabinopyranose]	BS-62-78

	[araC, SMALL-alpha-L-arabinopyranose, BS-83-99]	[araC, SMALL-alpha-L-arabinopyranose, BS-62-78, BS-araF-pro1]

	# araE
	[araC, SMALL-alpha-L-arabinopyranose]	BS-57-73
	[araC, SMALL-alpha-L-arabinopyranose]	BS-36-52

	[araC, SMALL-alpha-L-arabinopyranose, BS-57-73]	[araC, SMALL-alpha-L-arabinopyranose, BS-36-52, BS-araE-pro1]

Finally, execute the "*Rules from tf-tfbs.ipynb*" to obtain the
*Rules* to model the defined interaction network. The complete rule-based
model can be found in the arabinose folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/arabinose/Model%20arabinose%20operon%20Met%20%2B%20PPI%20%2B%20TXTL%20%2B%20GRN.ipynb>`_.

.. code:: python3

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
