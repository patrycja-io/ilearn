from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="about"),
	path('basket/', views.basket, name="basket"),
	path('checkout/', views.checkout, name="checkout"),
	path('store/', views.store, name="store"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]