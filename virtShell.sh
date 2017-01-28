#!/bin/bash
# VERY VERY simple wrapper around getting your virtual shell running.
virtualenv --no-site-packages ./venv
source ./venv/bin/activate
pip install -r requirements.txt
