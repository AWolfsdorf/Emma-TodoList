
from .models import UserProfile 
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    model = UserProfile
    template_name = 'AppList/index.html'
    # Agregando la siguiente linea le cambias el nombre del 'object_list'
    # context_object_name = 'user_profiles'
    