# decrypt.co

## Fetch log
- Inbox URL: https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra
- Final URL: https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra
- Fetched: 2026-06-03
- Pages: 1
- Mode: standard

## Article — https://decrypt.co/369689/nvidia-open-ai-model-nemotron-3-ultra

Title: Nvidia Releases Its Best Open AI Model Yet—But Still Lags Behind China
Author: Jose Antonio Lanz
Published: 2026-06-01
Category: Artificial Intelligence

#### In brief

* NVIDIA unveiled Nemotron 3 Ultra at Computex on June 1, a 550-billion-parameter open-weight model.
* The model delivers over 300 tokens per second on a pre-release DeepInfra endpoint, running three to six times faster than Chinese rivals
* But Kimi K2.6 from Moonshot AI still leads the open-weight intelligence ranking.

Jensen Huang walked onto the Computex stage in Taipei on Sunday, leather jacket on, and unveiled Nemotron 3 Ultra—Nvidia's largest open AI model ever and, at least for now, the smartest open-weight model built in America. It's good. It's just not good enough to beat China.

The model packs roughly 550 billion total parameters but runs on only 55 billion active ones at any given moment, using a design called mixture-of-experts. Parameters are what determine an AI model's breadth of knowledge, with a greater number generally meaning more powerful.

To understand how a mixture-of-experts model works, think of it like a hospital with hundreds of specialists: When a patient comes in, only the relevant doctors actually show up—not everyone on staff. That approach keeps the cost of running the model far lower than its headline parameter count would suggest, which is exactly why Nvidia can claim 5x faster inference and costs 30% lower than comparable open-weight alternatives.

Independent evaluator Artificial Analysis, which partnered with Nvidia on the pre-release assessment, put Nemotron 3 Ultra at 48 on its Intelligence Index—a composite benchmark that aggregates 10 evaluations spanning reasoning, coding, general knowledge, and agentic performance, scored on a numbered scale where higher means smarter.

That makes it the top U.S. open-weight model by a comfortable margin. The next closest American options are Gemma 4 31B from Google at 39, Nemotron 3 Super at 36, and OpenAI's gpt-oss-120b at 33.

The gap over its own predecessor is striking. Nemotron 3 Super, released in March 2026 at 120 billion parameters, was already considered a solid open model for autonomous agents. Ultra jumps 12 index points above it, which in this benchmarking landscape is a big leap.

## What the Nemotron family is

Nvidia has been in the model business longer than most people realize. The first Nemotron-branded model dropped in November 2023, with the third generation announced in December 2025.

The family comes in three sizes: Nano for lightweight tasks, Super for mid-range enterprise applications, and Ultra for complex reasoning workloads. All three share the same hybrid architecture combining Mamba-2 layers, standard Transformer attention, and mixture-of-experts routing.

Mamba-2 is an alternative to standard attention that processes long sequences at a fraction of the cost—relevant when you want a model capable of holding a million tokens in memory at once. Nemotron 3 Ultra supports a 1-million-token context window, meaning an agent can, in theory, have an entire large codebase or hundreds of research documents in view simultaneously.

The Ultra model also includes a technique called multi-token prediction (MTP), which lets the model predict several future tokens at once rather than one at a time, speeding up generation. All three Nemotron 3 models were post-trained using reinforcement learning across multiple interactive environments, teaching them to plan and execute multi-step tasks rather than just answer questions.

The Ultra's weights are public and its training recipes are being released. Do you need a supercomputer to run it? Essentially, yes—a 550-billion-parameter model lives in datacenter territory. But you can access it through Nvidia's API or cloud providers without owning the hardware yourself, the same way anyone already uses GPT or Claude through a browser.

## Fast model, slower brain

The speed story is where Nemotron 3 Ultra genuinely stands out. On a pre-release DeepInfra endpoint, the model served over 300 output tokens per second. Chinese models in its intelligence class—DeepSeek V4 Pro and Kimi K2.6—are served at 50–100 tokens per second through their commercial APIs today. That speed gap matters for real-world deployments, particularly for autonomous agents executing long multi-step tasks where waiting for each step compounds quickly.

But raw speed doesn't settle the intelligence contest. The chart Artificial Analysis published tells the actual story plainly. On the vertical axis—intelligence—Nemotron 3 Ultra sits at 48 which is nice, but China's Kimi K2.6 from Moonshot AI sits at 54. That six-point gap on the index represents a meaningful difference: Kimi K2.6 was released in April 2026 and currently ranks fourth among all AI models globally, closed or open, sitting only three points behind Anthropic, Google, and OpenAI's proprietary flagships—all tied at 57.

The U.S. open-weight situation isn't new. Chinese labs have been flooding the open ecosystem with strong models while American companies—OpenAI, Anthropic, Google—keep their best systems behind APIs. As Decrypt reported in March, Chinese open-source models jumped from roughly 1.2% of global open-model usage in late 2024 to around 30% by end of 2025. Nvidia is the biggest American name actively trying to reverse that trend, with a publicly disclosed five-year plan to spend $26 billion on open-weight AI development.

Nemotron 3 Ultra is the most visible result of that bet so far. Nvidia also announced it is already working on Nemotron 4—the next generation—developed through the Nemotron Coalition, a group of eight AI labs including Mistral AI and Perplexity that Nvidia assembled in March 2026 to co-develop open frontier models on DGX Cloud infrastructure. Nemotron 3 Ultra ships June 4.
