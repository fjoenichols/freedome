from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_activitypub.models import Note, LocalActor
from .models import Project
from .forms import ProjectForm
# Create your views here.

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            try: 
                local_actor = LocalActor.objects.get(name=request.user)
                note = Note(
                    local_actor = local_actor,
                    content = request.user.name + " started a new project called " + form.cleaned_data["title"],
                    content_url = request.build_absolute_uri('/' + request.user.username + '/projects')
                )
                note.save()
            except: 
                pass
            finally: 
                project = form.save(commit=False)
                project.owner = request.user
                project.save()

            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def project_public(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_public.html', {'projects': projects})