FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install Flask psycopg2-binary requests
EXPOSE 5000
CMD ["python", "app.py"]