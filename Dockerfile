FROM python:3.8

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
#ENV MYSQL_DATABASE=<YOUR_DATABASE_NAME>
#ENV MYSQL_USER=<YOUR_USERNAME>
#ENV MYSQL_PASSWORD=<YOUR_PASSWORD>
#ENV MYSQL_HOST=<YOUR_HOST>
#ENV MYSQL_PORT=<YOUR_PORT>

# Create and set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 80
EXPOSE 80

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]