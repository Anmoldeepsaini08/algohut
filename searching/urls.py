from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='searching'),
    path('LinearSearch',views.linearsearch,name='linearsearch'),
    path('BinarySearch',views.binarysearch,name='binarysearch'),
    path('JumpSearch',views.jumpsearch,name='jumpsearch'),
    path('InterpolationSearch',views.interpolationsearch,name='interpolationsearch'),
    path('FibonacciSearch',views.fibonaccisearch,name='fibonaccisearch')


   
]
