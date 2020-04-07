Rule('LACTOSE_MUTAROTATION',
	met(name = 'alpha_lactose', loc = 'cyt') |
	met(name = 'beta_lactose', loc = 'cyt'),
	Parameter('fwd_LACTOSE_MUTAROTATION', 1),
	Parameter('rvs_LACTOSE_MUTAROTATION', 1))

Rule('GALACTOSE_MUTAROTATION',
	met(name = 'alpha_GALACTOSE', loc = 'cyt') |
	met(name = 'beta_GALACTOSE', loc = 'cyt'),
	Parameter('fwd_GALACTOSE_MUTAROTATION', 1),
	Parameter('rvs_GALACTOSE_MUTAROTATION', 1))

Rule('GLUCOSE_MUTAROTATION',
	met(name = 'alpha_glucose', loc = 'cyt') |
	met(name = 'beta_glucose', loc = 'cyt'),
	Parameter('fwd_GLUCOSE_MUTAROTATION', 1),
	Parameter('rvs_GLUCOSE_MUTAROTATION', 1))

Rule('TRANS_RXN_24',
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'per') +
	met(name = 'alpha_lactose', loc = 'per') |
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'cyt') +
	met(name = 'alpha_lactose', loc = 'cyt'),
	Parameter('fwd_TRANS_RXN_24', 1),
	Parameter('rvs_TRANS_RXN_24', 1))

Rule('TRANS_RXN_24_beta',
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'per') +
	met(name = 'beta_lactose', loc = 'per') |
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'cyt') +
	met(name = 'beta_lactose', loc = 'cyt'),
	Parameter('fwd_TRANS_RXN_24_beta', 1),
	Parameter('rvs_TRANS_RXN_24_beta', 1))

Rule('TRANS_RXN_94',
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'per') +
	met(name = 'MELIBIOSE', loc = 'per') |
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'cyt') +
	met(name = 'MELIBIOSE', loc = 'cyt'),
	Parameter('fwd_TRANS_RXN_94', 1),
	Parameter('rvs_TRANS_RXN_94', 1))

Rule('RXN0_7215', prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'per') +
	met(name = 'CPD_3561', loc = 'per') |
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'cyt') +
	met(name = 'CPD_3561', loc = 'cyt'),
	Parameter('fwd_RXN0_7215', 1),
	Parameter('rvs_RXN0_7215', 1))

Rule('RXN0_7217', prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'per') +
	met(name = 'CPD_3785', loc = 'per') |
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'cyt') +
	met(name = 'CPD_3785', loc = 'cyt'),
	Parameter('fwd_RXN0_7217', 1),
	Parameter('rvs_RXN0_7217', 1))

Rule('RXN_17755', prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'per') +
	met(name = 'CPD_3801', loc = 'per') |
	prot(name = 'LACY_MONOMER') +
	met(name = 'PROTON', loc = 'cyt') +
	met(name = 'CPD_3801', loc = 'cyt'),
	Parameter('fwd_RXN_17755', 1),
	Parameter('rvs_RXN_17755', 1))

Rule('BETAGALACTOSID_RXN',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_lactose', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_GALACTOSE', loc = 'cyt') +
	met(name = 'beta_glucose', loc = 'cyt'),
	Parameter('fwd_BETAGALACTOSID_RXN', 1),
	Parameter('rvs_BETAGALACTOSID_RXN', 1))

Rule('BETAGALACTOSID_RXN_alpha',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'alpha_lactose', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'alpha_GALACTOSE', loc = 'cyt') +
	met(name = 'alpha_glucose', loc = 'cyt'),
	Parameter('fwd_BETAGALACTOSID_RXN_alpha', 1),
	Parameter('rvs_BETAGALACTOSID_RXN_alpha', 1))

Rule('RXN0_5363',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'alpha_lactose', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt'),
	Parameter('fwd_RXN0_5363', 1),
	Parameter('rvs_RXN0_5363', 1))

Rule('RXN0_5363_beta',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_lactose', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt'),
	Parameter('fwd_RXN0_5363_beta', 1),
	Parameter('rvs_RXN0_5363_beta', 1))

Rule('ALLOLACTOSE_DEG_alpha',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'alpha_GALACTOSE', loc = 'cyt'),
	Parameter('fwd_ALLOLACTOSE_DEG_alpha', 1),
	Parameter('rvs_ALLOLACTOSE_DEG_alpha', 1))

Rule('ALLOLACTOSE_DEG_beta',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_GALACTOSE', loc = 'cyt'),
	Parameter('fwd_ALLOLACTOSE_DEG_beta', 1),
	Parameter('rvs_ALLOLACTOSE_DEG_beta', 1))

Rule('RXN_17726',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'CPD_3561', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_GALACTOSE', loc = 'cyt') +
	met(name = 'Fructofuranose', loc = 'cyt'),
	Parameter('fwd_RXN_17726', 1),
	Parameter('rvs_RXN_17726', 1))

Rule('RXN0_7219',
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'CPD_3785', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt') |
	cplx(name = 'BETAGALACTOSID_CPLX') +
	met(name = 'beta_GALACTOSE', loc = 'cyt') +
	met(name = 'D_ARABINOSE', loc = 'cyt'),
	Parameter('fwd_RXN0_7219', 1),
	Parameter('rvs_RXN0_7219', 1))

Rule('GALACTOACETYLTRAN_RXN_galactose',
	cplx(name = 'GALACTOACETYLTRAN_CPLX') +
	met(name = 'beta_GALACTOSE', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt') |
	cplx(name = 'GALACTOACETYLTRAN_CPLX') +
	met(name = '_6_Acetyl_beta_D_Galactose', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt'),
	Parameter('fwd_GALACTOACETYLTRAN_RXN_galactose', 1),
	Parameter('rvs_GALACTOACETYLTRAN_RXN_galactose', 1))
