from django.urls import path
from . import views
from users.views import AccountUpdateView, AccountDeleteView

app_name = "users"

urlpatterns = [
    path('signup/', view=views.signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', view=views.logout_view, name='logout'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('dibs_list/', view=views.dibs_list, name='dibs_list'),
    path('reviews_list/', view=views.reviews_list, name='reviews_list'),
]
