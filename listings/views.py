from django.shortcuts import get_object_or_404 ,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices ,state_choices

from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request,'listings/listings.html',{'listings':paged_listings})

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    return render(request,'listings/listing.html',{'listing':listing})

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=city)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    return render(request,'listings/search.html',{
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'listings':queryset_list,
        'values': request.GET
    })