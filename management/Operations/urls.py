from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('graph/',views.graph_view,name='graph'),
    path('login/', views.User_login.as_view(), name='login'),
    path('logout/', views.userlogout, name='logoutuser'),
    path('export-csv',views.exporttask,name='exportcsvtask'),
    path('rechercher/', views.Projetrechercher.as_view(), name='rechercher'),
    path('projets/create',views.ProjetView.as_view(),name='projectCreate'),
    path('projets/',views.ProjetListView.as_view(),name='projectList'),
    path('projets/<int:idp>/update',views.ProjetUpdateView.as_view(),name='projectUpdate'),
    path('projets/<int:idp>/delete',views.ProjetDeleteView.as_view(),name='projectDelete'),
    path('projets/<int:idp>/details',views.ProjetDetailsView.as_view(),name='projectDetails'),
    path('categories/create', views.CategoryView.as_view(),name="categoryCreate"),
    path('categories/', views.CategoryListView.as_view(),name="categoryList"),
    path('categories/<int:idp>/update',views.CategoryUpdateView.as_view(),name='categoryUpdate'),
    path('categories/<int:idp>/delete',views.CategoryDeleteView.as_view(),name='categoryDelete'),
    path('categories/<int:idp>/details',views.CategoryDetailsView.as_view(),name='categoryDetails'),
    path('Taches/create',views.TacheView.as_view(),name='tacheCreate'),
    path('Tasks/',views.TacheListView.as_view(),name='tacheList'),
    path('Tasks/<int:idp>/update',views.TacheUpdateView.as_view(),name='tacheUpdate'),
    path('Tasks/<int:idp>/delete',views.TacheDeleteView.as_view(),name='tacheDelete'),
    path('Tasks/<int:idp>/details',views.TacheDetailsView.as_view(),name='tacheDetails'),
    path('ressource/create',views.RessourceView.as_view(),name='ressourceCreate'),
    path('ressources/',views.RessourceListView.as_view(),name='ressourceList'),
    path('ressources/<int:idp>/update',views.RessourceUpdateView.as_view(),name='ressourceUpdate'),
    path('ressources/<int:idp>/delete',views.RessourceDeleteView.as_view(),name='ressourceDelete'),
    path('ressources/<int:idp>/details',views.RessourceDetailsView.as_view(),name='ressourceDetails'),
    path('employes/create',views.EmployeView.as_view(),name='employeCreate'),
    path('employes/',views.EmployeListView.as_view(),name='employeList'),
    path('employes/<int:idp>/update',views.EmployeUpdateView.as_view(),name='employeUpdate'),
    path('employes/<int:idp>/delete',views.EmployeDeleteView.as_view(),name='employeDelete'),
    path('employes/<int:idp>/details',views.EmployeDetailsView.as_view(),name='employeDetails'),
    #path('gantt/',views.TacheGanttView.as_view(),name='tachegantt'),
    ]