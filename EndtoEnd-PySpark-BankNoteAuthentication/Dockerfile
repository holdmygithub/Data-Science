FROM ykursadkaya/pyspark:latest 
RUN mkdir -p /app
WORKDIR /app
COPY . .
EXPOSE 8888 5000 8000 8501
RUN pip install flasgger flask numpy streamlit
ENTRYPOINT ["streamlit","run","deploy.py"]

