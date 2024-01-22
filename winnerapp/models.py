from django.db import models

# Create your models here.



class SwiperContent(models.Model):
    image = models.ImageField(upload_to='swiper_images/')
    online_class_url = models.URLField()
    offline_class_url = models.URLField()



class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.heading
    

class Course(models.Model):
    image = models.ImageField(upload_to='course_images/')
    url = models.URLField()

    def __str__(self):
        return f"Course {self.id}"
    


class Portfolio_content(models.Model):
    image = models.ImageField(upload_to='swiper_images/')
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