from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django_activitypub.models import LocalActor
from accounts.forms import RegisterForm, CustomUserForm
from projects.models import Project
from django.conf import settings

def index(request):
    if (request.user.is_authenticated):
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return render(request, "accounts/index.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            print(form.errors)  
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required()    
def create_local_actor(request):
    print('creating local actor for ' + request.user.username)
    user = get_user_model().objects.get(username=request.user)
    LocalActor.objects.create(user=user, name=user.username, preferred_username=user.username, domain="freedome.us")
    return redirect('profile')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

@login_required
def profile(request):
    account = request.user
    projects = Project.objects.filter(owner=account)
    try:
        actor = LocalActor.objects.get(name=request.user)
        context = {
            "actor": actor,
            "user": account,
            "projects": projects,
        }
        return render(request, "accounts/profile.html", context)
    except:
        context = {
            "user": account,
            "projects": projects,
        }
        return render(request, "accounts/profile.html", context)

@login_required
def profile_update(request):
    account = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('profile')
    else: 
        form = CustomUserForm(instance=account)
    context = {
        "user": account,
        "form": form,
    }
    return render(request, 'accounts/profile_update.html', context)