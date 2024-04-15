# sdxs-cli

Requirement: Python 3.9

Create <b>conda</b> environment:
```shell
conda create -n venv python=3.9
conda activate venv
...
conda deactivate
```
OR create venv:
```bash
python3 -m venv venv
source venv/bin/activate # macOS and Linux 
.\venv\Scripts\activate # Windows
...
deactivate
```
Install dependencies:
```shell
pip install -r requirements.txt
```

Run CLI:
```shell
python app.py --prompt "a realistic sunset"
```
```
Params:
    --prompt     # prompt string
    --large_vae  # (optional) not exist by default, takes 4 times longer
```

[Model](https://huggingface.co/IDKiro/sdxs-512-dreamshaper) ~2Gb
