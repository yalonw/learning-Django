from django.shortcuts import render, redirect
from .models import Record, Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
    a = 1
    return render(request, 'app/hello.html', {'a':a})

def dashboard(request):
    return render(request, 'app/dashboard.html', {})
    

@login_required
def frontpage(request):
    user = request.user
    record_form = RecordForm(user=user, initial={'balance_type':'支出'})
    records = Record.objects.filter(user=user)
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list)!=0 else 0
    outcome = sum(outcome_list) if len(outcome_list)!=0 else 0
    net = income - outcome
    return render(request,'app/index.html',locals())

@login_required
def settings(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    return render(request,'app/settings.html',locals()) 

@login_required
def addCategory(request):
    if request.method == 'POST':
        user = request.user
        posted_data = request.POST
        category = posted_data['add_cateogry']
        Category.objects.get_or_create(user=user, category=category)
    return redirect('/settings')

@login_required
# def deleteCategory(request):
#     if request.method == 'POST':
#         category = request.POST['delete_category']
#         Category.objects.filter(user=user, category=category).delete()
#     return redirect('/settings')
def deleteCategory(request, category):
    user = request.user
    Category.objects.filter(user=user, category=category).delete()
    return redirect('/settings')

@login_required
def addRecord(request):
    if request.method == 'POST':
        user = request.user
        form = RecordForm(user,request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            record.save()
    return redirect('/')

@login_required
def deleteRecord(request):
	if request.method == 'POST':
		id = request.POST['delete_val']
		Record.objects.filter(id=id).delete()
	return redirect('/')
