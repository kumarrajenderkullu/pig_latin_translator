from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def translator(request):
    translate=""
    orignaltext = request.GET["textbox"]
    if len(orignaltext)>0:
        for text in orignaltext.split():
            if text[0] in {'a','e','i','o','u'}:
                translate+=text
                translate+="s "
            else:
                translate += "p"
                translate += text
                translate += "s "
    else:
        orignaltext="Empty text BOX"
        translate="Nothing can be translated for empty text BOX"


    return render(request,"translate.html",{"orignaltext":orignaltext,"translate":translate})

def about_us(request):
    return render(request,"About_us.html")