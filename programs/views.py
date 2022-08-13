
from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
def index(request):
    if request.method == 'POST':
        git = request.POST.get('execute_btn')
        params = {'source' : git}
        return render(request,'programs.html',params)


    else:
        data = sql.connect(host='localhost',user="root",passwd ="Root11",database='algohut')
        cursor = data.cursor()
        fetch = "select * from programs"
        cursor.execute(fetch)
        cards_data = [item for item in cursor.fetchall()]
        
        params  = {'cards_data' : cards_data}
        return render(request,'vertical_program_cards.html',params)
