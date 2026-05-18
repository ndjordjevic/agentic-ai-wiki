# huggingface.co

## Fetch log
- Inbox URL: https://huggingface.co/
- Final URL: https://huggingface.co/
- Fetched: 2026-05-18
- Pages: 6
- Mode: standard

## Landing page — https://huggingface.co/

Navigation:
- Models, Datasets, Spaces, Buckets (new), Docs, Enterprise, Pricing
- Website: Tasks, HuggingChat, Collections, Languages, Organizations
- Community: Blog, Posts, Daily Papers, Learn, Discord, Forum, GitHub (https://github.com/huggingface)
- Solutions: Team & Enterprise, Hugging Face PRO, Enterprise Support, Inference Providers, Inference Endpoints, Storage Buckets

Hero: "The platform where the machine learning community collaborates on models, datasets, and applications."

Taglines:
- "Create, discover and collaborate on ML better."
- The collaboration platform — Host and collaborate on unlimited public models, datasets and applications.
- Move faster with the HF Open source stack.
- Explore all modalities — Text, image, video, audio or even 3D.
- Build your portfolio — Share your work with the world and build your ML profile.

Compute & Enterprise solutions:
- Team & Enterprise — enterprise-grade security, access controls and dedicated support
- Inference Providers — 45,000+ models from leading AI providers through a single, unified API with no service fees

Featured open-source libraries (with GitHub star counts):
- Transformers (160,718 stars) — State-of-the-art AI models for PyTorch
- Diffusers (33,650) — State-of-the-art Diffusion models in PyTorch
- Safetensors (3,743) — Safe way to store/distribute neural network weights
- Hub Python Library (3,603) — Python client to interact with the Hugging Face Hub
- Tokenizers (10,744) — Fast tokenizers optimized for research & production
- TRL (18,402) — Train transformers LMs with reinforcement learning
- Transformers.js (16,010) — State-of-the-art ML running directly in your browser
- smolagents (27,367) — Smol library to build great agents in Python
- PEFT (21,138) — Parameter-efficient finetuning for large language models
- Datasets (21,521) — Access & share datasets for any ML tasks
- Text Generation Inference (10,853) — Serve language models with TGI optimized toolkit
- Accelerate (9,687) — Train PyTorch models with multi-GPU, TPU, mixed precision

## Docs — https://huggingface.co/docs

### Hub & Client Libraries
- Hub — Host Git-based models, datasets, and Spaces on the HF Hub
- Hub Python Library — Python client to interact with the Hugging Face Hub
- CLI — Tools for agents and humans to interact with all the Hugging Face services
- Huggingface.js — JavaScript libraries for Hugging Face with built-in TS types
- Tasks — Explore demos, models, and datasets for any ML tasks
- Dataset viewer — API for metadata, stats, and content of HF Hub datasets

### Deployment & Inference
- Inference Providers — Call 200k+ models hosted by our 10+ Inference partners
- Inference Endpoints (dedicated) — Deploy models on dedicated & fully managed infrastructure on HF
- Deploying on AWS — Train/deploy models from Hugging Face to AWS with DLCs
- Text Generation Inference — Serve language models with TGI optimized toolkit
- Text Embeddings Inference — Serve embeddings models with TEI optimized toolkit
- Microsoft Azure — Deploy Hugging Face models on Microsoft Azure
- Google Cloud — Train and Deploy Hugging Face models on Google Cloud

### Core ML Libraries
- Transformers, Diffusers, Datasets, Transformers.js, Tokenizers, Evaluate, timm, Sentence Transformers, Kernels

### Training & Optimization
- PEFT, Accelerate, Optimum, AWS Trainium & Inferentia, Google TPUs, TRL, Safetensors, Bitsandbytes, Lighteval

### Collaboration & Extras
- Gradio — Build ML demos and web apps with a few lines of Python
- Trackio — lightweight, local-first, free experiment tracking
- smolagents — Smol library to build great agents in Python
- LeRobot — Making AI for Robotics more accessible with end-to-end learning
- Reachy Mini — Open-source expressive robot SDK
- AutoTrain — AutoTrain API and UI for seamless model training
- Chat UI — Open source chat frontend powering HuggingChat
- Leaderboards — Create custom Leaderboards on Hugging Face
- Argilla — Collaboration tool for building high-quality datasets
- Distilabel — Framework for synthetic data generation and AI feedback
- Xet — Xet Protocol Specification

## smolagents — https://huggingface.co/docs/smolagents

smolagents is an open-source Python library for building and running agents in ~thousand lines of code.

Key features:
- Simplicity: minimal abstractions, ~1,000 lines of core logic
- CodeAgent: writes actions in Python code (nesting, loops, conditionals); secure sandboxed execution via Modal, Blaxel, E2B, or Docker
- ToolCallingAgent: standard JSON/text-based tool-calling
- Hub integrations: share and load agents and tools to/from the Hub as Gradio Spaces
- Model-agnostic: Hub via Inference providers, OpenAI, Anthropic, LiteLLM, Transformers, Ollama
- Modality-agnostic: text, vision, video, audio
- Tool-agnostic: MCP servers, LangChain tools, Hub Spaces
- CLI Tools: smolagent, webagent command-line utilities

Quickstart:
```python
from smolagents import CodeAgent, InferenceClientModel
model = InferenceClientModel()
agent = CodeAgent(tools=[], model=model)
result = agent.run("Calculate the sum of numbers from 1 to 10")
```

Adding tools:
```python
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=InferenceClientModel())
result = agent.run("What is the current weather in Paris?")
```

Model selection:
- InferenceClientModel(model_id="meta-llama/Llama-2-70b-chat-hf")
- LiteLLMModel(model_id="gpt-4")
- TransformersModel(model_id="meta-llama/Llama-2-7b-chat-hf")

GitHub: https://github.com/huggingface/smolagents

## Hub — https://huggingface.co/docs/hub

The Hugging Face Hub is the reference AI platform for open ML. Hosts 2M+ models, 1.5M+ datasets, and 1.5M+ AI apps (Spaces), all open and publicly available. Also a collaboration platform for private teams.

Content types:
- Models: state-of-the-art models for LLM, text, vision, and audio tasks; model cards, metadata, inference widgets
- Datasets: 500k+ public datasets in 8k+ languages; Dataset Cards, Data Studio browser viewer
- Spaces: ML demo apps hosted on Hub; supports Gradio, Streamlit, static HTML/CSS/JS, Docker; ZeroGPU provides NVIDIA RTX Pro 6000 Blackwell GPUs dynamically
- Storage Buckets: S3-like object storage powered by Xet backend for large-scale files without version control

Features: versioning, commit history, diffs, branches, 12+ library integrations, Xet storage (intelligent chunking), inference widgets, serverless Inference Providers API

Organizations: group accounts managing datasets, models, Spaces; role-based access control; Hugging Face for Classrooms

Security: User Access Tokens, organization access control, GPG commit signing, malware scanning

## Transformers — https://huggingface.co/docs/transformers

Transformers acts as the model-definition framework for state-of-the-art ML models in text, computer vision, audio, video, and multimodal tasks — for both inference and training.

Central to the ecosystem:
- Compatible with training frameworks: Axolotl, Unsloth, DeepSpeed, FSDP, PyTorch-Lightning
- Compatible with inference engines: vLLM, SGLang, TGI
- Compatible with modeling libraries: llama.cpp, mlx

1M+ Transformers model checkpoints on the Hub.

Key features:
- Pipeline: simple inference for text generation, image segmentation, ASR, document QA, and more
- Trainer: mixed precision, torch.compile, FlashAttention, distributed training for PyTorch
- generate: fast text generation for LLMs and VLMs with streaming and multiple decoding strategies

Design principles:
- Three-class implementation per model (configuration, model, preprocessor)
- Use pretrained models to reduce carbon footprint and compute cost

## TRL — https://huggingface.co/docs/trl

TRL (Transformers Reinforcement Learning) is a full-stack library for training transformer language models with post-training methods:
- Supervised Fine-Tuning (SFT)
- Group Relative Policy Optimization (GRPO, with vLLM support ⚡️)
- Direct Preference Optimization (DPO)
- Reward Modeling
- Integrated with 🤗 Transformers

TRL v1 (released March 27, 2026) marks a major shift in the library's scope and design.

Documentation sections: Getting Started, Conceptual Guides, How-to Guides, Integrations (DeepSpeed, Liger Kernel, PEFT), Examples, API

Notable integrations: DeepSpeed, Liger Kernel, PEFT, vLLM (co-located for efficiency)

Related learning: smol-course (GitHub: huggingface/smol-course) for post-training with TRL.

GitHub: https://github.com/huggingface/trl
