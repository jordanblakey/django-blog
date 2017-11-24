#!/bin/bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install -U pip
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
deactivate
yes | rm get-pip.py