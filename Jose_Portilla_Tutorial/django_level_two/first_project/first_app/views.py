from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def home(request):
    web_page = AccessRecord.objects.order_by('-date')
    data_dict = {'acc_record': web_page}
    return render(request,'first_app/index.html', context = data_dict)

