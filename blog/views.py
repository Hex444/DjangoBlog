from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [

    {
        'author':'Hex',
        'title':'myFirstPost',
        'content':'This is the content of the first ever post in the series so hope this goes well and i can stop being an idiot and leaern some stuff instead of helplessly asking others about what to do hope this teaches me something in life hope i can be good at something',
        'date_posted':'10-5-2021',
    },
    {
        'author':'Wil',
        'title':'Lmanburg anthem',
        'content':'i heard there was a special place, where men could go and emancipate the brutality and tyrrany of their rulers. asajslkjdfalksjdfkajsfkalskdfj ltubbo tommy f*ck eret aksldfjaskdlfkasjdkfalskflaskdjflkasdjflaksdfj my lmanburg,my lmanburg',
        'date_posted':'10-5-2021',
    },

]




def home(req):
    context={
        'posts':Post.objects.all()
    }
    return render(req,'blog/home.html',context=context)

def about(req):
    return render(req,'blog/about.html',{'title':'About'})