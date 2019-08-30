from django.urls import path
from . import views
urlpatterns = [
    path('borrow_screen',views.borrow_screen),
    path('touzhi',views.touzhi),
    path('bid/<int:p_id>',views.bid),
    path('tbmoney',views.tbmoney),
    path('timed',views.timed)
]
