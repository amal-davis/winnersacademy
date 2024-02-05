from django.db import models

# Create your models here.



class SwiperContent(models.Model):
    image = models.ImageField(upload_to='swiper_images/')
   
    


class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.heading
    


    


class Portfolio_content(models.Model):
    video_url = models.URLField(blank=True, null=True)
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()

    def __str__(self):
        return self.heading
    
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Contact_US(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    message = models.TextField()

class Team(models.Model):
    image = models.ImageField(upload_to='team_images/')
    heading = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255,default='')
    description = models.TextField()

    def __str__(self):
        return self.heading
    
class Online_admission(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonno = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)


class Add_student_corner(models.Model):
      image = models.ImageField(upload_to='team_images/')


class careers(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes',default='default_pdf.pdf')
    qualafication = models.CharField(max_length=255,default='')
    dob = models.CharField(max_length=255,default='')



class Syllabus(models.Model):
    name = models.CharField(max_length=255)
    sylabbus_pdf = models.FileField(upload_to='resumes',default='default_pdf.pdf')


class courses(models.Model):
      image = models.ImageField(upload_to='team_images/')
      name = models.CharField(max_length=255)
      url = models.URLField(blank=True, null=True)
    

