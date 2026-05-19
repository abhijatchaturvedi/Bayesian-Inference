# Bayesian Network Parameter Estimation

Command-line implementation for learning Bayesian network parameters from fully observed categorical data.

The project estimates marginal and conditional probability tables for a directed acyclic graphical model. Given variable domains, a dependency matrix, and observed samples, it computes maximum-likelihood probability estimates for each node in the network.

## Overview

The program accepts a Bayesian network structure and training samples through standard input, then prints one probability table per variable.

It supports:

- categorical variables with arbitrary string labels
- parent-child dependencies represented as an adjacency matrix
- marginal distributions for root nodes
- conditional probability tables for dependent nodes
- deterministic 4-decimal output formatting

## Repository Structure

```text
.
├── bayesian_network_parameter_estimation.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Method

For each variable, the estimator identifies its parent nodes from the dependency matrix.

Root node probabilities are estimated as:

```text
P(X = x) = count(X = x) / total_samples
```

Dependent node probabilities are estimated as:

```text
P(X = x | Parents = p) = count(X = x and Parents = p) / count(Parents = p)
```

The implementation uses maximum-likelihood estimation over complete observations. If a parent configuration is not present in the sample set, the corresponding probability is reported as `0.0000`.

## Input Format

```text
n
domain_of_N1
domain_of_N2
...
domain_of_Nn
n x n dependency matrix
m
sample_1
sample_2
...
sample_m
```

Where:

- `n` is the number of variables.
- Each domain line contains comma-separated values for one variable.
- The dependency matrix uses `1` to indicate a directed dependency from row variable to column variable.
- `m` is the number of observed samples.
- Each sample contains comma-separated values for all variables in order.

## Example

Input:

```text
3
TRUE, FALSE
TRUE, FALSE
TRUE, FALSE
0 0 1
0 0 1
0 0 0
4
TRUE, TRUE, TRUE
TRUE, FALSE, FALSE
FALSE, TRUE, TRUE
FALSE, FALSE, FALSE
```

Run:

```bash
python bayesian_network_parameter_estimation.py < input.txt
```

Output:

```text
0.5000 0.5000
0.5000 0.5000
1.0000 0.0000 1.0000 0.0000 0.0000 1.0000 0.0000 1.0000
```

## Output Format

The program prints `n` lines. Each line contains the learned probability values for the corresponding variable.

For variables with parents, probabilities are emitted by iterating over each value in the variable domain, then over every parent-value configuration in domain order.

## Requirements

The implementation uses only the Python standard library.

Recommended runtime:

```text
Python 3.9+
```

No third-party packages are required. A `requirements.txt` file is included for environment setup workflows that expect one.
