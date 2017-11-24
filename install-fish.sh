curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install -U pip
pip install virtualenv
virtualenv env
source env/bin/activate.fish
pip install -r requirements.txt
rm get-pip.py