from multiprocessing import context
from . models import CompanyProfile, Categories, Content

def empire(request):
    bloger = CompanyProfile.objects.get(pk=1)

    context = {
        'bloger':bloger
    }

    return context

def category(request):
    categories = Categories.objects.all()

    context = {
        'categories':categories,
    }

    return context 