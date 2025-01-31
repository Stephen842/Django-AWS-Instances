from celery import shared_task # Import shared_task decorator to define Celery tasks
import boto3 # AWS SDK for python to interact with AWS services
from .models import EC2Instance

# This is the Celery task that will be triggered to create an EC2 instance
@shared_task
def create_ec2_instance(user_id):
    # Initialize a boto3 client to interact with AWS EC2 service
    ec2 = boto3.client('ec2', region_name='us-east-1') # Replace with your AWS region

    # Launch a new EC2 instance using specific parameters like AMI ID, instance type, etc
    response = ec2.run_instances(
        ImageId = 'ami-XXXXXXXXXXXX', # Insert your desired AMI ID(Amazon Machine Image)
        InstanceType = 't2.micro', # Instance Type
        MinCount = 1, # Minimum number of instances to launch
        MaxCount = 1, # Maximum number of instances to launch
        KeyName = 'My-Key-pair', # AWS key pair for SSH access(replace with your key pair name)
        SecurityGroupIds = ['sg-xxxxxxx'], # Security group ID(replace with your Security group ID)
    )

    # Get the details of the created instance from the response
    instance = response['instances'][0] # We expect one instance to be created, so we are getting the first one
    instance_id = instance['instanceId'] # Extract the instance ID
    state = instance['State']['Name'] # Extract the current state, e.g running or stopped, etc

    # Save the EC2 instance details to the database
    ec2_instance = EC2Instance.objects.create(
        user_id = user_id, # Link the EC2 instance to the user who triggered the task
        instance_id = instance_id, # Save the instance ID
        instance_type = 't2.micro', # Save the instance type
        state = state # Save the instance state
    )

    # Return a success message with the EC2 instance details
    return f'EC2 instance {instance_id} created for the user {user_id}'