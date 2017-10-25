FROM ubuntu:xenial

#############################

## Environnement Variables ##

#############################

## set environment variables
ENV SHELL /bin/bash

###################################

##Python data science libraries ##

###################################

## install python3.5
RUN sed -i 's/archive.ubuntu.com/mirror.us.leaseweb.net/' /etc/apt/sources.list \
      && sed -i 's/deb-src/#deb-src/' /etc/apt/sources.list \
      && apt-get update \
      && apt-get upgrade -y \
      && apt-get install -y \
      aria2 \
      build-essential \
      ca-certificates \
      python-pip \
      python3-pip \
      python3.5 \
      python3.5-dev \
      && apt-get autoremove -y \
      && apt-get clean

## make some useful symlinks that are expected to exist
      RUN cd /usr/local/bin \
        && ln -s idle3 idle \
        && ln -s pydoc3 pydoc \
        && ln -s python3 python \
        && ln -s python3-config python-config

        RUN pip3 install \
          beautifulsoup4 \
          bokeh \
          jupyter \
          jupyterhub \
          jupyterlab \
          matplotlib \
          nltk \
          notebook \
          numpy \
          pandas \
          pyzmq \
          requests \
          scikit-image \
          scikit-learn \
          scipy \
          seaborn \
          sqlalchemy \
          statsmodels \
          sympy \
          textblob


