from django.shortcuts import render
#from thirdapp.models import User
from thirdapp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'thirdapp/index.html')

def user(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR! FORM INVALID")
    return render(request, 'thirdapp/userpage.html',{'form':form})