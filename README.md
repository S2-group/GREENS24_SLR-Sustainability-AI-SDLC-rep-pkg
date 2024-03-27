[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10887409.svg)](https://doi.org/10.5281/zenodo.10887409)

# GREENS24_SLR-Sustainability-AI-SDLC-rep-pkg
This repository is a companion page for the following research accepted at the 8th International Workshop on Green and Sustainable Software (GREENS’24):

E. Trinh, M. Funke, P. Lago, and J. Bogner, "Sustainability Integration of Artificial Intelligence into the Software Development Life Cycle," 2024.  (accepted for publication)

It contains all the material required for replicating the study, including: raw data, figures, and results.

Repository Structure
---------------
This is the root directory of the repository. The directory is structured as follows:

    SLR-Sustainability-AI-SDLC-rep-pkg
     .
     |
     |--- data/
            |
            |--- initialsearchpruning.pdf
                    Spreadsheet containing containing all primary studies including at which stage they were removed
            |--- Literature to Dimension+AI Mapping.xlsx
                    Spreadsheet containing the associated sustainability dimensions and discussed machine learning models of each primary study
     |
     |--- results/
            |
            |--- /figures
                    Contains all produced and used figures throughout this research
            |
            |--- references.bib
                    Contains all BibTeX references used in the report
     |
     |--- src/
            |
            |--- plotaimodels.py
                    Python script to plot the distribution of all AI models           
            |--- plotsustdim.py
                    Python script to plot the distribution of all sustainability dimensions across SDLC phases   


created by [Eames Trinh](https://github.com/EamesTrinh)
