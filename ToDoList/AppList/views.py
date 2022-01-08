
from .models import UserProfile 
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    model = UserProfile
    template_name = 'AppList/index.html'
    