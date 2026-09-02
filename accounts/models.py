from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
     # Idhi Database Table lo column layout
     user=models.OneToOneField(User,on_delete=models.CASCADE)
     about=models.CharField(max_length=500)
     city=models.TextField(max_length=500)
     district=models.TextField(max_length=500)
     state=models.TextField(max_length=500)
     Profile_picture=models.ImageField(upload_to='profiles/',blank=True,null=True)

     def __str__(self):
        return self.user.username

class Skills(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=50,
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
            ("Expert", "Expert"),
        ],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.profile.user.username}"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="education")
    institution = models.CharField(max_length=200)   
    degree = models.CharField(max_length=100)        
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.PositiveIntegerField(blank=True, null=True)
    end_year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.degree} at {self.institution} ({self.profile.user.username})"

class Achievements(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="achievements")
    title = models.CharField(max_length=200)             
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)       
    issuer = models.CharField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return f"{self.title} - {self.profile.user.username}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")
    job_title = models.CharField(max_length=200)       
    company = models.CharField(max_length=200)         
    location = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True) 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company} ({self.profile.user.username})"

class Certificates(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="certificates")
    title = models.CharField(max_length=200)              
    issuer = models.CharField(max_length=200)             
    issue_date = models.DateField(blank=True, null=True) 
    expiry_date = models.DateField(blank=True, null=True) 
    certificate_id = models.CharField(max_length=100, blank=True, null=True) 
    certificate_file = models.FileField(upload_to="certificates/", blank=True, null=True) 

    def __str__(self):
        return f"{self.title} - {self.profile.user.username}"

class Projects(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)             
    description = models.TextField(blank=True, null=True) 
    technologies = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)         
    project_file = models.FileField(upload_to="projects/", blank=True, null=True) 

    def __str__(self):
        return f"{self.title} ({self.profile.user.username})"

class Internship(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="internships")
    company = models.CharField(max_length=200)            
    role = models.CharField(max_length=200)                
    description = models.TextField(blank=True, null=True) 
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    certificate = models.FileField(upload_to="internships/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)        

    def __str__(self):
        return f"{self.role} at {self.company} ({self.profile.user.username})"

class Award(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="awards")
    title = models.CharField(max_length=200)             
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    certificate = models.FileField(upload_to="awards/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.profile.user.username})"

class Publication(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="publications")
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to="publications/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.profile.user.username})"

class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="resume")
    title = models.CharField(max_length=200, default="My Resume")   
    summary = models.TextField(blank=True, null=True)               
    file = models.FileField(upload_to="resumes/", blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)                  

    def __str__(self):
        return f"{self.title} ({self.profile.user.username})"

