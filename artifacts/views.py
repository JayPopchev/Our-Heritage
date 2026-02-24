from django.shortcuts import render, get_object_or_404, redirect

from artifacts.filters import ArtifactFilter
from artifacts.forms import ArtifactForm
from artifacts.models import Artifact
from resources.models import ArtifactResource  # <-- ADD THIS IMPORT


def home_page(request):
    featured_artifacts = Artifact.objects.select_related('category').prefetch_related('media').order_by('-id')[:3]

    context = {
        'featured_artifacts': featured_artifacts
    }
    return render(request, 'home.html', context)


def dashboard(request):
    artifact_filter = ArtifactFilter(request.GET, queryset=Artifact.objects.all())

    context = {
        'filter': artifact_filter,
        'artifacts': artifact_filter.qs,
    }

    if request.headers.get('HX-Request'):
        return render(request, 'artifacts/partials/artifact_list.html', context)

    return render(request, 'artifacts/dashboard.html', context)


def artifact_detail(request, slug):
    artifact = get_object_or_404(Artifact, slug=slug)
    related_artifacts = Artifact.objects.filter(
        category=artifact.category
    ).exclude(id=artifact.id)[:3]
    context = {
        'artifact': artifact,
        'related_artifacts': related_artifacts
    }
    return render(request, 'artifacts/detail.html', context)


def artifact_create(request):
    if request.method == 'POST':
        form = ArtifactForm(request.POST)
        if form.is_valid():
            artifact = form.save()

            image_url = form.cleaned_data.get('image_url')
            if image_url:
                ArtifactResource.objects.create(artifact=artifact, image_url=image_url)

            return redirect('artifacts:detail', slug=artifact.slug)
    else:
        form = ArtifactForm()
    return render(request, 'artifacts/artifact_form.html', {'form': form, 'title': 'Add New Treasure'})


def artifact_edit(request, slug):
    artifact = get_object_or_404(Artifact, slug=slug)
    first_resource = artifact.media.first()
    initial_data = {}
    if first_resource and first_resource.image_url:
        initial_data['image_url'] = first_resource.image_url

    if request.method == 'POST':
        form = ArtifactForm(request.POST, instance=artifact)
        if form.is_valid():
            artifact = form.save()
            image_url = form.cleaned_data.get('image_url')

            if image_url:
                if first_resource:
                    first_resource.image_url = image_url
                    first_resource.save()
                else:
                    ArtifactResource.objects.create(artifact=artifact, image_url=image_url)
            elif first_resource:
                first_resource.delete()  # User cleared the input field, so remove the image

            return redirect('artifacts:detail', slug=artifact.slug)
    else:
        # Pass the initial data so the URL shows up in the input box when editing
        form = ArtifactForm(instance=artifact, initial=initial_data)

    return render(request, 'artifacts/artifact_form.html', {'form': form, 'title': f'Edit {artifact.title}'})


def artifact_delete(request, slug):
    artifact = get_object_or_404(Artifact, slug=slug)
    if request.method == 'POST':
        artifact.delete()
        return redirect('artifacts:list')
    return render(request, 'artifacts/artifact_confirm_delete.html', {'artifact': artifact})

from .models import Artifact, Exhibition # Add Exhibition here

def exhibition_list(request):
    exhibitions = Exhibition.objects.all().order_by('start_date')
    return render(request, 'exhibitions/exhibition_list.html', {'exhibitions': exhibitions})

def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    # The 'artifacts' here come from the Many-to-Many field
    return render(request, 'exhibitions/exhibition_detail.html', {'exhibition': exhibition})