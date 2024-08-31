from django.urls import path
from .views import socio_create_update,socio_detail,socio_delete,socio_list


app_name = 'socios'

urlpatterns = [
	path('new/', socio_create_update, name='socio_create'),
	path('edit/<int:socio_id>/', socio_create_update, name='socio_update'),
	path('detail/<int:socio_id>/', socio_detail, name='socio_detail'),
	path('delete/<int:socio_id>/', socio_delete, name='socio_delete'),
	path('list/', socio_list, name='socio_list'),
]