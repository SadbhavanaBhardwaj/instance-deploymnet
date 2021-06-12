import boto3
import botocore
import paramiko
import time
 
from instance.configurations import *
 
def run_commands(instance_id):
   ec2_client = boto3.resource("ec2", region_name=region_name)
   res = ec2_client.instances.filter(Filters=[{
       "Name": "instance-id",
       "Values": [instance_id]
   }])
   for instance in res:
       instance.wait_until_running()
       print("after waiting")
       instance.load()
       print(instance.public_ip_address)
       hostname = instance.public_ip_address
 
       key = paramiko.RSAKey.from_private_key_file(KEY_PATH)
       client = paramiko.SSHClient()
       client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       cmds = commands
      
       time.sleep(20)
       try:
           # Here 'ubuntu' is user name and 'hostname' is public IP of EC2
           client.connect(hostname=hostname, username="ubuntu", pkey=key)
 
           for cmd in cmds:
               stdin, stdout, stderr = client.exec_command(cmd)
               print(stdout.read())
               print(stderr.read())
               print("------")
 
           # close the client connection once the job is done
           client.close()
 
       except Exception as e:
           print(e)
 
def create_deploy_instance(instance_type):
   from instance_deployment.celery import run_commands_task
 
   ec2_res = boto3.resource('ec2', region_name=region_name)
   print("b4 creation")
   instances = ec2_res.create_instances(
       ImageId = 'ami-0c1a7f89451184c8b',
       MinCount = 1,
       MaxCount = 1,
       InstanceType = instance_type,
       KeyName = 'sadbhavana_key1',
       BlockDeviceMappings = [
               {
                   'DeviceName': "/dev/xvda",
                   'Ebs': {
                       'DeleteOnTermination': True,
                       'VolumeSize': 8
                   }
               }
           ],
       SecurityGroups = ['launch-wizard-19']
       )
   print("after creation")
   instance = instances[0].instance_id
   run_commands_task.delay(instance)
   return(instance)
  
 
 
 
def get_instance_state(instance_id):
   ec2_client = boto3.client("ec2", region_name=region_name)
   state = ec2_client.describe_instance_status(
       InstanceIds=[
           instance_id,
       ],
       IncludeAllInstances=True
   )
   print(state)
   return state['InstanceStatuses'][0]['InstanceState']
