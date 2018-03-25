from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    """Model definition for userProfile."""
    
    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics", blank = True)
    portfolio_site = models.URLField(blank = True)

    def __str__(self):
        """Unicode representation of userProfile."""
        return self.user.username
