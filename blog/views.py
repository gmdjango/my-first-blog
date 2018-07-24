from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # request - this is what we received from the user via the internet
    # 'blog/post_list.html' - this is our template file to renter
    # {} is a dictionary of parameters to use in the template
    return render(request, 'blog/post_list.html', {'posts':posts})

# this variable pk is passed to us from urls.py from <int:pk>
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
