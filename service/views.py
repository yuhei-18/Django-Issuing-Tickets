from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketCreateForm


def index(request):
    tickets = Ticket.objects.all()
    return render(request, "index.html", {"tickets": tickets})


def create(request):
    form = TicketCreateForm()
    print("form")
    if request.method == "POST":
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
        return redirect("/")
    return render(request, "create.html", {"form": form})
