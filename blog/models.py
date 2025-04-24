from django.db import models
from account.models import CustomUser

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    likes = models.ManyToManyField(CustomUser, related_name='liked_blogs', blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
   
    def edit(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image
        self.save()

    def short_description(self):
       
        words = self.description.split()
        if len(words) > 50:
           
            return ' '.join(words[:50]) + '...'
        else:
           
            return self.description

    def update_likes_count(self):
        self.likes_count = self.likes.count()
        self.save()
