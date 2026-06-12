# Base image eka widihata Python 3.9 use karanawa
FROM python:3.9-slim

# Container eka athule wada karana main folder eka
WORKDIR /app

# Requirements file eka copy karala packages install karanawa
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ape project files okkoma container ekata copy karanawa
COPY . .

# Container eka run weddi automatic execute wenda one command eka
CMD ["python", "src/main_pipeline.py"]