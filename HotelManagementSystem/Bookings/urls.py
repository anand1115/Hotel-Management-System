from django.urls import path
from . import views
app_name="Bookings"
urlpatterns=[
    path("",views.BookingView1.as_view(),name='booking1'),
    path("room/",views.BookingView2.as_view(),name='booking2'),
    path("confirm/",views.BookingView3.as_view(),name='booking3'),
    path("payment/",views.BookingView4.as_view(),name='booking4'),
]