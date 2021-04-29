# set the base image
FROM python:3.9


#add project files to the usr/src/app folder
ADD . /app

#set directoty where CMD will execute
WORKDIR /app

COPY requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8004

# default command to execute
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]