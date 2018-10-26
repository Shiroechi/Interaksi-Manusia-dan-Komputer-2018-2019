from django.shortcuts import render
from MainApp.models import Category, Transportation, Schedule, Account
from MainApp.forms import LoginForm

def index(request):
    return render(request, "MainApp/header.html")

def home(request):
    all_categories          = Category.objects.all()
    categories_dictionary   = {'all_categories' : all_categories}
    return render(request, "MainApp/home.html",categories_dictionary)

def map(request):
    return render(request, "MainApp/map.html")

def new_home(request):
    return render(request, "MainApp/new_home.html")

def schedule_list(request, pk):
    query               = "SELECT * FROM MAINAPP_SCHEDULE S JOIN MAINAPP_TRANSPORTATION T ON S.TRANSPORTATION_ID_ID = T.id JOIN MAINAPP_CATEGORY C ON T.CATEGORY_ID_ID = C.id WHERE C.id = " + pk
    all_schedule        = Schedule.objects.raw(query)
    schedule_dictionary = {'all_schedule' : all_schedule}
    print(schedule_dictionary)
    # category = Category.objects.all().get(pk=pk)
    # RETURNS 0 OR MORE
    # transportations = Transportation.objects.all().filter(category_id=category)
    # transportations_dictionary = {'all_transportations' : transportations}
    return render(request, "MainApp/schedule_list.html", schedule_dictionary)

def schedule_detail(request, pk):
    query                       = "SELECT * FROM MAINAPP_SCHEDULE S WHERE S.id = " + pk
    schedule                    = Schedule.objects.raw(query)
    schedule_detail_dictionary  = {"schedule" : schedule}
    return render(request, "MainApp/schedule_detail.html", schedule_detail_dictionary)

def login(request):
    if request.method == 'GET':
        return render(request, "MainApp/login.html", {'response' : ""})
    else:
        input_mail      = request.POST.get("inputEmail", "")
        input_pass      = request.POST.get("inputPassword", "")
        found_account   = Account.objects.filter(email=input_mail, password=input_pass)
        if not found_account:
            return render(request, "MainApp/login.html", {'response' : False})
        else:
            return home(request)
        
def contact(request):
    content = {'content' : ['if you would like to contact me, please mail me at', 'm26416083@john.petra.ac.id']}
    return render(request, "MainApp/basic.html", content)