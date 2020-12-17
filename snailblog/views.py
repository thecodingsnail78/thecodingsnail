from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Post, Comment, Item
from .forms import PostForm,CommentForm, ContactForm

# Create your views here.

def video(request):

    obj=Item.objects.all()
    return render(request,'snailblog/video.html',{'obj':obj})

def contact_us(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            # send email code here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} ({1}) has sent you a message\n{2}".format(sender_name, sender_email, form.cleaned_data['message'])
            send_mail('Web Enquiry', message, 'info@thecodingsnail.co.uk', ['info@thecodingsnail.co.uk'], fail_silently=False)
            return render(request,'snailblog/contact.html',{'success' : True, 'selected' : 'contact'})
    else:
        form=ContactForm()
    return render(request,'snailblog/contact.html', {'form' : form, 'selected':'contact'})

def index(request):
    return render(request,'snailblog/index.html', { 'selected':'index' })

def about(request):
    return render(request, 'snailblog/about.html', {'selected' : 'about'})

def resources(request):
    obj=Item.objects.all()
    return render(request, "snailblog/resources.html", {'selected' : 'resources','obj':obj})

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #my_months = [x.month + "_" + x.year for x in posts]
    my_months = [x.month for x in posts]
    months = {}
    for month in my_months:
        months[month] = {}
        for post in posts:
            if post.month == month:
                months[month][post.pk] = post
    
    return render(request, 'snailblog/post_list.html', {'posts':posts,'selected' : 'blog', 'len': len(posts), 'months': months})    

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'snailblog/post_detail.html', {'post':post, 'selected' : 'blog'})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:

        form = PostForm()
    return render(request, 'snailblog/post_edit.html',{'form':form, 'selected' : 'blog'})

@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            #post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'snailblog/post_edit.html',{'form':form, 'selected' : 'blog'})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'snailblog/post_draft_list.html', {'posts': posts, 'selected' : 'blog'})

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def post_remove(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'snailblog/add_comment_to_post.html', {'form': form, 'selected' : 'blog'})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)