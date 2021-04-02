#The Complexity Project

These are the code for complexity project, specifically, for the 1-d oslo model. Using analysis with saved data would be enough to generate the plots. Run ddata.py to generate another group of data.

###Site.py & Pile.py
The class files for the oslo model. Site is the class describe any site in an 1-d oslo model. Pile is the data container or lattice for the oslo model. Pile composed by a list of sites and contains some further information for the whole data sequence.   
The oslo model is implemented by these 2 files and could work independent of functions in other files.

###Data.py
This is just a method to acquire essential data and serialise them to files with json module. The data saving is necessary because the runningtime for a whole simulation is too long even running by multiple process.   

###task1.py
This is kind of unit test to check if the model works as expected. This is not a very strict check but just use the simple case with known values to see if the model gives a good approximation. 

###data for 4/8/16/32/64/128/256/512:
The Data for the simulation of different system size.

###Analysis.py
This files gives the helper functions used to analyse the data and then generate plots.