from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
# As you can see, this uses a constant STATUS. Create this constant above the class as a tuple.

class Post(models.Model):
    # Note: The title values should be unique to avoid having blog posts of the same name confusing your users.
    title = models.CharField(max_length=200, unique=True)
    # In Django the slug is what you'll use to build a URL for each of your posts.
    slug = models.SlugField(max_length=200, unique = True)
     # Note: One user can write many posts, so this is a one-to-many or Foreign Key. 
     # The cascade on delete means that on the deletion of the user entry, all their posts are also deleted. 
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # Note: This is the blog article content.
    # Note: The auto_now_add=True means the default created time is the time of post entry.
    content = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    # 
    # In the Post model, add an attribute status defined as an integer field with a default of 0.
    status = models.IntegerField(choices=STATUS, default=0)
    # As you can see, this uses a constant STATUS. Create this constant above the class as a tuple. (row 6)
    excerpt = models.TextField(blank=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = "comments"
    )
    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name = "commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
