FROM python:3.10-slim

# Specify working directory for next commands
WORKDIR /root

# Copy necessary files
#COPY src /root/src
COPY train.py /root/train.py
COPY requirements.txt /root/requirements.txt

# Create env/install dependencies
RUN pip install -r /root/requirements.txt

# Set up entry point
ENTRYPOINT ["python", "train.py"]
