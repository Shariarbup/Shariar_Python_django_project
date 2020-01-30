from django.shortcuts import render


# Create your views here.
def other(request):
    context_dict ={'text': 'hello world', 'num': 100}
    return render(request, 'basic_app/other.html', context_dict)
def help(request):
    return render(request, 'basic_app/help.html')