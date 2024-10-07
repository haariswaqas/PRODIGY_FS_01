from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    username = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        profile = Profile.objects.get(user=self)
    
    def __str__(self):
        return self.username



from datetime import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100, null=True, blank=True)
    middle_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length = 100, null=True, blank=True)
    bio = models.TextField(null=True, blank = True)
    image = models.ImageField(null=True, blank=True, upload_to="user_images")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)





class Lecturer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 3)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank = True)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(default = 'This is me')
   



    def __str__(self):
        return f'{self.title} {self.first_name} {self.last_name}'

    # def save(self, *args, **kwargs):
    #     try:
    #         dob = datetime.strptime(str(self.date_of_birth), '%Y-%m-%d').date()
    #         today = datetime.now().date()
    #         age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    #         self.age = age
    #     except (ValueError, TypeError):
    #         self.age = None

    #     if self.middle_name and len(self.middle_name) > 0:
    #         middle_initial = self.middle_name[0].lower()
    #     else:
    #         middle_initial = ''

    #     self.email = f'{self.first_name[0].lower()}{middle_initial}.{self.last_name.lower()}{str(self.lecturer_id)[5:8]}@lect.ug.edu.gh'
    #     super(Lecturer, self).save(*args, **kwargs)



class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length = 14)
    title = models.CharField(max_length = 1000)
    description = models.TextField(null=True, blank=True)
    credits = models.IntegerField(default = 3)
    type = models.CharField(max_length=20, default='Core')
    level = models.CharField(max_length = 12, default = '300')
    semester = models.CharField(max_length=6, default = '1')
    department = models.CharField(max_length = 200, default = 'CPEN')
    lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE)


    def __str__(self):
        return f'{self.code} - {self.title}'

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, default = 1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    week = models.CharField(max_length = 100, default = 'Week 1', null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course.code}, Lecture {self.week} - {self.title}'
