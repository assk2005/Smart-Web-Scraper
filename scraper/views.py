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


def export_csv(request):
    import csv
    from django.http import HttpResponse
    response=HttpResponse(content_type="text/csv")
    response["Content-Disposition"]="attachment; filename=scraped_data.csv"
    writer=csv.writer(response)
    writer.writerow(["Website","Page URL","Section","Content","Scraped At"])
    for sec in Section.objects.all():
        writer.writerow([
            sec.page.website.url,
            sec.page.page_url,
            sec.heading,
            sec.content,
            sec.scraped_at
        ])
    return response


def export_json(request):
    import json
    from django.http import HttpResponse
    data=[]
    for sec in Section.objects.all():
        data.append({
            "website":sec.page.website.url,
            "page_url":sec.page.page_url,
            "section":sec.heading,
            "content":sec.content,
            "scraped_at":str(sec.scraped_at)
        })
    response=HttpResponse(
        json.dumps(data,indent=4),
        content_type="application/json"
    )
    response["Content-Disposition"]="attachment; filename=scraped_data.json"
    return response
