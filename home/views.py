from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login, authenticate

from .forms import LoginForm, UserForm

# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}
    form = LoginForm()

    def get(self, request):
        self.context = {
            "form": self.form
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')

class Logout(generic.View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
class SignUp(generic.CreateView):
    template_name = "home/signup.html"
    form_class = UserForm
    success_url = reverse_lazy("home:inicio")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password1)
        if user is not None:
            login(self.request, user)
        id = form.cleaned_data.get("id")
        print(id)
        return redirect("home:inicio")