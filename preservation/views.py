from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from artifacts.models import Artifact
from .models import PreservationRecord
from .forms import PreservationForm


def preservation_detail(request, artifact_slug):
    artifact = get_object_or_404(Artifact, slug=artifact_slug)
    # Fetch all records for this artifact (using the related_name 'logs' from your model)
    records = artifact.logs.all()

    context = {
        'artifact': artifact,
        'records': records,
    }
    return render(request, 'preservation/preservation_detail.html', context)
def preservation_add(request, artifact_slug):
    artifact = get_object_or_404(Artifact, slug=artifact_slug)

    if request.method == 'POST':
        form = PreservationForm(request.POST)
        if form.is_valid():
            # Don't save to the database just yet
            preservation_record = form.save(commit=False)
            # Attach the specific artifact to the record
            preservation_record.artifact = artifact
            # Now save it!
            preservation_record.save()
            return redirect('artifacts:detail', slug=artifact.slug)
    else:
        form = PreservationForm()

    context = {
        'form': form,
        'artifact': artifact,
        'title': f'Preservation Check: {artifact.title}'
    }
    return render(request, 'preservation/preservation_form.html', context)


def preservation_log_detail(request, artifact_slug, pk):
    artifact = get_object_or_404(Artifact, slug=artifact_slug)
    # Get the specific record, making sure it belongs to this artifact
    record = get_object_or_404(PreservationRecord, pk=pk, artifact=artifact)

    context = {
        'artifact': artifact,
        'record': record,
    }
    return render(request, 'preservation/preservation_log_detail.html', context)


def preservation_edit(request, artifact_slug, pk):
    artifact = get_object_or_404(Artifact, slug=artifact_slug)
    record = get_object_or_404(PreservationRecord, pk=pk, artifact=artifact)

    if request.method == 'POST':
        # Pass the 'instance' so Django updates the existing record instead of creating a new one
        form = PreservationForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('preservation:detail', artifact_slug=artifact.slug)
    else:
        form = PreservationForm(instance=record)

    context = {
        'form': form,
        'artifact': artifact,
        'title': f'Edit Check: {record.check_date}'
    }
    # We can reuse the exact same form template we created for adding!
    return render(request, 'preservation/preservation_form.html', context)


def preservation_delete(request, artifact_slug, pk):
    artifact = get_object_or_404(Artifact, slug=artifact_slug)
    record = get_object_or_404(PreservationRecord, pk=pk, artifact=artifact)

    if request.method == 'POST':
        record.delete()
        return redirect('preservation:detail', artifact_slug=artifact.slug)

    context = {
        'artifact': artifact,
        'record': record,
    }
    return render(request, 'preservation/preservation_confirm_delete.html', context)