## instance-deploymnet


# The project is to create EC2 instances and deploying nginx on the created instances using boto3


1. install RabbitMQ in the system 
```
sudo apt-get install rabbitmq-server
```

2. run celery worker using below cmd:
```
celery -A instance_deployment.celery worker -l INFO
```

3. run runserver
```
python3 manage.py runserver
```

*Endpoints*

Instance creation
http://127.0.0.1:8000/instances/api/create_instance/
POST request: body :
 ```
 {
    "instance_type": "t2.micro"
}
```

Get Instance State:
http://127.0.0.1:8000/instances/api/<str:instance_id>/
GET request: 
    response: 
    ```
    {
    "instance_id": "i-0b00bbf3719aaf691",
    "code": 16,
    "state": "running"
    }
    ```