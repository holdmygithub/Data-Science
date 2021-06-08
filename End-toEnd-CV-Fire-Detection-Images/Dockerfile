FROM python:3.8-slim-buster
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
RUN sh setup.sh
CMD ["streamlit","run","app.py"]

