from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#Dashboard view
@login_required
def dashboard(request):
    return render(request, 'miscellaneous/dashboard.html', {})
