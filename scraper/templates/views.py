from django.shortcuts import render
from scraper.services.crawler import crawl_website
from scraper.models import Section

def home(request):
    if request.method=="POST":
        url=request.POST.get("url")
        depth=int(request.POST.get("depth"))
        crawl_website(url,depth)
        sections=Section.objects.all().order_by("-scraped_at")[:100]
        return render(request,"scraper/results.html",{"sections":sections})
    return render(request,"scraper/home.html")
