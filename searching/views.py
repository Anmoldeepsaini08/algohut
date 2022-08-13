from django.shortcuts import render
import math
import mysql.connector as sql
import time
# Create your views here.


def index(request):
    data = sql.connect(host='localhost',user="root",passwd ="Root11",database='algohut')
    cursor = data.cursor()
    fetch = "select * from searching"
    cursor.execute(fetch)
    cards_data = [item[0] for item in cursor.fetchall()]
    params = {'page_name':'Searching','cards' : cards_data}
    return render(request,'vertical_cards.html',params)

def linearsearch(request):
    if request.method == 'POST':
        arr = request.POST.get('text_area')
        
        start_time = time.time()
        a,b = arr.split("\n")
        
        # a = element to search
        # b = array
        
        found = -1
        b =list(map(int,b.split()))
     
        for i in range(0, len(b)):
            if b[i] == int(a):
                found = i
        end_time = time.time()
        result = end_time-start_time

        if found == -1:
            params = {'Output':'Element Not found',"Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)

        else:
            params = {'Output':f"Found at index: {found}","Input":b,'time':f'Time:\t{result} .sec \n',}
            return render(request,'text_area_search.html',params)
    else:
    
        return render(request,'text_area_search.html')


def binarySearchutil(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
       
        if arr[mid] == x:
            return mid
 
       
        elif arr[mid] > x:
            return binarySearchutil(arr, l, mid-1, x)
 
        
        else:
            return binarySearchutil(arr, mid + 1, r, x)
 
    else:
       
        return -1
 
def binarysearch(request):
    if request.method == 'POST':
        arr = request.POST.get('text_area')
        start_time = time.time()

        a,b = arr.split("\n")
        b =list(map(int,b.split()))
        # a = element to search
        # b = array
        found = -1
        # l = left
        # r = right
        found = binarySearchutil(b,0,len(b)-1,int(a))
       
        end_time = time.time()
        result = end_time-start_time
        if found == -1:
            params = {'Output':'Element Not found',"Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)

        else:
            params = {'Output':f"Found at index: {found}","Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)
    else:
       
        return render(request,'text_area_search.html')

def jumpsearchutil( arr , x , n ):
    step = math.sqrt(n)
      
 
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
      
   
    while arr[int(prev)] < x:
        prev += 1
   
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev
      
    return -1


def jumpsearch(request):
    if request.method == 'POST':
        arr = request.POST.get('text_area')
        start_time = time.time()
        a,b = arr.split("\n")
        b =list(map(int,b.split()))
        # a = element to search
        # b = array
        found = -1
        # l = left
        # r = right
        found = math.floor(jumpsearchutil(b,int(a),len(b)))

        end_time = time.time()
        result = end_time-start_time

        if found == -1:
            params = {'Output':'Element Not found',"Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)

        else:
            params = {'Output':f"Found at index: {found}","Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)
    else:
        
        return render(request,'text_area_search.html')


def interpolationsearchutil(arr, lo, hi, x):
  
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
  
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
  
        # Condition of target found
        if arr[pos] == x:
            return pos
  
        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationsearchutil(arr, pos + 1,
                                       hi, x)
  
        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationsearchutil(arr, lo,
                                       pos - 1, x)
    return -1

def interpolationsearch(request):
    if request.method == 'POST':
        arr = request.POST.get('text_area')
        start_time = time.time()
        a,b = arr.split("\n")
        b =list(map(int,b.split()))
        # a = element to search
        # b = array
        found = -1
        # l = left
        # r = right
        found = interpolationsearchutil(b,0,len(b)-1,int(a))

        end_time = time.time()
        result = end_time-start_time

        if found == -1:
            params = {'Output':'Element Not found',"Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)

        else:
            params = {'Output':f"Found at index: {found}","Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)
    else:
        
        return render(request,'text_area_search.html')

def fibonaccisearchutil(arr, x, n):



	fibMMm2 = 0
	fibMMm1 = 1 
	fibM = fibMMm2 + fibMMm1 


	while (fibM < n):
		fibMMm2 = fibMMm1
		fibMMm1 = fibM
		fibM = fibMMm2 + fibMMm1


	offset = -1


	while (fibM > 1):


		i = min(offset+fibMMm2, n-1)

	
		if (arr[i] < x):
			fibM = fibMMm1
			fibMMm1 = fibMMm2
			fibMMm2 = fibM - fibMMm1
			offset = i

	
		elif (arr[i] > x):
			fibM = fibMMm2
			fibMMm1 = fibMMm1 - fibMMm2
			fibMMm2 = fibM - fibMMm1

	
		else:
			return i


	if(fibMMm1 and arr[n-1] == x):
		return n-1

	return -1






def fibonaccisearch(request):
    if request.method == 'POST':
        arr = request.POST.get('text_area')
        start_time = time.time()
        a,b = arr.split("\n")
        b =list(map(int,b.split()))
        # a = element to search
        # b = array
        found = -1
        # l = left
        # r = right
        found = fibonaccisearchutil(b,int(a),len(b))

        end_time = time.time()
        result = end_time-start_time

        if found == -1:
            params = {'Output':'Not found',"Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)

        else:
            params = {'Output':f"Found at index: {found}","Input":b,'time':f'Time:\t{result} .sec \n'}
            return render(request,'text_area_search.html',params)
    else:
        
        return render(request,'text_area_search.html')

