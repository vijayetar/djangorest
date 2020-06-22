from django.urls import path

from .views import ReviewList, ReviewDetail

urlpatterns = [
  path('', ReviewList.as_view(), name="review_list"),
  path('<int:pk>/', ReviewDetail.as_view(), name="review_detail"),
]