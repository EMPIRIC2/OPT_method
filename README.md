# An Optimal Path Threshold (OPT) Method for Rigorously Identifying Extreme Climate Events

This repository contains the source code and data for the paper "An Optimal Path Threshold Method for Rigorously Identifying Extreme Climate Events," published in *Environmental Research Letters*.

**DOI:** [10.1088/1748-9326/adae24](https://doi.org/10.1088/1748-9326/adae24)

This work is part of the [EMPIRIC](https://github.com/EMPIRIC2) project.

## About the OPT Method

The Optimal Path Threshold (OPT) method is a dynamic programming-based approach that adaptively determines optimal thresholds for defining extreme events at specific severity levels. This repository provides examples of the 2D and 3D OPT methods.

## How to Run the Code

### Prerequisites

- Python 3
- NumPy

You can install NumPy using pip:

```bash
pip install numpy
```

### 2D OPT Method

The `Find_optimal_path.py` script provides an example of the 2D OPT method. It loads data from `air_heatwave_matrix.npy` and `lake_heatwave_matrix.npy` and calculates the optimal path.

To run the script:

```bash
python Find_optimal_path.py
```

### 3D OPT Method

The `Find_optimal_path_3d.py` script provides an example of the 3D OPT method. It loads data from `3d_compound_matrix.npy` and calculates the optimal path.

To run the script:

```bash
python Find_optimal_path_3d.py
```