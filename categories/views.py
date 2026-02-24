from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    # Showcase dynamic data by getting related artifacts
    artifacts = category.artifacts.all()
    return render(request, 'category/category_detail.html', {'category': category, 'artifacts': artifacts})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories:list')
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form, 'title': 'Add New Era'})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form, 'title': f'Edit {category.get_name_display()}'})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    return render(request, 'category/category_confirm_delete.html', {'category': category})