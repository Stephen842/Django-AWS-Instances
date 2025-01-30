from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Create your models here.

class User_Manager(BaseUserManager):
    def create_user(self, email, name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
        )
        user.set_password(password)  # To Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password=None):
        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin): 
    name = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Fixing the group and permission conflicts
    groups = models.ManyToManyField(Group, related_name="my_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="my_user_permissions", blank=True)

    objects = User_Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.email


# Model to track EC2 instances in the database
class EC2Instance(models.Model):
    # The user field link the EC2 instance to a registered user in the app
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    # 'instance_id' is a unique identifier for the EC2 instance
    instance_id = models.CharField(max_length=255)

    # 'instance_type' stores the type of EC2 instance
    instance_type = models.CharField(max_length=255)

    # 'state' stores the current state of the EC2 instance whether it is running or it have stopped
    state = models.CharField(max_length=50)

    # 'ip_address' will store the public IP address of the EC2 instance, if assigned
    ip_address = models.CharField(max_length=255, null=True, blank=True)

    # 'created_at' stores the time when the EC2 instance was created
    created_at = models.DateTimeField(auto_now=True)

    # 'updated_at' stores the time when the Ec2 instance was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # The __str__ method returns a human readable string representation of the object
    def __str__(self):
        return f'EC2 instance {self.instance_id} for {self.user.username}' 