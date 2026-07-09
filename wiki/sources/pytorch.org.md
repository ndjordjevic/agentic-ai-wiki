---
type: source
category: "Model infra, ML & providers"
source_url: https://pytorch.org/
companion_urls:
  - https://github.com/pytorch/pytorch
raw_files:
  - ../../raw/web/pytorch.org.md
  - ../../raw/github/pytorch-pytorch.md
tags:
  - deep-learning-framework
  - tensor-computation
  - autograd
  - neural-networks
  - distributed-training
  - torchscript
  - gpu-acceleration
  - python-first
related:
  - huggingface.co
  - fastai-fastbook
product: pytorch
detail_level: standard
created: 2026-05-18
updated: 2026-07-02
---

PyTorch is the dominant open-source deep learning framework, providing GPU-accelerated tensor computation and a dynamic neural network library built around a tape-based autograd system. Originally developed at Facebook AI Research, it is now stewarded by the PyTorch Foundation under the Linux Foundation and has become the framework of choice for research (99k+ GitHub stars, v2.12.0 current) and increasingly for production via TorchScript and TorchServe. For agentic AI practitioners, PyTorch is foundational infrastructure: virtually every leading model (LLMs, vision models, multimodal systems) is trained or fine-tuned with PyTorch, and inference runtimes, quantization tools, and serving infrastructure (TorchServe, ExecuTorch for edge) are all part of the same ecosystem.

_All claims below are sourced from ../../raw/web/pytorch.org.md unless otherwise noted._

## What it does

PyTorch provides two core capabilities:

1. **Tensor computation** — a NumPy-like tensor library with strong GPU/accelerator support. Tensors can reside on CPU or GPU and support slicing, indexing, mathematical operations, linear algebra, and reductions — all with hardware acceleration.
2. **Dynamic neural networks** — a tape-based automatic differentiation system (`torch.autograd`) that builds the computation graph dynamically at runtime. Unlike static-graph frameworks, this means the network architecture can change on each forward pass, enabling flexible research workflows.

Beyond these primitives, PyTorch provides a complete ML stack:
- `torch.nn` — neural network layers, loss functions, and activations
- `torch.jit` (TorchScript) — compilation stack to serialize and optimize models for production C++ runtimes
- `torch.distributed` — distributed training across multiple GPUs and nodes
- `torch.utils.data` — `DataLoader` and `Dataset` primitives for efficient data pipelines
- Domain libraries: TorchVision, TorchText, TorchAudio

## Key features

- **Eager execution by default** — code runs line-by-line; debugging with standard Python tools works naturally. No session or graph compilation step required.
- **TorchScript** — JIT-compile Python models to a static graph for production deployment; supports export to C++ runtime and serialization to `.pt` files.
- **TorchServe** — production model serving tool; multi-model serving, logging, metrics, RESTful endpoints; cloud and environment agnostic. (../../raw/github/pytorch-pytorch.md)
- **Distributed training** — `torch.distributed` backend supports data-parallel, model-parallel, and pipeline-parallel training; integrates NCCL (NVIDIA) and Gloo backends.
- **Native ONNX export** — `torch.onnx.export()` for interoperability with ONNX-compatible runtimes and visualizers.
- **C++ Front-End** — pure C++ interface (`libtorch`) following the Python API design; for high performance, low-latency applications. (../../raw/github/pytorch-pytorch.md)
- **ExecuTorch** — extends PyTorch to edge devices (mobile, embedded); end-to-end workflow from Python to iOS and Android.
- **Hardware backends** — CUDA (NVIDIA), ROCm (AMD), MPS (Apple Silicon), XPU (Intel), CPU.
- **Latest release** — PyTorch 2.12.0 (May 2026): improvements in linalg (100× speedup on batched CUDA eigh), compilation, distributed systems, graph capture, and expanded accelerator support. (../../raw/github/pytorch-pytorch.md)

## Architecture

PyTorch's architecture is layered from Python down to hardware: (../../raw/github/pytorch-pytorch.md)

- **Python layer** — user-facing API (`torch`, `torch.nn`, `torch.optim`, `torch.utils.data`); deeply integrated with the Python interpreter rather than wrapping a monolithic C++ runtime.
- **ATen (A Tensor library)** — the C++ tensor operations backend; provides the ~1000+ operators that all PyTorch code ultimately dispatches to. Lives in `aten/`.
- **c10** — core library providing device abstractions, memory allocators, stream management; platform-independent. Lives in `c10/`.
- **torch.autograd** — reverse-mode automatic differentiation; builds the computation graph dynamically using a "tape" that records operations as they execute; supports higher-order derivatives.
- **TorchScript / `torch.jit`** — compilation stack; converts Python/PyTorch models to an intermediate representation (IR) that can be serialized, optimized, and run independently of Python.
- **torch.fx** — symbolic tracing and graph transformation toolkit; enables program analysis and optimization passes at the Python level.
- **Compile stack (torch.compile)** — introduced in 2.x; uses TorchDynamo (bytecode-level graph capture) + TorchInductor (code generation) to compile models to optimized kernels without requiring TorchScript rewrites.
- **Functorch** — JAX-style function transforms (`vmap`, `grad`, `jacrev`) built on top of the core dispatcher; lives in `functorch/`. (../../raw/github/pytorch-pytorch.md)

## Installation

Via pip (recommended): (../../raw/github/pytorch-pytorch.md)

```bash
# CUDA 11.8
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# CPU only
pip3 install torch torchvision torchaudio
```

From source requires Python 3.10+, C++20-compatible compiler, 10+ GB disk space, 30–60 min build time. Full instructions: https://github.com/pytorch/pytorch#from-source

## Example usage

Basic neural network training workflow: (../../raw/github/pytorch-pytorch.md)

```python
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import v2

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512), nn.ReLU(),
            nn.Linear(512, 512), nn.ReLU(),
            nn.Linear(512, 10),
        )
    def forward(self, x):
        x = self.flatten(x)
        return self.linear_relu_stack(x)

model = NeuralNetwork().to("cuda")
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
```

Verify tensor computation:
```python
import torch
x = torch.rand(5, 3)
print(x)  # tensor([[0.338, ...], ...])
torch.cuda.is_available()  # True if CUDA GPU available
```

## When to use

- **Training or fine-tuning deep learning models** — PyTorch is the dominant choice for research and increasingly for production; most published architectures ship PyTorch implementations first.
- **Building on top of pre-trained models** — integrates natively with Hugging Face Transformers and Hub; most open-weight LLMs and vision models are distributed in PyTorch format.
- **Production inference at scale** — TorchServe for REST API serving; TorchScript/ONNX export for optimized runtimes; ExecuTorch for edge/mobile.
- **Research requiring flexible architectures** — dynamic computation graphs allow architecture changes between forward passes; no graph recompilation needed.
- **When you need C++ integration** — libtorch provides a stable C++ API for embedding PyTorch in game engines, robotics systems, or any latency-sensitive application.

## Maintenance status

PyTorch 2.12.0 released May 2026; three minor releases per year cadence. ~99,982 GitHub stars, 27,807 forks. BSD-style license. Maintained by the PyTorch Foundation (Linux Foundation member project). Core maintainers: Soumith Chintala, Gregory Chanan, Dmytro Dzhulgakov, Edward Yang, Alban Desmaison, Piotr Bialecki, Nikita Shulga. Active CI at hud.pytorch.org. (../../raw/github/pytorch-pytorch.md)

## Ecosystem

The PyTorch ecosystem is extensive: (../../raw/github/pytorch-pytorch.md)

- **Hugging Face Transformers** — built on PyTorch; the primary distribution channel for LLMs and vision-language models; see [[huggingface.co]].
- **TorchVision / TorchText / TorchAudio** — official domain libraries for CV, NLP, and audio respectively.
- **PyTorch Geometric** — graph neural networks on irregular data (graphs, point clouds).
- **Captum** — model interpretability / explainability.
- **skorch** — scikit-learn-compatible high-level PyTorch wrapper.
- **vLLM / DeepSpeed** — high-throughput LLM inference and training optimization built on PyTorch (tracked as Projects in llms.txt).
- **ExecuTorch** — edge deployment: iOS, Android, embedded systems.
- **PyTorch Hub** — model repository with pre-trained checkpoints (ResNet, AlexNet, DenseNet, GAN models, NLP Transformers).
- **Landscape** — full ecosystem catalog at https://pytorch.landscape2.io

## Documentation

Official docs at https://pytorch.org/docs/ (currently v2.12); tutorials at https://pytorch.org/tutorials/. Tutorial series covers the full ML workflow: Tensors → Datasets & DataLoaders → Transforms → Build Model → Autograd → Optimization → Save & Load.
