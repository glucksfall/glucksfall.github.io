.. _Simulation-page:

Simulation
==========

Simulation could be done within the PySB python package (See more at `PySB
documentation
<https://pysb.readthedocs.io/en/stable/tutorial.html#simulation-and-analysis>`_)
. Here is the relevant code that able the simulation of any PySB model, albeit
PySB exports the model, calls the simulator, and imports the results under the
hood. See :ref:`Plotting-page` for a simple example on how to plot simulation results.

.. literalinclude:: ./simulation.py
   :language: python
   :encoding: latin-1
   :linenos:
   :emphasize-lines: 7,8

.. note::
    Please follow the instructions at `BioNetGen <https://github.com/RuleWorld/bionetgen>`_
    and at `KaSim <https://github.com/Kappa-Dev/KaSim>`_ documentations to install
    the stochactic simulators. For network-based simulations (Ordinary Differential
    Equations and Gillespie`s algorithm), BioNetGen is required to perform the network
    generation. Change the corresponding paths (lines 7-8) to match the parent folder for
    the BNG2.pl or KaSim executable.
