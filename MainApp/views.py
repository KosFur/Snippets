from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Snippet
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

@login_required
def my_snippets_page(request):
    snippets = Snippet.objects.filter(user=request.user)  
    return render(request, 'pages/view_snippets.html', {'snippets': snippets, 'pagename': 'Мои сниппеты'})


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description', 'is_public'] 

def edit_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('list_snippets')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'pages/edit_snippet.html', {'form': form})

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'POST':
        messages.success(request, 'Сниппет успешно создан!')
        return redirect('list_snippets')
    else:
        return render(request, 'pages/add_snippet.html')

def snippets_page(request):
    if request.user.is_authenticated:
        snippets = Snippet.objects.filter(is_public=True) | Snippet.objects.filter(user=request.user)
    else:
        snippets = Snippet.objects.filter(is_public=True)  
    return render(request, 'pages/view_snippets.html', {'snippets': snippets, 'pagename': 'Все сниппеты'})

def delete_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    snippet.delete()
    return redirect('list_snippets')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})