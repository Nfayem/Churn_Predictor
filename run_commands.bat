@echo off
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r LP4_STAPP_v_Requirements.txt