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

.. literalinclude:: ./networks/tfbs_network1.tsv
   :linenos:
   :encoding: latin-1

Finally, execute the "*Rules from tf-tfbs.ipynb*" to obtain the
*Rules* to model the defined interaction network. The complete rule-based
model can be found in the arabinose folder from the Network Biology Lab
GitHub repository `here <https://github.com/networkbiolab/atlas/blob/master/arabinose/Model%20arabinose%20operon%20Met%20%2B%20PPI%20%2B%20TXTL%20%2B%20GRN.ipynb>`_.

.. literalinclude:: ./model_tfbs_network1.py
   :language: python
   :encoding: latin-1
   :linenos:

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
