source deactivate
conda env remove -y -n foobar
conda create -y -n foobar python=3.4
source activate foobar
rm -rf src
