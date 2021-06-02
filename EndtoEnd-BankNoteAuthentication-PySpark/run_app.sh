#!/bin/bash
( sudo docker start --attach banknotecont ) || (( sudo docker run -p 8501:8501 --name banknotecont banknote ) || ((( echo "Building docker image" ) && ( sudo docker build -t banknote . )) && ( sudo docker run -p 8501:8501 --name banknotecont banknote )))
