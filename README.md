# SELFPHISH: a Self-supervised, Physics-Informed generative networks approach for the phase retrieval

# Overview

SELFPHISH is a data reconstruction framework that harnesses the power of self-supervised, physics-informed generative networks. While traditional reconstruction methods rely on intricate algorithms to piece together fragmented data, SELFPHISH leverages deep generative models that are both self-supervised and guided by physical constraints to reimagine and revitalize the phase retrieval process.

Originally designed for complex phase retrieval in tomography and holography, SELFPHISH shines in its adaptability. With the capability to incorporate user-defined forward models, this framework can be flexibly adapted for various advanced data reconstruction challenges.

# Features

1. Self-supervised, Physics-Informed Networks: At its core, SELFPHISH employs deep generative networks that are both self-supervised and physics-guided, enabling cutting-edge reconstruction performance.
2. Specialized for Phase Retrieval: Optimized for tasks in phase retrieval and tomography, ensuring precise and reliable reconstructions.
3. Modular Design: The architecture allows users to integrate their own forward models, making it adaptable for a range of reconstruction challenges.
4. Efficient and Scalable: Built to manage large datasets, SELFPHISH maintains speed and efficiency without compromising reconstruction accuracy.

# Installation

This guide provides detailed steps for setting up the `selfphish` package in a Conda environment.

## Steps for General Users

### 1. Create & Activate a Conda Environment
Open your terminal and create a new environment named `selfphish` with Python 3.11:

```bash
conda create --name selfphish python=3.10
conda activate selfphish
```

### 2. Install TensorFlow OR PyTorch 
Choose and install either TensorFlow or PyTorch based on your preference.

For TensorFlow:
```bash
pip install tensorflow
```

For PyTorch (ensure you select the correct version for your system from the official website):
```bash
# Example command for installing PyTorch with CUDA support
pip install torch torchvision torchaudio
```

### 3. Install 'selfphish' from PyPI
Finally, install the selfphish package from PyPI:
```bash
pip install selfphish
```

## Steps for Developers

If you are contributing to SELFPHISH development, please follow these steps to set up your development environment:

### 1. Create & Activate a Conda Environment
Open your terminal and create a new conda environment named `selfphish` with Python 3.11:

```bash
conda create --name selfphish python=3.10
conda activate selfphish
```

### 2. Install TensorFlow OR PyTorch 
Choose and install either TensorFlow or PyTorch.

For TensorFlow:
```bash
pip install tensorflow
```

For PyTorch:
```bash
# Example command for installing PyTorch with CUDA support
pip install torch torchvision torchaudio
```

### 3. Clone the SELFPHISH Repository
Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/XYangXRay/selfphish.git
```

### 4. Install the Required Packages
Navigate to the repository’s main directory and install the necessary packages in editable mode:

```bash
cd selfphish
python3 -m pip install -e .
```

## Additional Notes for Users

### Choosing Between TensorFlow and PyTorch
If unsure which one to choose, consider the requirements of your project or your familiarity with the libraries:
- **TensorFlow** is known for its production deployment capabilities and integration with TensorFlow Extended (TFX).
- **PyTorch** is favored for its simplicity, dynamic computation graph, and strong research community support.

### Installing GPU Support
SELFPHISH is designed for GPU-accelerated tasks. Ensure you install the GPU versions of TensorFlow or PyTorch. Refer to their official websites for instructions on installing GPU support.

# Examples

SELFPHISH currently includes examples for phase retrieval of holography:

1. Holography phase retrieval:
   - [Phase Retrieval Example](https://github.com/XYangXRay/selfphish/blob/main/examples/holography_tf.ipynb)
2. X-ray tomography:
   - [Tomography Example](https://github.com/XYangXRay/selfphish/blob/main/examples/tomography_tf.ipynb)

# References

If you find SELFPHISH useful for your research or projects, please consider citing:

J. Synchrotron Rad. (2020). 27, 486-493.  
Available at: [https://doi.org/10.1107/S1600577520000831](https://doi.org/10.1107/S1600577520000831)