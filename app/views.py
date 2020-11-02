from django.shortcuts import render
from pandas import read_excel

def index(request):
    if request.method == 'POST':
        if 'sheet_file' in request.FILES:
            df = read_excel(request.FILES['sheet_file'], 0, dtype=str).groupby(['ExamID', 'TabulationSerial'])
            ctx = {'df': df}
            return render(request, 'app/marksheet.html', context=ctx)
    return render(request, 'app/index.html')
