from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
# , PostForm
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, 'blog/post_list.html', {'posts': posts, 'form':form})

# def post_new(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     form = PostForm()
#     if request.method == "POST":
#         form = Post(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.published_date = timezone.now()
#             post.save()
#             # return HttpResponse("you saved") 
#             return render(request, 'blog/post_list.html', { 'posts':posts,'form': form})
#     # else:
#     #     form = PostForm()
#     return render(request, 'blog/post_list.html', {'posts': posts, 'form': form})

def add(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    form = PostForm()
    return render(request, 'blog/add.html', {'posts':posts,'form':form})

    # else:
    #     return HttpResponse("you saved")
   

    # redirect('blog/post_list.html', {'form': form})