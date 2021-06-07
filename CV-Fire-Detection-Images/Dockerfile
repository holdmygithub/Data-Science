FROM python:3.8-slim-buster
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit","run","app.py","--server.port","$PORT"]
