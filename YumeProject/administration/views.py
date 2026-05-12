from django.http import HttpResponse
from accounts.decorators import admin_role_required


@admin_role_required
def admin_view(request):
    return HttpResponse("Administration panel — coming soon.")
