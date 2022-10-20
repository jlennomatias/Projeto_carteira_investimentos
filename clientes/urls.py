from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
    path('update_ativo/<int:id>', views.update_ativo, name="update_ativo"),
    path('excluir_ativo/<int:id>', views.excluir_ativo, name="excluir_ativo"),
    path('update_cliente/<int:id>', views.update_cliente, name="update_cliente")
]
