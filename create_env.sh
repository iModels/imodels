source deactivate
conda env remove -y -n imodels
conda create -y -n imodels python=3.4
source activate imodels
rm -r src
