
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
import json
import urllib.request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def home(request):
    return render(request,'home.html')

def map(request):
    return render(request, 'map.html')

from django.shortcuts import render, redirect
from .models import Post  # Make sure to import your Post model
from .forms import PostForm  # Import your form

def blog(request):
    # Get the search query from GET parameters
    search_query = request.GET.get('search', '')
    
    # Filter posts based on the search query if provided
    if search_query:
        posts = Post.objects.filter(para__icontains=search_query)  # Adjust to your field
    else:
        posts = Post.objects.all()
    
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/blog")
    
    context = {'posts': posts, 'form': form, 'search_query': search_query}
    return render(request, 'blog.html', context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/blog")
    
    context = {'form': form}
    return render(request, "update_post.html", context)

def deletePost(request, pk):
    item = Post.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('/blog')
    
    context = {'item': item}
    return render(request, 'delete.html', context)
        

def currency(request):
    return render(request,'currency.html')

def translate(request):
    return render(request,'translate.html')

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_data = json.loads(res)
        temp_kelvin = json_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15

        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": f"{temp_celsius:.2f} °C",  # Displaying temperature in Celsius
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
    }
    else:
        city = ''
        data ={}
    return render (request, 'weather.html',{'city':city, 'data':data})

def places(request):
    return render(request,'places.html')

def guides(request):
    return render(request,'guides.html')

def about(request):
    return render(request,'about.html')




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/blog")
    
    context = {'form': form}
    return render(request, "update_post.html", context)