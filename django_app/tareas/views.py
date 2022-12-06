from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputFom
from .tasks import send_name_email, add

# Create your views here.
def test_celery(request):
    template = "testCelery.html"
    print(request.method)
    # request.session["authors"] = 0
    # request.session["id"] = 0
    context = {
        "form": InputFom(),
       
    }
    
    
    if request.method == "POST":
        form = InputFom(request.POST)
        print("******")
        print(request.POST)
        print("******")
        if form.is_valid():
            add.delay(5,6)
            print(form.cleaned_data["name"], form.cleaned_data["email"])
            send_name_email.delay(form.cleaned_data["name"], form.cleaned_data["email"])
            result = send_name_email.delay("a", "b")
            print(result.backend)
            return HttpResponse(form.cleaned_data["name"] + " " + form.cleaned_data["email"])
    return render(request, template, context)

def index(request):
    return HttpResponse("HOME")

    git = "https://github.com/nicolagardo/silabuz-dnago-celery.git"