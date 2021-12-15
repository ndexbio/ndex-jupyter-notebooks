# NDEx Jupyter Notebook Tutorials
This repository contains tutorials and code examples to work with networks using the ndex2 Python Client and NiceCX object class. 
These tutorials require Python 3.6+ and the ndex2 module. 
See the [ndex2 client](https://github.com/ndexbio/ndex2-client#readme) for installation instructions.
The Sphinx documentation for the ndex2 client package is at https://ndex2.readthedocs.io/en/latest/.

## [Access node, edge, and network attributes in NiceCX](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Access%20node%2C%20edge%2C%20and%20network%20attributes%20in%20NiceCX.ipynb)


## [Edit an NDEx Network Using networkx and Save as a New Network](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Edit%20an%20NDEx%20Network%20Using%20networkx%20and%20Save%20as%20a%20New%20Network.ipynb)
This notebook shows how to:
* download a network from NDEx as a NiceCX network
* make a networkxGraph()object via the to_networkx(mode='default') method
* display the networkx network
* remove 0 degree nodes
* create a new NiceCX network from the modified networkx network
* upload the new network to NDEx.

## [Find Subgraphs of NDEx Networks with Neighborhood Queries](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Find%20Subgraphs%20of%20NDEx%20Networks%20with%20Neighborhood%20Queries.ipynb)
This notebook shows how to find subgraphs of NDEx networks based on queries in which a list of strings is applied to a network. The result returned is a CX network containing nodes whose names match one of the strings and nodes that are "nearby" in the network, the "neighborhood" subgraph. A common use for these queries is to find subgraphs of an interactome based on a list of gene names.

## [Five ways to create NiceCX networks](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Five%20ways%20to%20create%20NiceCX%20networks.ipynb)
This notebook shows how to create a NiceCX network from:
* An Empty Network
* A CX File
* An NDEx Networks
* A NetworkX Network
* A Pandas DataFrame

## [Style and Edit an NDEx Network](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Style%20and%20Edit%20an%20NDEx%20Network.ipynb)
This notebook shows how to:
* Load a network from NDEx
* Copy and apply a visual style from an existing template in NDEx
* Save (upload) the modified network to your NDEx account
* Apply a layout
* Save (update) the modified network to your NDEx account

## [Using NDEx Network Sets](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Using%20NDEx%20Network%20Sets.ipynb)
Network Sets are used to group networks. They are essentially sets of "bookmarks", where a network can belong to many different sets, created by different users. This notebook shows how to:
* Get a network set
* Operate on the networks in a set
* Create a network set
* Add a network to a set
* Remove a network from a set
* Rename a network set
* Delete a network set

#
## Legacy Tutorials
#

## [Protocol 3: Working with NDEx Networks in Python](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Working%20with%20NDEx%20Networks%20in%20Python.ipynb)
This notebook shows how to perform simple operations on networks stored in NDEx, using the ndex2 client and NiceCX class. This notebook is part of the latest NDEx publication in the journal Current Protocols in Bioinformatics (reference coming soon). [**>> Go to Tutorial**](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/Working%20with%20NDEx%20Networks%20in%20Python.ipynb)

## [ndex2 Client v2.0 Tutorial](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NDEx2%20Client%20v2.0%20Tutorial.ipynb)
In this tutorial you will learn to use the ndex2 Python client. The ndex2 client is a module that simplifies access to the NDEx Server API and provides convenience methods for common operations on networks. [**>> Go to Tutorial**](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NDEx2%20Client%20v2.0%20Tutorial.ipynb)

## [ndex2 Client v2.0 Tutorial: Querying networks](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NDEx%20Query%20Tutorial.ipynb)
This tutorial shows how to query networks in NDEx, extract a subset of the data  and display the results using both the ndex2 client and NiceCX object class. [**>> Go to Tutorial**](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NDEx%20Query%20Tutorial.ipynb)

## [NiceCX v2.0 Tutorial](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NiceCX%20v2.0%20Tutorial.ipynb)
In this tutorial you will learn to use NiceCX, a simple data model that is part of the ndex2 client module. NiceCX facilitates creating and working with networks, including interfaces to NetworkX and Pandas. [**>> Go to Tutorial**](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NiceCX%20v2.0%20Tutorial.ipynb)

## [NiceCX v2.0 Tutorial: Navigating the Network](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NiceCX%20v2.0%20navigating%20the%20network.ipynb)
This tutorial is focused on accessing a network's nodes, edges and attributes. [**>> Go to Tutorial**](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NiceCX%20v2.0%20navigating%20the%20network.ipynb)

## [NiceCX v2.0 Tutorial: Prune Zero Degree Nodes](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NiceCX%20v2.0%20prune%20zero%20degree%20nodes.ipynb)
In this tutorial you will learn how to manipulate an NDEx network by converting it to a networkx graph() object. This tutorial requires **_Python 3.7 and networkx 2.4_**. [**>> Go to Tutorial**](https://github.com/ndexbio/ndex-jupyter-notebooks/blob/master/notebooks/NiceCX%20v2.0%20prune%20zero%20degree%20nodes.ipynb)

