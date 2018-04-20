from django.shortcuts import render

from Blog.models import Post

def index (request):
    return render(request, 'index.html')

def blog_list (request):
    blogs = Post.objects.all()
    return render (request, 'blog/blog_list.html', {"blogs": blogs, "active_menu": "blog"})

def blog_detail (request, blog_id):
    blog = Post.objects.get(pk=blog_id)
    return render (request, 'blog/blog_detail.html', {"blog": blog, "active_menu": "blog"}) 

def blog_add (request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        blog = Post (title=title, text=text)
        blog.save()
        return redirect('/blogs')
    else:
        return render(request, "blog/blog_add.html", {"active_menu": "blog"})

def blog_delete (request, blog_id):
    blog = Post.objects.get (pk=blog_id)
    blog.delete()
    return redirect('/blogs')

def blog_update (request, blog_id):
    blog = Post.objects.get (pk=blog_id)
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.text = request.POST['text']
        blog.save()
        return redirect('/blogs')
    else:
        return render(request, "blog/blog_update.html", {"active_menu": "blog", "blog": blog})
