FROM python:3.12-slim
ENV PORT=8080
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
# Документация - на каком порту запускаем:
EXPOSE 8080 
CMD ["python", "app.py"]