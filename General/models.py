from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=30)
    username  = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    mail = models.EmailField()
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    pro_pic = models.FileField(default='default.jpg')

    def __str__(self):
        return self.name

class Softwares(models.Model):
    own_by = models.ForeignKey(Users,on_delete = models.CASCADE )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    requirements = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    download =models.IntegerField(default=0)
    cover_pic = models.FileField(default='software-icon-30.png', blank=True)
    zip_file = models.FileField()

    def __str__(self):
        return self.name

class Downloads(models.Model):
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    soft = models.ForeignKey(Softwares,on_delete= models.CASCADE)

    def _str_(self):
        return self.soft.name+self.user.name

class Bookmarks(models.Model):
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    soft = models.ForeignKey(Softwares,on_delete= models.CASCADE)

    def _str_(self):
        return self.soft.name+self.user.name
