#!/bin/bash
source ~/ai-development/environments/ai-main/bin/activate
export OPENAI_API_KEY="${OPENAI_API_KEY:-}"
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY:-}"
export PPLX_API_KEY="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"
echo "🧠 NeoSpiral AI environment activated"
echo "📍 Working directory: $(pwd)"
echo "🛠️  Available tools: ollama, opencode, aider, gpt4all"
echo "📊 Mathematical tools: shannon_entropy.py, stdp_learning.py, spiral_network.py"
