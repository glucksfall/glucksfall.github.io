Welcome to Atlas v1.0 documentation!
====================================

Atlas is a small software developed to use simple text files that encode
biological networks and write Rule-Based Models (RBMs). Atlas writes rules and
others model components for the PySB python package `PySB`_, PMID `23423320`_.
The RBMs could be simulated within PySB with `NFsim`_, PMID `26556387`_ (within
the `BioNetGen2`_ software, PMID `27402907`_), KaSim (`KaSim`_, PMID
`29950016`_). Models could be exported to text files in *BioNetGen*
(`BioNetGenLanguage`_) or *kappa* language (`Kappa`_) for further calibration
(`BioNetFit`_, PMID `26556387`_ or `pleione`_, PMID `31641245`_) and analysis
(`sterope`_ for parameter sensibility and `alcyone`_ for parameter uncertainty).

.. toctree::
   :maxdepth: 3

   Installation
   Modeling
   Simulation
   Plotting
   Export_to

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. refs
.. _KaSim: https://github.com/Kappa-Dev/KaSim
.. _NFsim: https://github.com/RuleWorld/nfsim
.. _BioNetGen2: https://github.com/RuleWorld/bionetgen
.. _PISKaS: https://github.com/DLab/PISKaS
.. _BioNetFit: https://github.com/RuleWorld/BioNetFit
.. _SLURM: https://slurm.schedmd.com/
.. _PySB: http://pysb.org/

.. _Kappa: https://www.kappalanguage.org/
.. _BioNetGenLanguage: http://www.csb.pitt.edu/Faculty/Faeder/?page_id=409
.. _pandas: https://pandas.pydata.org/

.. _27402907: https://www.ncbi.nlm.nih.gov/pubmed/27402907
.. _26556387: https://www.ncbi.nlm.nih.gov/pubmed/26556387
.. _29950016: https://www.ncbi.nlm.nih.gov/pubmed/29950016
.. _29175206: https://www.ncbi.nlm.nih.gov/pubmed/29175206
.. _26556387: https://www.ncbi.nlm.nih.gov/pubmed/26556387
.. _31641245: https://www.ncbi.nlm.nih.gov/pubmed/31641245
.. _23423320: https://www.ncbi.nlm.nih.gov/pubmed/23423320

.. _pleiades: https://github.com/networkbiolab/pleiades
.. _pleione: https://github.com/networkbiolab/pleione
.. _sterope: https://github.com/networkbiolab/sterope
.. _alcyone: https://github.com/networkbiolab/alcyone
