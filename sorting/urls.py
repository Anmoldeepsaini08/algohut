from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='sorting'),
    path('BubbleSort',views.bubbleSort,name='bubblesort'),
    path('InsertionSort',views.insertionsort,name='insertionsort'),
    path('SelectionSort',views.selectionsort,name='selectionsort'),
    path('MergeSort',views.mergesort,name='mergersort')

   
]
