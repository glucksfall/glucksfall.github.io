.. _Net-GenomeGraphs:

Genome Graphs
=============

Metabolic networks have four columns. The first declares a unique name for the
enzyme or enzymatic complex; the second declares a unique name for the reaction;
the third column lists using comma unique names for substrates; and the last row
list using comma unique names for products. To declare metabolites located at
the periplasm or extracellular compartments, the user should employ the prefix
“PER-” and “EX-”, respectively. Use *spontaneous* for non-enzymatic reactions.

Examples:

.. literalinclude:: ./networks/genomegraphs_network1.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./networks/genomegraphs_network2.tsv
   :linenos:
   :encoding: latin-1

.. note::
    **Visualization in Cytoscape.** Colors and arrows remains to the user for
    customization. The network could be complemented with a description of
    sigma factor specifity for promoter, as the following network

    .. image:: Fig_GenomeGraphs.png

Finally, execute the "*Rules from metabolic network.ipynb*" to obtain the
*Rules* to model the defined network. If using a Sigma Factor-Promoter
Interaction Network, the user could use "*Rules from SigmaFactors x Architecture*"
to obtain the *Rules* to model both network at once. The complete rule-based
model can be found in the arabinose folder (1st example) and in the sigma
folder (2nd example) from the Network Biology Lab GitHub repository `here
<https://github.com/networkbiolab/atlas/>`_.

.. note::
    **Kappa BioBrick Framework.** The *Rules* for transcription and translation
    come from the work of Stewart and Wilson-Kanamori (See more
    `here <https://www.sciencedirect.com/science/article/pii/S1571066111001289>`_).
    A "pure" genome graph uses the originally defined rules, while a genome
    graph + sigma factor specifity uses a modified *rules* to model the release
    of the sigma factor from the RNA Polymerase at the transcription
    initiation. Please note the explicit modeling of the RNA Polymerase complex in the
    second example.

    .. literalinclude:: ./model_graph_network1.py
       :language: python
       :encoding: latin-1
       :linenos:

    *OR*

    .. literalinclude:: ./model_graph_network2.py
       :language: python
       :encoding: latin-1
       :linenos:

.. note::
    **Reversibility of reactions**. Atlas writes irreversible *Rules* for each
    interaction between the RNA Polymerase and a promoter. The ``Parameter('rvs_ReactionName', 0))``
    must be set to non-zero to define a reversible reaction. The remaining *Rules*
    are irreversible without a way to define reversible reactions.

.. note::
    **Simulation**. The model can be simulated only with the instantiation of
    ``Monomers`` and ``Initials`` (`More here <https://pysb.readthedocs.io/en/stable/tutorial.html#introduction>`_).
    Run *Monomer+Initials+Observables from metabolic network.ipynb* to obtain
    automatically the necessary ``Monomers`` and ``Initials`` (including
    proteins and enzymatic complexes). For initial genes, please refer to the
    following example:

    .. literalinclude:: ./model_dna_initials.py
       :language: python
       :encoding: latin-1
       :linenos:

    **Plotting**. The model can be observed only with the instantation of
    ``Observables`` (`More here <https://pysb.readthedocs.io/en/stable/tutorial.html#simulation-and-analysis>`_).
    Run *Monomer+Initials+Observables from metabolic network.ipynb* to obtain
    automatically the all possible ``Observables`` for metabolites.
