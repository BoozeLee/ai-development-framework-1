# NeoSpiral AI Tools Usage Guide

## Quick Start

### Activate AI Environment

source ~/ai-development/environments/ai-main/bin/activate

### Launch Menu System

~/ai-development/neospiral-menu.sh

## Individual Tool Usage

### 1. OpenCode (Terminal AI Assistant)
**Purpose**: Terminal-native AI coding assistant
**Usage**:

cd ~/ai-development
opencode
**Features**:
- Multi-model support (OpenAI, Anthropic, Ollama)
- Session management
- Direct file editing
- Command execution with permission control

### 2. Cursor IDE (AI-Powered Code Editor)
**Purpose**: VSCode-based editor with AI features
**Usage**:

cursor ~/ai-development
Or launch from desktop applications menu
**Features**:
- Inline AI suggestions (Ctrl+K)
- AI chat panel (Ctrl+L)
- Multi-line autocomplete
- Codebase understanding

### 3. Aider (AI Pair Programmer)
**Purpose**: Direct file editing AI assistant
**Usage**:

cd ~/ai-development
source environments/ai-main/bin/activate
aider
**Features**:
- Direct code modification
- Git integration
- Multi-file editing
- Test generation

### 4. Ollama (Local LLMs)
**Purpose**: Run large language models locally
**Usage**:

ollama run codellama:7b
ollama run deepseek-coder:6.7b
**API Usage**:
curl -X POST http://localhost:11434/api/generate
-H "Content-Type: application/json"
-d '{"model":"codellama:7b","prompt":"Your question"}'

### 5. Mathematical Tools

#### Shannon Entropy Analysis

python ~/ai-development/tools/shannon_entropy.py

#### STDP Learning Simulation

python ~/ai-development/tools/stdp_learning.py

#### Spiral Network Analysis

python ~/ai-development/tools/spiral_network.py

## Environment Management

### Main AI Environment

source ~/ai-development/environments/ai-main/bin/activate
**Contains**: gpt4all, transformers, torch, jupyterlab

### Neuromorphic Environment

source ~/ai-development/environments/neuromorphic/bin/activate
**Contains**: brian2, snntorch, nengo, qiskit, pennylane

### Research Environment

source ~/ai-development/environments/research/bin/activate
**Contains**: datasets, arxiv, scholarly, opencv, spacy

## GitHub Integration

### Clone Repository

gh repo clone username/repo-name

### Create New Repository


### Authentication Status


### Authentication Status

gh auth status

## Configuration Files

### OpenCode Config
Location: `~/.config/opencode/opencode.json`

### Environment Variables
Add to `~/.bashrc`:

export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"
export PPLX_API_KEY="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"

## Troubleshooting

### Common Issues
1. **Python path errors**: Always activate virtual environment first
2. **Cursor not found**: Reinstall using the provided script
3. **OpenCode directory error**: Ensure you're in `~/ai-development`
4. **GitHub auth**: Use `gh auth login` with personal access token

### Support Resources
- OpenCode docs: https://opencode.ai/docs/
- Cursor support: Built-in help system
- Aider docs: https://aider.chat/docs/
- Ollama docs: https://ollama.ai/docs/
