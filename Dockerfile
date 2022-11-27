FROM python:3.11 
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install mysqlclient flask flask-mysqldb
CMD [ "python","app.py" ]