from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/compte/connection/login')
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "account/register.html", context)


