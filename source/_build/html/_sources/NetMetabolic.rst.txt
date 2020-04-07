.. _Net-Metabolic:

Metabolic Networks
==================

Metabolic networks have four columns. The first declares a unique name for the
enzyme or enzymatic complex; the second declares a unique name for the reaction;
the third column lists using comma unique names for substrates; and the last row
list using comma unique names for products. To declare metabolites located at
the periplasm or extracellular compartments, the user should employ the prefix
“PER-” and “EX-”, respectively. Use *spontaneous* for non-enzymatic reactions.

Examples:

.. literalinclude:: ./metabolic_network1.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./metabolic_network2.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./metabolic_network3.tsv
   :linenos:
   :encoding: latin-1

.. note::
    **Visualization in Cytoscape.** Transform the four-columns file into a
    two-columns file with the helper script "*Expand metabolic network.ipynb*", paste
    the results in a new file, and import the network into Cytoscape. Colors and
    arrows remains to the user for customization.

    .. image:: Fig_Lactose_MetNetwork.png

Finally, execute the "*Rules from metabolic network.ipynb*" to obtain the
*Rules* to model the defined metabolic network. The complete rule-based
model can be found in the lactose folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/lactose/Models/Model3%20MetNet%20fully%20automatized.ipynb/>`_.

.. literalinclude:: ./metabolic_model.py
   :language: python
   :encoding: latin-1
   :linenos:

.. note::
    **Reversibility of Rules**. Atlas writes reversible *Rules* for each
    reaction declared in the network file. The ``Parameter('rvs_RuleName', 1))``
    must be set to zero to define an irreversible reaction.

.. note::
    **Uniqueness of Rule names**. Atlas will write *Rules* for unique
    metabolic reactions. Identical names will be reported for further curation.

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
