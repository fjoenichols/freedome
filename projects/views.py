from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django_activitypub.models import Note, LocalActor
from .models import Project, Task, Subtask
from .forms import ProjectForm, TaskForm, SubtaskForm
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                status=form.cleaned_data["status"],
                due_date=form.cleaned_data["due_date"],
                parent=project,
            )
            task.save()
            return HttpResponseRedirect(request.path_info)
        
    tasks = Task.objects.filter(parent=project)
    context = {
        "project":project,
        "tasks": tasks,
        "form": TaskForm(),
    }
    return render(request, 'projects/project_detail.html', context)

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

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    project = Project.objects.get(id=task.parent.id)
    form = SubtaskForm()
    if request.method == "POST":
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = Subtask(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                status=form.cleaned_data["status"],
                due_date=form.cleaned_data["due_date"],
                parent=task,
            )
            subtask.save()
            return HttpResponseRedirect(request.path_info)
        
    subtasks = Subtask.objects.filter(parent=task)
    context = {
        "task": task,
        "project": project,
        "subtasks": subtasks,
        "form": SubtaskForm(),
    }
    return render(request, 'projects/task_detail.html', context)

def subtask_detail(request, pk):
    subtask = Subtask.objects.get(pk=pk)
    task= Task.objects.get(id=subtask.parent.id)
    project= Project.objects.get(id=task.parent.id)
    context = {
        "task": task,
        "subtask": subtask,
        "project": project,
    }
    return render(request, 'projects/subtask_detail.html', context)
