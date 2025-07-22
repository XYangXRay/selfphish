
# SELFPHISH: Self-supervised, Physics-Informed Generative Networks for Phase Retrieval

![PyPI](https://img.shields.io/pypi/v/selfphish)
![License](https://img.shields.io/github/license/XYangXRay/selfphish)
![Python](https://img.shields.io/pypi/pyversions/selfphish)

## Overview

**SELFPHISH** is a flexible data reconstruction framework that harnesses self-supervised, physics-informed generative networks. Unlike traditional methods that rely on complex algorithms, SELFPHISH leverages deep generative models guided by physical constraints to advance the phase retrieval process.

Originally designed for complex phase retrieval in tomography and holography, SELFPHISH is highly adaptable and can incorporate user-defined forward models for a wide range of advanced data reconstruction challenges.

## Features

- **Self-supervised, Physics-Informed Networks:** Deep generative networks that are both self-supervised and physics-guided for state-of-the-art reconstruction.
- **Specialized for Phase Retrieval:** Optimized for phase retrieval and tomography tasks, ensuring precise and reliable reconstructions.
- **Modular Design:** Easily integrate custom forward models for diverse reconstruction challenges.
- **Efficient and Scalable:** Handles large datasets efficiently without compromising accuracy.

![The flowchart of Selfphish](docs/source/figures/algorithm_flowchart.png)
---


## Installation

The following steps will help you set up the `selfphish` package in a Conda environment.


### For General Users

1. **Create & Activate a Conda Environment**

   ```bash
   conda create --name selfphish python=3.11
   conda activate selfphish
   ```

2. **Install SELFPHISH from PyPI**

   - For the default TensorFlow backend:
     ```bash
     pip install selfphish
     ```
   - For the PyTorch backend:
     ```bash
     pip install "selfphish[pytorch]"
     ```

---

### For Developers

If you are contributing to SELFPHISH development, follow these steps:

1. **Create & Activate a Conda Environment**
   ```bash
   conda create --name selfphish python=3.11
   conda activate selfphish
   ```

2. **Clone the SELFPHISH Repository**
   ```bash
   git clone https://github.com/XYangXRay/selfphish.git
   cd selfphish
   ```

3. **Install Required Packages in Editable Mode**
   ```bash
   python3 -m pip install -e .
   ```

---

## Additional Notes

- **Choosing a Backend:**
  - *TensorFlow* is recommended for production and TFX integration.
  - *PyTorch* is popular for research and dynamic computation graphs.
- **GPU Support:**
  - SELFPHISH is designed for GPU acceleration. Install the GPU versions of TensorFlow or PyTorch as needed. See their official documentation for details.

---


## Examples

SELFPHISH includes ready-to-run examples for phase retrieval and tomography:

1. **Holography phase retrieval:**
   - [Phase Retrieval Example](https://github.com/XYangXRay/selfphish/blob/main/examples/holography_tf.ipynb)
2. **X-ray tomography:**
   - [Tomography Example](https://github.com/XYangXRay/selfphish/blob/main/examples/tomography_tf.ipynb)

---

## Citation

If you use SELFPHISH in your research or projects, please cite:

J. Synchrotron Rad. (2020). 27, 486-493.  
Available at: [https://doi.org/10.1107/S1600577520000831](https://doi.org/10.1107/S1600577520000831)