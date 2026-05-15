from django.http import HttpResponse,HttpRequest
from accounts.decorators import owner_required


@owner_required
def owner_view(request):
    return HttpResponse("Owner dashboard — coming soon.")

# Hotel Owner
def hotel_create(request):
    pass

# Hotel Owner
def hotel_update(request, pk):
    pass

# Hotel Owner
def hotel_delete(request, pk):
    pass

# Hotel Owner
def capsule_list(request, hotel_pk):
    pass

# Hotel Owner
def capsule_create(request, hotel_pk):
    pass

# Hotel Owner
def capsule_update(request, pk):
    pass

# Hotel Owner
def capsule_delete(request, pk):
    pass