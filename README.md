# G-XAI Bench

G-XAI Bench is an open-source library for evaluating graph neural network (GNN) explainers. This library provides XAI-ready datasets, a number of state-of-the-art explainers, and evaluation metrics for explanations. One of the major features of this package is the novel, flexible ShapeGraph dataset generator which can generate graph datasets with unique ground-truth explanations. In addition, ShapeGraph is parameterized such that generated graphs can have varying sizes, degree distributions, types of ground-truth explanations, levels of homophily/heterophily, and degrees of fairness as defined by a protected feature. 

## Installation

After cloning the repo, install the graphxai package from the root directory of this project:

  ```pip install -e .```
  
This will allow you to access features within the package, including datasets, explainers, and evaluation tools.

## Data Availability

Downloads are provided for the datasets in our package through our page on the [Harvard Dataverse](https://doi.org/10.7910/DVN/KULOS8). 
