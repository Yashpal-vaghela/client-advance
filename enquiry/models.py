from django.db import models



class NewsLetter(models.Model):
    email = models.CharField(max_length = 150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    
   
class Review(models.Model):
    name  = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    message  = models.TextField()
    date = models.DateField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.email
    
class Contact(models.Model):
    name  = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    contact = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 150)
    message  = models.TextField()
    date = models.DateField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.email

class STLFile(models.Model):
    name  = models.CharField(max_length = 150)
    contact = models.CharField(max_length = 150)
    message  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    def files(self):
        q = STLFileData.objects.filter(stl_data=self.id)
        return q

class STLFileData(models.Model):
    files = models.FileField(upload_to="STL_FILE")
    stl_data  = models.ForeignKey(STLFile, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.stl_data)



class InstaPost(models.Model):
    name  = models.CharField(max_length = 150)
    image  = models.ImageField(upload_to="INSTA")
    date = models.DateField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
     