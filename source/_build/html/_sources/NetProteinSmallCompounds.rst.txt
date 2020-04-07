.. _Net-Protein-SmallCompounds:

Protein-Small compounds Interaction Networks
============================================

Protein-small compound interaction networks have two columns. Similar to a PPI
network, but the user should add the prefix “SMALL-” to encode a small compound
that interacts with the protein or protein complex.

Examples:

.. literalinclude:: ./networks/smallcompounds_network1.tsv
   :linenos:
   :encoding: latin-1

Finally, execute the "*Rules from protein-small compounds.ipynb*" to obtain the
*Rules* to model the defined interaction network. The complete rule-based
model can be found in the arabinose folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/arabinose/Model%20arabinose%20operon%20Met%20%2B%20PPI%20%2B%20TXTL%20%2B%20GRN.ipynb>`_.

.. literalinclude:: ./model_smallcompounds_network1.py
   :language: python
   :encoding: latin-1
   :linenos:

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
