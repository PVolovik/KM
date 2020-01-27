from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    url(r'^persons/$', views.ChoiceListView.as_view(), name='persons'),
    url(r'^person/(?P<pk>\d+)$', views.ChoiceDetailView.as_view(), name='choice-detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
