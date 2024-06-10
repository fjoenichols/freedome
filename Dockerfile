FROM python:3.11.9-alpine3.20

WORKDIR /app
COPY . /app

RUN rm -rf .git
RUN rm -rf .github
RUN rm -rf ansible
RUN rm -f Dockerfile
RUN rm -f .gitignore

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]