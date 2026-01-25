from django.urls import path
from scraper.views import home,export_csv,export_json

urlpatterns=[
    path("",home,name="home"),
    path("export/csv/",export_csv,name="export_csv"),
    path("export/json/",export_json,name="export_json"),
]
