.. _Plotting-page:

Plotting
========

PySB could inform the results of a simulation to dataframes (See
:ref:`Simulation-page`) and visualization of results could be done with
matplotlib or seaborn even (`See more here <https://seaborn.pydata.org/>`_). To
access the data, the dataframes columns reproduce the names of the ``Observables``.
The following example could be adapted to show the dynamics of any ``Observable``.

.. note::
    Importantly, PySB allows the inspection of the model to find which
    ``Monomers`` (and complexes of monomers) exists in the model, but as the
    simulation is network-free, the possible formed complexes are up to the user
    concern.

.. note::
    Atlas produces automatically ``Observables`` for metabolites, and other
    components and complexes could also be observed and plotted, but their
    declaration in the model is entirely up to the user.

.. literalinclude:: ./plotting.py
       :language: python
       :encoding: latin-1
       :linenos:

And the results is

.. image:: Fig_Arabinose.png

.. note::
    See the `Arabinose Model <https://github.com/glucksfall/atlas/blob/master/arabinose/Model%20arabinose%20operon%20Met%20%2B%20PPI%20%2B%20TXTL%20%2B%20GRN.ipynb>`_
    to inspect the rules and reproduce (at some extent because of stochasticity) the plot showed in this Manual.
