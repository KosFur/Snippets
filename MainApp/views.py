from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Snippet
from django import forms

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description']  # Убедитесь, что эти поля соответствуют вашей модели

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
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов'}
    return render(request, 'pages/view_snippets.html', context)

def delete_snippet(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    snippet.delete()
    return redirect('list_snippets')