from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def productlistview(request):
    return render(request, 'productlist.html')

def supplierlistview(request):
    muuttuja = "Merkkijono \o/"
    another = "Second one!"
    context = {'x': muuttuja, 'y':another}
    return render(request, 'supplierlist.html', context)


