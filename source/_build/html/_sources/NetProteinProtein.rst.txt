.. _Net-ProteinProtein:

Protein-Protein Interaction Networks
====================================

Protein-protein interaction (PPI) interaction networks have two columns. In any
order and for any number of components, each column lists using comma the
interacting proteins or protein complexes. The user should employ brackets to
enclose a list of proteins that are part of a complex.

Examples:

.. literalinclude:: ./networks/ppi_network1.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./networks/ppi_network2.tsv
   :linenos:
   :encoding: latin-1

.. note::
    **Visualization in Cytoscape.** Cytoscape cannot import hyper-graphs. To do so,
    Create simple network and right-click to embed a subnetwork in the corresponding node.

    .. image:: Fig_Lactose_PPINetwork.png

Finally, execute the "*Rules from protein-protein.ipynb*" to obtain the
*Rules* to model the defined interaction network. The complete rule-based
model can be found in the lactose folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/lactose/Models/Model4%20PPI%20from%20automatic%20Rules.ipynb>`_.

.. literalinclude:: ./model_ppi_network1.py
   :language: python
   :encoding: latin-1
   :linenos:

.. note::
    **Reversibility of Rules**. Atlas writes irreversible *Rules* for each
    reaction declared in the network file. The ``Parameter('rvs_RuleName', 0))``
    must be set to non-zero to define an reversible reaction.

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
