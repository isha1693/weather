from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index", views.Index.as_view(), name="index"),
    path("add-question/", views.CreateQuestion.as_view(), name="add-question"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('persons/', views.person_list, name='person_list'),
    path('add/', views.PersonCreateView.as_view(), name='person-list'),
    path('persons/class/', views.PersonListView.as_view(), name='person_list_class'),
    path('edit/<int:person_id>/', views.add , name='add'),
    path('add',views.add),
    path('persons/', views.filter_persons, name='filter_persons'),
    path('addresses/', views.address_list, name='address_list'),
 ]

