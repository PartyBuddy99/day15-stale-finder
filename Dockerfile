FROM python:3.10-slim
RUN pip install boto3
WORKDIR /app
COPY day15.py .
COPY config.json .
CMD ["python", "day15.py", "5"]