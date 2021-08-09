from django.urls import path
from . import views
from users.views import AccountUpdateView, AccountDeleteView

app_name = "users"

urlpatterns = [
    path('signup/', view=views.signup, name='signup'),    
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', view=views.logout, name='logout'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
