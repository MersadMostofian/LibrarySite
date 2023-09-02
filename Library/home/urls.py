from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.addBook,name='add'),
    path('detile/<int:Book_id>',views.detile,name='detile'),
    path('edite/<int:Book_id>',views.edit,name='edite'),
    path('delete/<int:Book_id>',views.delete,name='delete'),
    path('get/<int:Book_id>',views.get_book,name='get'),
    path('users/get',views.users_get,name='users_get'),
    path('users/leave',views.users_leave,name='users_leave'),
    path('recruitment/<str:user_name>',views.get_employee,name='get_employee'),
    path('layingoff/<str:user_name>',views.out_employee,name='out_employee'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)