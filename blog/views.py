from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm 
from account.models import CustomUser
from django.db.models import Count
from django.db.models import Q


def blog_list(request):
	blogs = Blog.objects.all()
	return render(request, 'blogpage.html', {'blogs': blogs})


def blog_detail(request, pk):
	blog = Blog.objects.get(pk=pk)
	return render(request, 'blogpage.html', {'blog': blog})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            author = request.user
            
            blog = Blog.objects.create(title=title, description=description, image=image, author=author)
            
            return redirect('user') 
    else:
        form = BlogForm()
    
    return render(request, 'create.html', {'form': form})


def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():

            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
           
            blog.edit(title, description, image)
            
            return redirect('user')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit.html', {'form': form})

def delete_blog(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method == 'POST':
		blog.delete()
		return redirect('user')
	return render(request, 'delete.html', {'blog': blog})


@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user not in blog.likes.all():
        blog.likes.add(request.user)
        blog.update_likes_count()
    return redirect('blog_detail', pk=blog_id)

@login_required
def unlike_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        blog.update_likes_count()
    return redirect('blog_detail', pk=blog_id)


def homepage(request):
   
    recent_blogs = Blog.objects.order_by('-created_at')[:3]
    
    top_writers = CustomUser.objects.annotate(num_likes=Count('blogs__likes')).order_by('-num_likes')[:3]
    
    most_liked_blogs = Blog.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:3]
    
    context = {
        'recent_blogs': recent_blogs,
        'top_writers': top_writers,
        'most_liked_blogs': most_liked_blogs,
    }
    
    return render(request, 'homepage.html', context)


def search_blogs(request):
    query = request.GET.get('q', '')
    if query:
        search_results = Blog.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        search_results = Blog.objects.none()

    context = {
        'query': query,
        'search_results': search_results,
    }
    return render(request, 'search_results.html', context)
