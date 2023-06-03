FROM python:3.10-alpine

COPY api/ /api

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "api.main:app", "--host", "0.0.0.0" ]
