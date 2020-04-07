from pysb.export import export
with open('model.kappa', 'w') as outfile:
	outfile.write(export(model, 'kappa'))
with open('model.bngl', 'w') as outfile:
	outfile.write(export(model, 'bngl'))
