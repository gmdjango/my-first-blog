from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # request - this is what we received from the user via the internet
    # 'blog/post_list.html' - this is our template file to renter
    # {} is a dictionary of parameters to use in the template
    return render(request, 'blog/post_list.html', {'posts':posts})
