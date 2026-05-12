from django.http import HttpResponse
from accounts.decorators import owner_required


@owner_required
def owner_view(request):
    return HttpResponse("Owner dashboard — coming soon.")
