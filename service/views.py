from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketCreateForm


def index(request):
    if request.method == "POST":
        ticket = Ticket.objects.filter(title=list(request.POST.keys())[1]).first()
        ticket.is_done = False if ticket.is_done else True
        ticket.save()
        return render(request, "index.html", {"tickets": Ticket.objects.all()})
    return render(request, "index.html", {"tickets": Ticket.objects.all()})


def create(request):
    form = TicketCreateForm()
    if request.method == "POST":
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, "create.html", {"form": form})
