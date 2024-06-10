from django.contrib import admin
from .models import Post
from .models import Comment

# Register your models here.
admin.site.register(Post)
# Note: This will allow you to create, update and delete blog posts from the admin panel. 
# However, please refrain from adding any posts at the moment, 
# as there are more fields to be added to the tables in an upcoming topic.
admin.site.register(Comment)