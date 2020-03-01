from django.shortcuts import render, get_object_or_404

from django.views.generic import RedirectView #FAVICON
from django.http import HttpResponse

from .forms import CommentForm #ВОПРОСЫ!!!
from .models import Articles, Comment

def index(request):
    post = Articles.objects.get(id=1)
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.post = post
            comm.save()
    else:
        form = CommentForm()

    #comm_sort = comm.order_by('-created')
    return render(request, "blog/post.html", {'post': post, 'form': form, 'comments': comments})



def show(request, pk=1):
    post = Articles.objects.get(id=pk)
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(request, "blog/post.html", {'post': post, 'form': form, 'comments': comments})


def download(request):
    return render(request, 'blog/download.html')

def contact(request):
    return render(request, 'blog/contact.html')



# def post_single(request, pk):
#     post = get_object_or_404(Articles, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comm = form.save(commit=False)
#             comm.post = post
#             comm.save()
#     else:
#         form = CommentForm()
#     return render(request, "blog/post.html", {'post': post, 'form': form})




