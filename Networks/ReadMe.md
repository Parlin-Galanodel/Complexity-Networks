# This is the Network project investigated the degree distribution of a graph generated by BA model  
There are several files in this folder:
* *requirements.txt* list the modules required by the project, I highly recommend using Anaconda since the project used anaconda=2020.11=py38_0 
* *implementation.py* contains the implementation of he module used in this project, the most important part are 3 function used to generate graphs. `pref` generate graph by BA model with preferential attachment. `ran` employs pure random sampling instead of preferential method. `mix` as the name, used a mixed sampling method with probability q of preferential attachment.
* *data_generating.py* generates datas with paramaters defined in it by calling functons in *implementation.py*
* *logbin.py* is a logbin ploting method implemented by **Max Falkenberg McGillivray**
* *degree_distribution.py* is just a function to get the k distribution of a graph.
* 3 folders DATA contains data generated, RefferedImagesByIpynb contains the image reffered by the jupyter notebook, reference contains the material refered by doing this project.
* *Networks.ipynb* is an jupyter notebook walk you through the whole project with some explainations.
