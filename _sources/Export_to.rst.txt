Export to
=========

The PySB python package could export to different languages
(See more `here <https://pysb.readthedocs.io/en/stable/modules/export/>`_).
Use the following code to export to BioNetGen and *kappa* languages, putting
the code at the end of the model.

.. code-block:: python3

	from pysb.export import export
	with open('model.kappa', 'w') as outfile:
		outfile.write(export(model, 'kappa'))
	with open('model.bngl', 'w') as outfile:
		outfile.write(export(model, 'bngl'))

.. note::
	In the case of matlab, mathematica, and stochkit, PySB requires to expand
	the rules to determine all mass-balances to write ODE-based models, a proccess
	call network generation and could take excessive time to finish.
