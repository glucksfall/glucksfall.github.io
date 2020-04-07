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
