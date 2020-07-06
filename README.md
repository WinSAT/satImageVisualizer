# satImageVisualizer
Visualize images from the WinSAT satellite

pip install --upgrade setuptools
pip install --upgrade pip

virtualenv venv

pip freeze > requirements.txt 
pip install -r requirements.txt

sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
sudo apt-get update
sudo apt-get install gdal-bin
sudo apt-get install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
pip install GDAL