# coding-llms-from-the-ground-up

## Fetch log
- Inbox URL: https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up
- Final URL: https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up
- Fetched: 2026-11-04
- Pages: 1
- Mode: single-page
- Note: Substack magazine article at /p/<slug>; treated as single-page article capture (path-derived slug) to avoid colliding with sibling posts on magazine.sebastianraschka.com. llms.txt absent (404). Docs discovery skipped. Companion GitHub discovered from article body: rasbt/LLMs-from-scratch. Some lecture videos may be paywalled on Substack.

## Landing page — https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up

Title: Coding LLMs from the Ground Up: A Complete Course

URL Source: https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up

Published Time: 2025-05-10T11:03:17+00:00

Markdown Content:
I wrote a lot about reasoning models in recent months (4 articles in a row)! Next to everything "agentic," reasoning is one of the biggest LLM topics of 2025.

This month, however, I wanted to share more fundamental or "foundational" content with you on how to code LLMs, which is one of the best ways to understand how LLMs work.

Why? Many people really liked and benefited from the abbreviated LLM workshop I shared last year:

So, I thought this ~5× longer and more detailed content (~15 hours in total) would be even more useful.

Also, I'm sadly dealing with a bad neck injury and haven't really been able to work on a computer for the past 3 weeks. I am currently trying a conservative treatment before considering the suggested surgical route. This is the worst timing as I just started to get back on track before life threw another curveball.

So, during my recovery, I thought sharing these videos I recorded in the last couple of months would be a nice in-between content.

I hope you find this useful, and thanks for your support!

_PS: The videos originally started as supplementary content for my [Build a Large Language Model (From Scratch) book](https://amzn.to/4fqvn0D). But it turns out they also work pretty well as standalone content._

**Why build from scratch?**

It's probably the best and most efficient way to learn how LLMs really work. Plus, many readers have told me they had a lot of fun doing it.

To offer an analogy: if you are into cars and want to understand how they work, following a tutorial that walks you through building one from the ground up is a great way to learn. Of course, we probably wouldn't want to start by building a Formula 1 race car since it would be prohibitively expensive and overly complex for a first project. Instead, it makes more sense to start with something simpler, like a go-kart.

Building a go-kart still teaches you how the steering works, how the motor functions, and more. You can even take it to the track and practice (and have a lot of fun with it) before stepping into a professional race car (or joining a company or team that is focused on building one). After all, the best race drivers often got their start by building and tinkering with their own go-karts (think Michael Schumacher and Ayrton Senna). By doing that, they not only developed a great feel for the car but could also provide valuable feedback to their mechanics, which gave them an edge over the other drivers.

1.   Build an LLM from Scratch book ([Manning](https://mng.bz/M96o) | [Amazon](https://amzn.to/4fqvn0D))

2.   [Build an LLM from Scratch GitHub repository](https://github.com/rasbt/LLMs-from-scratch)

This is a supplementary video explaining how to set up a Python environment using uv.

In particular, we are using “`uv pip”`, which is explained in [this document](https://github.com/rasbt/LLMs-from-scratch/blob/main/setup/01_optional-python-setup-preferences/README.md).

Alternatively, the native “`uv add”` syntax (mentioned but not explicitly covered in this video) is described [here](https://github.com/rasbt/LLMs-from-scratch/blob/main/setup/01_optional-python-setup-preferences/native-uv.md).

[Video 15](https://www.youtube.com/watch?v=yAcWnfsZhzo)

**Note / Tip:** The installation may cause issues on certain versions of Windows. If you are on a Windows machine and have troubles with the installation (likely due to a TensorFlow dependency to load the original GPT-2 model weights from OpenAI in video 5), please don’t worry about it and feel free to skip the TensorFlow installation (you can do this by removing the TensorFlow line from the requirements file.)

To provide an alternative, I converted the GPT-2 model weights from a TensorFlow tensor format to PyTorch tensors and shared them on the Hugging Face model hub, which you can use as an alternative to the weight loading portion in video 5: [https://huggingface.co/rasbt/gpt2-from-scratch-pytorch](https://huggingface.co/rasbt/gpt2-from-scratch-pytorch).

In any case, you don’t have to worry about this weight-loading code until the end of video 5.

This video goes over text data preparations steps (tokenization, byte pair encoding, data loaders, etc.) for LLM training.

[Video 16](https://www.youtube.com/watch?v=341Rb8fJxY0)

This is a supplementary video explaining how attention mechanisms (self-attention, causal attention, multi-head attention) work by coding them from scratch.   
You can think of it as building the engine of a car (before adding the frame, seats, and wheels).

[Video 17](https://www.youtube.com/watch?v=-Ll8DtpNtvk)

This video covers how to code an LLM architecture from scratch.

[Video 18](https://www.youtube.com/watch?v=YSAkgEarBGE)

This video explains how to pretrain a LLM from scratch.

[Video 19](https://www.youtube.com/watch?v=Zar2TJv-sE0)

This is a video explaining how to fine-tune an LLM as a classifier (here using a spam classification example) as a gentle introduction to finetuning, before instruction finetuning the LLM in the next video.

[Video 20](https://www.youtube.com/watch?v=5PFXJYme4ik)

Finally, this video explains how to instruction finetune the LLM.

[Video 21](https://www.youtube.com/watch?v=4yNswvhPWCQ)

**Happy viewing & tinkering!**

As a big thank you to the paid subscribers, I want to share a 2.5h (non-coding) bonus video I recorded earlier in April, approximately 2 days after the Llama 4 release. In this talk, I discuss the current LLM landscape in 2025 with a focus on what and how things have changed since GPT-2 in 2018.

Thanks for your support, as an independent and self-employed researcher, this really means a lot to me!

Hopefully, things will improve in the next few weeks/months as I have lots of ideas for upcoming articles and can’t wait to work on them!



## Article outline (structured capture)

# Coding LLMs from the Ground Up: A Complete Course
Author: Sebastian Raschka, PhD · Published: 2025-05-10 · Ahead of AI (Substack magazine)

### Pitch
~15 hours of coding videos as supplementary content for *Build a Large Language Model (From Scratch)*; also works standalone. Follows an earlier ~3-hour workshop ("Building LLMs from the Ground Up").

### Why build from scratch
Pedagogy analogy: build a go-kart before a Formula 1 car — learn steering/motor fundamentals by implementing them.

### References
1. Build an LLM from Scratch book (Manning | Amazon)
2. Build an LLM from Scratch GitHub repository: https://github.com/rasbt/LLMs-from-scratch

### Videos
1. Set up your code environment (0:21:01) — uv / `uv pip`; Windows TensorFlow tip; Hugging Face GPT-2 PyTorch weights alternative https://huggingface.co/rasbt/gpt2-from-scratch-pytorch
2. Working with text data (1:28:01) — tokenization, BPE, data loaders
3. Coding attention mechanisms (2:15:40) — self-attention, causal attention, multi-head attention
4. Coding an LLM architecture (note: page labeling may show duplicate "Set up" numbering in some renders; content is the GPT architecture chapter) — implementing the model from scratch
5. Pretraining on Unlabeled Data (2:36:44)
6. Finetuning for Classification (2:15:29) — spam classifier intro to finetuning
7. Instruction Finetuning (1:46:04)

### Bonus (paid subscribers)
LLMs Then And Now (From 2018 to 2025) — ~2.5h non-coding landscape talk recorded after Llama 4 release.

