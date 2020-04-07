.. _Net-Protein-SmallCompounds:

Protein-Small compounds Interaction Networks
============================================

Protein-small compound interaction networks have two columns. Similar to a PPI
network, but the user should add the prefix “SMALL-” to encode a small compound
that interacts with the protein or protein complex.

Examples:

.. code-block:: bash

	SOURCE	TARGET
	PER-araF	SMALL-PER-alpha-L-arabinofuranose
	PER-araF	SMALL-PER-beta-L-arabinofuranose
	PER-araF	SMALL-PER-alpha-L-arabinopyranose
	PER-araF	SMALL-PER-beta-L-arabinopyranose
	[crp, crp]	SMALL-CAMP
	[crp, SMALL-CAMP, crp]	SMALL-CAMP
	[lacI, lacI]	SMALL-ALLOLACTOSE
	[lacI, SMALL-ALLOLACTOSE, lacI]	SMALL-ALLOLACTOSE
	[araG, araG]	SMALL-ATP
	araC	SMALL-alpha-L-arabinopyranose
	[araC, araC]	SMALL-alpha-L-arabinopyranose
	[araC, SMALL-alpha-L-arabinopyranose, araC]	SMALL-alpha-L-arabinopyranose

Finally, execute the "*Rules from protein-small compounds.ipynb*" to obtain the
*Rules* to model the defined interaction network. The complete rule-based
model can be found in the arabinose folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/arabinose/Model%20arabinose%20operon%20Met%20%2B%20PPI%20%2B%20TXTL%20%2B%20GRN.ipynb>`_.

.. code:: python3

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

.. note::
	**Reversibility of Rules**. Atlas writes reversible *Rules* for each
	reaction declared in the network file. The ``Parameter('rvs_RuleName', 1))``
	must be set to zero to define an irreversible reaction.

.. note::
	**Uniqueness of Rule names**. Atlas will write *Rules* with numbered
	names. Use only one file to model the many interactions the system has.

.. note::
	**Simulation**. The model can be simulated only with the instantiation of
	``Monomers`` and ``Initials`` (`More here <https://pysb.readthedocs.io/en/stable/tutorial.html#introduction>`_).
	Run *Monomer+Initials+Observables from metabolic network.ipynb* to obtain
	automatically the necessary ``Monomers`` and ``Initials`` (including
	proteins and enzymatic complexes). Manually add the necessary ``Monomers``
	and ``Initials`` for non-enzymatic proteins.

	**Plotting**. The model can be observed only with the instantation of
	``Observables`` (`More here <https://pysb.readthedocs.io/en/stable/tutorial.html#simulation-and-analysis>`_).
	Run *Monomer+Initials+Observables from metabolic network.ipynb* to obtain
	automatically the all possible ``Observables`` for enzymatic proteins. Other
	observables for proteins should be added manually.
