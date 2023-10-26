# Use the official Python image as the base image
FROM python:3.10

# Copy the .env file
COPY .env .env

# Copy the rest of the application code
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Execute the script when the container starts
ENTRYPOINT ["chainlit", "run", "app.py", "--host=0.0.0.0", "--port=80", "--headless"]
