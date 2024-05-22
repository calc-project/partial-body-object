# Data and Code Accompanying the Study "Partial Colexifications Reveal Directional Tendencies in Object Naming"

## Table of Contents

1. [Introduction](#introduction)
2. [Citation](#how-to-cite)
3. [Networks](#network-representations)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

The present study uses the methods and data presented in [List (2023)](https://doi.org/10.3389/fpsyg.2023.1156540) and [Tjuka (2024)](https://doi.org/10.1515/lingty-2023-0032) to investigate the directionality of partial colexifications between the semantic domains of the human body and objects. We test the prediction that meaning extensions move predominantly from the body domain to the object domain.

## How to cite 

When using the data, please quote the original paper:

> Tjuka, Annika, and Johann-Mattis List (2024): Partial Colexifications Reveal Directional Tendencies in Object Naming. _Yearbook of the German Cognitive Linguistics Association_. [accepted]

## Network representations

For the exploratory data analysis, we used the TSV file [`affix-subgraph.gml`](graphs/affix-subgraph.gml), which we analyzed with the help of [Cytoscape](https://cytoscape.org). See [Tjuka (2024)](https://doi.org/10.15475/calcip.2024.1.2) for a detailed tutorial illustrating how data can be analyzed with Cytoscape.

## Directory Structure

Below is the directory structure of the project with comments explaining each part:

calc-project/partial-body-object/
│
├── concept-lists/ # Files provided in previous studies and the basis for the comparison of partial body-object colexifications extracted from [https://github. com/lexibank/tjukabodyobject/tree/v0.1.0](https://github. com/lexibank/tjukabodyobject/tree/v0.1.0) and [https://github.com/lingpy/pacs/tree/v1.0](https://github.com/lingpy/pacs/tree/v1.0).
│
├── directions/ # Files with the frequencies of directions of partial body-object colexifications across languages extracted from [https://github.com/lingpy/pacs/tree/v1.0](https://github.com/lingpy/pacs/tree/v1.0).
├── graphs/ # GML file for partial colexification network extracted from [https://github.com/lingpy/pacs/tree/v1.0][https://github.com/lingpy/pacs/tree/v1.0], Cytoscape files for individual networks, and corresponding PNG files.
│
├── .gitignore # Git ignore file
├── LICENSE # License file
├── README.md # This README file