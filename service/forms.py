from django.forms import ModelForm
from .models import Ticket


class TicketCreateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ("title", "target_date", "from_user", "to_user")
