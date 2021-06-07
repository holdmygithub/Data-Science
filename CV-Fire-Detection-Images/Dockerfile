FROM python:3.8-slim-buster
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run","app.py"]
