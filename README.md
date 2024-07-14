### Watershed Tools ###

#### Synopsis ####
A collection of python scripts to discretize a watershed shapefile into sub-areas to account for geospatial attributes.<br>

Authors: Andy Wood and Hongli Liu designed and developed the code from 2020 to 2021. Hongli Liu conducted initial code prototyping according to the specified design, while Andy Wood later upgraded the code through revisions, debugging, streamlining, testing, and documentation. In July 2024, Hongli Liu revised this code repository specifically for a case study in Utah.<br>

#### Code organization ####
The code is organized into subdirectories as follows:<br>
 * steps/
 * functions/

#### Code workflow ####
The recommended workflow for applying this code is to run the scripts in the 'steps' folder sequentially.

#### Contact ####
Hongli Liu, hongli.liu@ualberta.ca

#### References and Acknowledgements ####
The development of this code base and the associated experimental project (led by A. Wood) was funded by the US Bureau of Reclamation under Cooperative Agreement #R16AC00039.<br>
The initial application of the code is described in:<br>
    Liu, H, AW Wood, D Broman, G Brown, and J Lanini, 2021.  Impact of SUMMA hydrologic model discretization on the representation of snowmelt and runoff variability.  J. Hydromet. (in prep, target submission Nov 2021)..<br>
We thank Genevieve Brown of the University of Waterloo for providing the code implementation of the radiation algorithm that was included in the radiation preparation step.  <br>
We also thank Wouter Knoben for providing a MERIT-based DEM file and Naoki Mizukami for providing the landcover dataset file and soiltype files that were used in the initial experiment & development. <br>





