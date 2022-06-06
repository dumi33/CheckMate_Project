#./Dockerfile 
FROM python:3.9.7                            
WORKDIR /app                     

## Install packages               
RUN pip install -r requirements.txt  

## Copy all src files 
COPY . /app


ENTRYPOINT ["flask"]


## Run the application on the port 8080 
#EXPOSE 8080                              

#CMD ["python", "./setup.py", "runserver", "--host=0.0.0.0", "-p 8080"] 
#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "example.wsgi:application"]  
#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["run", "--host", "0.0.0.0"]



