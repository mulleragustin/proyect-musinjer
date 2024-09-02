from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from socios.models import Socio

@login_required
def home(request):
    active_members = Socio.objects.filter(estado='A').count()
    suspended_members = Socio.objects.filter(estado='S').count()
    inactive_members = Socio.objects.filter(estado='B').count()
    ctx = {
        'active_members': active_members, 
        'suspended_members': suspended_members,
        'inactive_members': inactive_members,
    }
    return render(request, 'base.html', ctx)