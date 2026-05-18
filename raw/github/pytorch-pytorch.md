# pytorch/pytorch

## Metadata
- Stars: 99982
- Primary language: Python
- Default branch: main
- Latest release: v2.12.0 (2026-05-13)
- License: Other (BSD-style)
- Homepage: https://pytorch.org
- Fetched: 2026-05-18
- Final URL: https://github.com/pytorch/pytorch

## Description
Tensors and Dynamic neural networks in Python with strong GPU acceleration

## README
![PyTorch Logo](https://github.com/pytorch/pytorch/raw/main/docs/source/_static/img/pytorch-logo-dark.png)

PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy, and Cython to extend PyTorch when needed.

Our trunk health (Continuous Integration signals) can be found at [hud.pytorch.org](https://hud.pytorch.org/ci/pytorch/pytorch/main).

## More About PyTorch

At a granular level, PyTorch is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **torch** | A Tensor library like NumPy, with strong GPU support |
| **torch.autograd** | A tape-based automatic differentiation library that supports all differentiable Tensor operations in torch |
| **torch.jit** | A compilation stack (TorchScript) to create serializable and optimizable models from PyTorch code |
| **torch.nn** | A neural networks library deeply integrated with autograd designed for maximum flexibility |
| **torch.multiprocessing** | Python multiprocessing, but with magical memory sharing of torch Tensors across processes. Useful for data loading and Hogwild training |
| **torch.utils** | DataLoader and other utility functions for convenience |

Usually, PyTorch is used either as:
- A replacement for NumPy to use the power of GPUs.
- A deep learning research platform that provides maximum flexibility and speed.

### A GPU-Ready Tensor Library

PyTorch provides Tensors that can live either on the CPU or the GPU and accelerates the computation by a huge amount. We provide a wide variety of tensor routines to accelerate and fit your scientific computation needs such as slicing, indexing, mathematical operations, linear algebra, reductions.

### Dynamic Neural Networks: Tape-Based Autograd

PyTorch has a unique way of building neural networks: using and replaying a tape recorder. Most frameworks such as TensorFlow, Theano, Caffe, and CNTK have a static view of the world. With PyTorch, we use a technique called reverse-mode auto-differentiation, which allows you to change the way your network behaves arbitrarily with zero lag or overhead.

### Python First

PyTorch is not a Python binding into a monolithic C++ framework. It is built to be deeply integrated into Python. You can use it naturally like you would use NumPy / SciPy / scikit-learn etc. You can write your new neural network layers in Python itself, using your favorite libraries and use packages such as Cython and Numba.

### Imperative Experiences

PyTorch is designed to be intuitive, linear in thought, and easy to use. When you execute a line of code, it gets executed. There isn't an asynchronous view of the world. When you drop into a debugger or receive error messages and stack traces, understanding them is straightforward.

### Fast and Lean

PyTorch has minimal framework overhead. We integrate acceleration libraries such as Intel MKL and NVIDIA (cuDNN, NCCL) to maximize speed. At the core, its CPU and GPU Tensor and neural network backends are mature and have been tested for years. The memory usage in PyTorch is extremely efficient compared to Torch or some of the alternatives.

### Extensions Without Pain

Writing new neural network modules, or interfacing with PyTorch's Tensor API, was designed to be straightforward and with minimal abstractions. You can write new neural network layers in Python using the torch API or your favorite NumPy-based libraries such as SciPy. If you want to write your layers in C/C++, we provide a convenient extension API that is efficient and with minimal boilerplate.

## Installation

### Binaries
Commands to install binaries via Conda or pip wheels are on our website: https://pytorch.org/get-started/locally/

### From Source

Prerequisites:
- Python 3.10 or later
- A compiler that fully supports C++20, such as clang or gcc (gcc 11.3.0 or newer is required, on Linux)
- Visual Studio or Visual Studio Build Tool (Windows only)
- At least 10 GB of free disk space
- 30-60 minutes for the initial build

CUDA Support: https://pytorch.org/get-started/locally/
AMD ROCm Support available.
Intel GPU Support available.

## Getting Started

- Tutorials: https://pytorch.org/tutorials/
- Examples: https://github.com/pytorch/examples
- API Reference: https://pytorch.org/docs/
- Glossary: https://github.com/pytorch/pytorch/blob/main/GLOSSARY.md

## Communication
- Forums: https://discuss.pytorch.org
- GitHub Issues: Bug reports, feature requests, install issues, RFCs, thoughts, etc.
- Slack: https://pytorch.slack.com/
- Newsletter: https://eepurl.com/cbG0rv
- Facebook Page: https://www.facebook.com/pytorch

## Releases and Contributing

Typically, PyTorch has three minor releases a year. Contributions are welcome — bug fixes can be submitted directly as PRs; new features should start with an issue for discussion first. See CONTRIBUTING.md and RELEASE.md.

## License

PyTorch has a BSD-style license, as found in the LICENSE file.

## Top-level structure
- `torch/` — main Python package (nn, autograd, jit, distributed, etc.)
- `aten/` — ATen tensor library (C++ tensor operations backend)
- `c10/` — core library (allocators, streams, device abstractions)
- `caffe2/` — Caffe2 (merged into PyTorch ecosystem)
- `functorch/` — function transforms (vmap, grad, etc.)
- `docs/` — documentation source
- `test/` — test suite
- `tools/` — build tools and codegen utilities
- `benchmarks/` — performance benchmarks
- `android/` — Android mobile support
- `third_party/` — third-party dependencies
- `scripts/` — CI and automation scripts
- `cmake/` — CMake build configuration
- `AGENTS.md` — AI agent instructions (present)
- `CLAUDE.md` — Claude AI agent instructions (present)
- `CONTRIBUTING.md` — contribution guide
- `RELEASE.md` — release guide
- `GLOSSARY.md` — PyTorch terminology glossary
- `.ci/` — CI pipeline configurations
