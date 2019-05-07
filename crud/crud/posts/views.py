from django.shortcuts import render

# Create your views here.
def create(request):
    form = PostForm()
    return render(request, 'posts/create.html', {'form':form})
    