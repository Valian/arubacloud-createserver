FROM python:2-alpine

ENV PROJECT_DIR /srv

COPY requirements.txt $PROJECT_DIR/requirements.txt
RUN pip install -r $PROJECT_DIR/requirements.txt
COPY entrypoint.py $PROJECT_DIR/entrypoint.py

ENTRYPOINT ["python", "/srv/entrypoint.py"]