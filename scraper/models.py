from django.db import models

class Website(models.Model):
    url=models.URLField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class Page(models.Model):
    website=models.ForeignKey(Website,on_delete=models.CASCADE)
    page_url=models.URLField()
    depth=models.IntegerField()
    scraped_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_url


class Section(models.Model):
    page=models.ForeignKey(Page,on_delete=models.CASCADE)
    heading=models.TextField(blank=True)
    content=models.TextField()
    content_hash=models.CharField(max_length=64)
    scraped_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading if self.heading else "No Heading"
