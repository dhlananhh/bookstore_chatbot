# base image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
# COPY . .
COPY app/ app/
COPY static/ static/
COPY README.md .

# expose port
EXPOSE 8000

# run command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
