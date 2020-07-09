from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

'''
__author__ = [
    mprodhan,
    https://stackoverflow.com/questions/58558989/what-does-djangos-property-do,
    https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
    ]
'''
class DropBoxUserManager(BaseUserManager):
    def create_user(self, display_name, email, is_staff=False,
        is_admin=False, is_active=True, password=None):
        if not display_name:
            ValueError("Must register with a Display Name")
        if not email:
            ValueError("Must have a valid email address as username. \
                No Email address is also not valid.")
        if not password:
            ValueError("All users must have password to log in.")
        user_obj = self.model(
            email = self.normailize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active_user = is_active
        user_obj.display_name
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, display_name, password=None):
        user = self.create_user(email, display_name, password=password, is_staff=True)
        return user

    def create_superuser(self, email, display_name, password=None):
        user = self.create_user(email, display_name, password=password,
            is_staff=True, is_admin=True)
        return user


class DropBoxUser(AbstractBaseUser):
    '''
        To be added:
        email: as username
        display_name: name to appear as the handle name for the user
        active_user = BooleanField set to default=True
        staff = BooleanField set to default=False; only True when a user is added to staff
        admin = same conditions as staff
        created_at = DateTimeField set to auto_now or auto_now_add = True
        Adding the:
            USERNAME_FIELD = 'email'
            possible REQUIRED_FIELDS = []
        The functions for AbstractBaseUser include a display for display_name, perhaps email?;
        the functions for staff should include the @Property deocrator for privileges to set permissions
        for any user that is deemed as either staff or admin.
    '''
    email = models.EmailField(max_length=60, unique=True)
    display_name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    active_user = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    objects = DropBoxUserManager()
    '''This wiil be the class name from the class above.'''

    def __str__(self):
        return self.display_name

    def user_cred(self): #function name subject to change
        return self.email

    @property
    def is_active(self):
        return self.active_user

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


