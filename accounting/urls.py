from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/<id_budget>', views.accounts, name='accounts'),
    path('operations/add', views.add_operation, name='add_operation'),
    path('operations/view/<id_operation>', views.view_operation, name='view_operation'),
    path('operations/<id_budget>', views.operations, name='operations'),
    path('planned_operations/<id_budget>', views.planned_operations, name='planned_operations'),
]
