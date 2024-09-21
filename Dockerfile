FROM python:3.9

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
