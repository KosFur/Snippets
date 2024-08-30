from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SnippetForm
from .models import Snippet
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Вы можете войти в систему.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/accounts/login/')
def add_snippet_page(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user  # Привязка пользователя к сниппету
            snippet.save()
            messages.success(request, 'Сниппет успешно создан!')
            return redirect('list_snippets')
    else:
        form = SnippetForm()
    return render(request, 'pages/add_snippet.html', {'form': form})



@login_required
def edit_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)

    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сниппет успешно отредактирован!')
            return redirect('list_snippets')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'pages/edit_snippet.html', {'form': form})

@login_required
def delete_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)

    if request.method == 'POST':
        snippet.delete()
        messages.success(request, 'Сниппет успешно удален!')
        return redirect('list_snippets')

    return render(request, 'pages/delete_confirmation.html', {'snippet': snippet})

@login_required
def my_snippets_page(request):
    snippets = Snippet.objects.filter(user=request.user)
    return render(request, 'pages/view_snippets.html', {'snippets': snippets})

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    return render(request, 'pages/snippet_detail.html', {'snippet': snippet})

def snippets_page(request):
    if request.user.is_authenticated:
        snippets = Snippet.objects.filter(is_public=True) | Snippet.objects.filter(user=request.user)
    else:
        snippets = Snippet.objects.filter(is_public=True)
    
    print(snippets) 
    return render(request, 'pages/view_snippets.html', {'snippets': snippets})


@login_required
def profile_page(request):
    return render(request, 'profile.html')

def index_page(request):
    return render(request, 'pages/index.html')