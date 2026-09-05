---
title: "deepke-mcp-tools"
description: "MCP service for the prediction part of DeepKE's four NLP tasks (standard version). Requires the DeepKE toolkit (https://github.com/zjunlp/DeepKE) to be installed."
---

# deepke-mcp-tools

MCP service for the prediction part of DeepKE's four NLP tasks (standard version). Requires the DeepKE toolkit (https://github.com/zjunlp/DeepKE) to be installed.

# DeepKE-mcp-tools

This is the **standard** **prediction** part of the mcp service for the four natural language processing tasks in `DeepKE`. Therefore, it is necessary to have a [DeepKE](https://github.com/zjunlp/DeepKE) model trained for the corresponding task, ensuring that the corresponding `predict.py` can run.

## Download the Code

bash
cd DeepKE
git clone https://github.com/Shotsuke/deepke-mcp-tools.git

## Configure `.env` Environment Variables

- Set up the deepke / deepke-ee virtual environment.
- If the environment has already been set up during model training, this section can be skipped.

bash
cd DeepKE
conda create -n deepke python=3.8 -y
conda activate deepke

pip install pip==24.0.0 # Requires pip<=24.0
pip install -r requirements.txt
pip install -U transformers==4.36.2 # Some libraries specify `transformers == 3.4.0`, but it actually doesn't work

# `requirements.txt` does not check `torch` and `cuda` versions, so you need to manually check them
# conda list | grep "torch"
# nvidia-smi
# Choose the appropriate version to download based on the `nvidia` compatible `cuda` from ([Start Locally | PyTorch](https://pytorch.org/get-started/locally/)), for example:
pip install torch==2.4.1
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

python setup.py install
python setup.py develop

After setting up deepke, configure deepke-ee, which is essentially the same, but with an additional `pip install hydra-core==1.3.1` as the `EE` task uses a higher version of `hydra`.

Add the `conda` directory containing `PY` and the `DeepKE` directory to the `.env` file, for example:

DEEPKE_PATH="~/DeepKE"
CONDA_PY="/home/user_name/anaconda3/envs/deepke/bin/"
CONDA_EE_PY="/home/user_name/anaconda3/envs/deepke-ee/bin/"

- API_KEY

The project uses Alibaba's Qwen large model. You can change `DASHSCOPE_API_KEY` accordingly.

## Configure the MCP Project UV Environment

bash
# curl -LsSf https://astral.sh/uv/install.sh | sh # Install uv
# pipx install uv # Choose one method to install uv
pip install uv

# Now in: DeepKE/
cd deepke-mcp-tools
uv venv
source .venv/bin/activate
uv add "mcp[cli]" httpx openai pyyaml

## Run

bash
# Now in: DeepKE/deepke-mcp-tools/
python run.py

**Official site: ** [https://github.com/Shotsuke/deepke-mcp-tools](https://github.com/Shotsuke/deepke-mcp-tools)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory absolute/path/to/DeepKE/deepke-mcp-tools/tools run server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/openkg-deepke-tools.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
