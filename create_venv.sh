#!/bin/bash

# this installs the virtualenv module
python3.7 -m pip install virtualenv

# this cd to your root directory and install a virtual environment named baccpack_tts
cd
python3.7 -m venv baccpack_tts
dir=$(pwd)
# activate the created virtual environment 
source baccpack_tts/bin/activate
# go back to the previous directory
cd -
# and copy requirements.txt to the venv directory
cp requirements.txt ~/baccpack_tts/.
# and then cd back to the venv
cd $dir/baccpack_tts/
# and then the real pip here is the bin/pip
pip_env=$dir/baccpack_tts/bin/pip
python_env=$dir/baccpack_tts/bin/python3
# update pip
$pip_env install -U pip
# then write to ~/.bashrc and ~/.bash_profile that baccpack_tts from now on is to activate the
# virtual environment
echo "alias baccpack_tts='source ~/baccpack_tts/bin/activate'" >> ~/.bashrc
echo "alias baccpack_tts='source ~/baccpack_tts/bin/activate'" >> ~/.bash_profile
source ~/.bashrc
source ~/.bash_profile
# and install the required python packages to the virtual environment
for line in $(cat requirements.txt)
do
    $python_env -m pip install $line
done

echo created gym environment
# now go back to the previous directory
cd -
