# satImageVisualizer
Visualize images from the WinSAT satellite

https://earthexplorer.usgs.gov/

#update pip requirements txt
pip freeze > requirements.txt 

#setup
pip install --upgrade setuptools
pip install --upgrade pip

virtualenv venv
source venv/bin/activate

sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
sudo apt-get update
sudo apt-get install gdal-bin
sudo apt-get install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
pip install GDAL


pip install -r requirements.txt