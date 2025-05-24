# Official Python Image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copies application code to the container
COPY . /app

# Links the code to the image in GitHub
LABEL org.opencontainers.image.source https://github.com/ewsmyth/monsys

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposes port
EXPOSE 7337

# Command to run server
CMD ["python", "monsys.py"]
