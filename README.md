Django-AWS-Instance-Manager

A Django-based web application that automates the creation and management of Amazon EC2 instances for users upon registration. The app integrates with AWS services using boto3, enabling seamless scaling, instance lifecycle management, and user-specific instance configurations.

Features

    i. Automated EC2 Instance Creation: Automatically provides multiple EC2 instances for each new user during the registration process.

    ii. User-Specific Instance Management: Each user can have unique configurations (e.g., instance type, region, etc.).

    iii. Real-Time Instance Tracking: Monitor the status of EC2 instances (running, stopped, terminated).

    iv. Scalable: Easily scale the application to handle increasing users and EC2 instances using AWS Auto Scaling.

    v. Seamless Integration with AWS: Utilizes boto3 for AWS services integration, ensuring smooth communication with EC2 instances.

Installation

Prerequisites

    i. Python 3.x

    ii. Django 3.x or later

    iii. AWS account and IAM credentials with EC2 access

    iv. boto3 library for AWS integration

Step-by-Step Installation

    i. Clone the Repository:
            git clone git@github.com:Stephen842/Django-AWS-Instances.git
            cd Django-AWS-Instances

    ii. Set Up a Virtual Environment:
            python3 -m venv venv
            source venv/bin/activate  # On Windows, use venv\Scripts\activate

    iii. Install Dependencies:
            pip install -r requirements.txt

    iv. Configure AWS Credentials:
            a. Ensure you have AWS credentials (Access Key ID and Secret Access Key).
            b. You can set up AWS credentials by running the following command:
                aws configure

    v. Migrate Database:
            python manage.py migrate

    vi. Run the Development Server:
            python manage.py runserver

Usage

i. User Registration:
        When a new user registers on the platform, the system automatically creates one or more EC2 instances for that user.

ii. Instance Management:
        Users can view the status and configurations of their EC2 instances through their dashboard.

iii. Monitoring:
        Admins can monitor the health and status of all instances in the admin panel.

iv. Instance Lifecycle:
        Users can start, stop, or terminate their instances based on their needs, and these changes are reflected in the app.

Configuration

Instance Configuration Options

    i. Instance Type: Select the instance type (e.g., t2.micro, t2.medium) when the user registers.

    ii. Region: Choose the AWS region where the instances should be launched (e.g., us-east-1, eu-west-1).

    iii. Security Groups: Define the security groups for each instance (e.g., HTTP, SSH access).

Admin Panel

The admin panel allows you to:

    i. View all EC2 instances for each user.

    ii. Start/Stop/Terminate instances.

    iii. Manage User-specific Configurations (instance types, regions, etc.).

Technologies Used

    i.  Django: Python web framework for building the backend.

    ii. boto3: AWS SDK for Python, used to interact with AWS EC2 services.

    iii. AWS EC2: Cloud computing instances used to scale based on user needs.

    iv. SQLite3 (or your preferred database): For storing user data and EC2 instance metadata.

    v. Celery (optional): For handling background tasks such as instance creation or deletion asynchronously.

Contributing

We welcome contributions! If you'd like to improve or add features to the project, please fork the repository and submit a pull request. Here's how you can contribute:

    i. Fork the repository

    ii. Create a new branch for your feature (git checkout -b feature-name)

    iii. Make your changes

    iv. Commit your changes (git commit -m 'Add new feature')

    v. Push to your branch (git push origin feature-name)

    vi. Open a pull request

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

    i. boto3: For making AWS services accessible from Python.

    ii. Django: For providing a robust framework to build this web application.

    iii. AWS: For providing scalable cloud solutions.