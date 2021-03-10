from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts')
]

# no base.html, ao invés de colocar "/" ou "/contacts/" pode colocar um {% urls 'index' %} que também dá certo
# por isso tem o name = 'index' / 'contacts' ali, pra facilitar
