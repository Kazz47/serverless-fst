#!/bin/bash
sudo yum update -y
sudo yum groupinstall "Development Tools" -y
mkdir install
wget http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.6.5.tar.gz
gunzip openfst-1.6.5.tar.gz
tar -xvf openfst-1.6.5.tar
cd openfst-1.6.5
./configure --enable-static=yes --enable-shared=no --prefix=$HOME/install/
make
make install
