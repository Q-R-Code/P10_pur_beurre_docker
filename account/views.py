from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    """function for request recovery and verification """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/compte/connection/login')
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "account/register.html", context)
