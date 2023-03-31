from django.db import models
import datetime, os


#superuse: devraj445

# Create your models here.




def get_image(instance, filename):
    old_name =filename
    current_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s'%(current_time, old_name)
    return os.path.join('static/media/b_pics', filename)

class Contact(models.Model):
    fname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.fname

class Blog(models.Model):
    b_head = models.CharField(max_length = 40)
    b_body = models.TextField()
    date = models.DateField()
    image  = models.ImageField(upload_to=get_image, null=True, blank = True)
    def __str__(self):
        return self.b_head
