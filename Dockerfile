FROM --platform=linux/amd64 python

# Copy the current directory contents into the container at /app
COPY ./app.py .

# Install the dependencies
RUN pip install Flask

# Set the entrypoint
CMD ["python", "app.py"]
