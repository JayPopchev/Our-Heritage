from django.shortcuts import render, get_object_or_404

from artifacts.filters import ArtifactFilter
from artifacts.models import Artifact


# Create your views here.

def home_page(request):
    featured_artifacts = Artifact.objects.all().order_by('-id')[:3]

    context = {
        'featured_artifacts': featured_artifacts
    }
    return render(request, 'home.html', context)
def dashboard(request):
    # 1. Pass the GET data (the search/filter info) to the filter class
    artifact_filter = ArtifactFilter(request.GET, queryset=Artifact.objects.all())

    context = {
        'filter': artifact_filter,         # Needed to render the form (search bar/checkboxes)
        'artifacts': artifact_filter.qs,   # This is the "filtered" list of artifacts
    }

    # 2. HTMX Check: If this is an HTMX request, only send the list, not the whole page
    if request.headers.get('HX-Request'):
        return render(request, 'artifacts/partials/artifact_list.html', context)

    # 3. Normal page load
    return render(request, 'artifacts/dashboard.html', context)


def artifact_detail(request, slug):
    # Fetch the artifact by slug, or return 404 if it doesn't exist
    artifact = get_object_or_404(Artifact, slug=slug)
    # We want to show other artifacts from the same category as "Related"
    related_artifacts = Artifact.objects.filter(
        category=artifact.category
    ).exclude(id=artifact.id)[:3]
    context = {
        'artifact': artifact,
        'related_artifacts': related_artifacts
    }
    return render(request, 'artifacts/detail.html', context)