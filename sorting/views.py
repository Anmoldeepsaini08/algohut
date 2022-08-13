
from django.shortcuts import render
import mysql.connector as sql
import time
# Create your views here.

def index(request):
    
    data = sql.connect(host='localhost',user="root",passwd ="Root11",database='algohut')
    cursor = data.cursor()
    fetch = "select * from sorting"
    cursor.execute(fetch)
    cards_data = [item[0] for item in cursor.fetchall()]
    params = {'page_name':'Sorting','cards' : cards_data}
    return render(request,'vertical_cards.html',params)

def bubbleSort(request):

    if request.method == 'POST':
        arr = request.POST.get('text_area')
        
        #a,b = arr.split("\n")
        
        new_arr = list(map(int,arr.split()))
        start_time = time.time()

        n = len(new_arr)
  
     
        for i in range(n):
    
            for j in range(0, n-i-1):
    
               
                if new_arr[j] > new_arr[j+1]:
                    new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
        end_time = time.time()
        result = end_time-start_time
        params = {'Output':f'Sorted Array :\t {new_arr}',"Input":arr,'time':f'Time:\t{result} .sec \n'}
        return render(request,'text_area.html',params)
        


    else:
    
        
        return render(request,'text_area.html')

def insertionsort(request):

    if request.method == 'POST':

        arr = request.POST.get('text_area')

        new_arr = list(map(int,arr.split()))

        start_time = time.time()

        for i in range(1, len(new_arr)):
  
            key = new_arr[i]
    
            
            j = i-1
            while j >= 0 and key < new_arr[j] :
                    new_arr[j + 1] = new_arr[j]
                    j -= 1
            new_arr[j + 1] = key
        end_time = time.time()
        result = end_time-start_time

        params = {'Output':f'Sorted Array :\t {new_arr}',"Input":arr,'time':f'Time:\t{result} .sec \n'}
        return render(request,'text_area.html',params)

    else:
        
        return render(request,'text_area.html')


def selectionsort(request):

    if request.method == 'POST':

        arr = request.POST.get('text_area')

        new_arr = list(map(int,arr.split()))
        
        start_time = time.time()

        for i in range(len(new_arr)):
  
            min_idx = i
            for j in range(i+1, len(new_arr)):
                if new_arr[min_idx] > new_arr[j]:
                    min_idx = j
                    
               
            new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]

        end_time = time.time()
        result = end_time-start_time
        params = {'Output':f'Sorted Array :\t {new_arr}',"Input":arr,'time':f'Time:\t{result} .sec \n'}
        return render(request,'text_area.html',params)

    else:
        return render(request,'text_area.html')

def mergesortutil(arr):

    
        

    if len(arr) > 1:
 
    
        mid = len(arr)//2
    
        L = arr[:mid]
    
            
        R = arr[mid:]
    
          
        mergesortutil(L)
    
       
        mergesortutil(R)
    
        i = j = k = 0
    
         
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
         
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def mergesort(request):
    if request.method == 'POST':

        arr = request.POST.get('text_area')
        
        new_arr = list(map(int,arr.split()))

        start_time = time.time()

        new_arr = mergesortutil(new_arr)
        end_time = time.time()
        result = end_time-start_time
        params = {'Output':f'Sorted Array :\t {new_arr}',"Input":arr,'time':f'Time:\t{result} .sec \n'}
        return render(request,'text_area.html',params)

    else:
       
        return render(request,'text_area.html')



    
