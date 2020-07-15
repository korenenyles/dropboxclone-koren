from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

'''
__author__ = [
    mprodhan,
    https://stackoverflow.com/questions/58558989/what-does-djangos-property-do,
    https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
    ] += [MalikMAlna,
    Consider using this to login with the an email or a username,
    https://stackoverflow.com/questions/31370118/multiple-username-field-in-django-user-model
    ]
'''


class DropBoxUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not username:
            ValueError("Must register with a Username")
        if not email:
            ValueError("Must have a valid email address as username. \
                No Email address is also not valid.")
        if not password:
            ValueError("All users must have password to log in.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, email, username, password=None):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class DropBoxUser(AbstractBaseUser):
    '''
        To be added:
        email: as username
        display_name: name to appear as the handle name for the user
        active_user = BooleanField set to default=True
        staff = BooleanField set to default=False;
        only True when a user is added to staff
        admin = same conditions as staff
        created_at = DateTimeField set to auto_now or auto_now_add = True
        Adding the:
            USERNAME_FIELD = 'email'
            possible REQUIRED_FIELDS = []
        The functions for AbstractBaseUser include a display for display_name,
        perhaps email?;
        the functions for staff should include the
        @Property deocrator
        for privileges to set permissions
        for any user that is deemed as either staff or admin.
    '''
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(
        max_length=30, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = DropBoxUserManager()
    '''This wiil be the class name from the class above.'''

    def __str__(self):
        return self.username

    # function name subject to change
    def user_cred(self):
        return self.email

    @property
    def is_user_active(self):
        return self.is_active

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
