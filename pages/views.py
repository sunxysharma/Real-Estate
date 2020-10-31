from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices ,bedroom_choices ,state_choices


from listings.models import Listing
from realtors.models import Realtor
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request,'pages/index.html',{
        'listings':listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices
    })


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    return render(request,'pages/about.html',{'realtors':realtors,'mvp_realtors':mvp_realtors})