import requests
import hashlib
from bs4 import BeautifulSoup
from collections import deque
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.utils import timezone
from scraper.models import Website,Page,Section
import difflib
from scraper.models import Page,Section

def get_driver():
    options=Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)

def fetch_html(url,driver=None):
    try:
        response=requests.get(url,timeout=10)
        if response.status_code==200 and len(response.text)>500:
            return response.text
    except:
        pass
    if driver:
        driver.get(url)
        return driver.page_source
    return None

def extract_sections(html):
    soup=BeautifulSoup(html,"html.parser")
    sections=[]
    headings=soup.find_all(["h1","h2","h3"])
    for heading in headings:
        content=[]
        for sib in heading.find_next_siblings():
            if sib.name in ["h1","h2","h3"]:
                break
            content.append(sib.get_text(strip=True))
        text=" ".join(content)
        if text:
            content_hash=hashlib.sha256(text.encode()).hexdigest()
            sections.append((heading.get_text(strip=True),text,content_hash))
    return sections

def extract_links(html):
    soup=BeautifulSoup(html,"html.parser")
    links=set()
    for a in soup.find_all("a",href=True):
        href=a["href"]
        if href.startswith("http"):
            links.add(href)
    return links

def crawl_website(start_url,max_depth=2):
    website,_=Website.objects.get_or_create(url=start_url)
    visited=set()
    queue=deque([(start_url,0)])
    driver=get_driver()
    while queue:
        url,depth=queue.popleft()
        if url in visited or depth>max_depth:
            continue
        visited.add(url)
        html=fetch_html(url,driver)
        if not html:
            continue
        page=Page.objects.create(
            website=website,
            page_url=url,
            depth=depth,
            scraped_at=timezone.now()
        )
        sections=extract_sections(html)
        changes=detect_changes(page,sections)
        for link in extract_links(html):
            queue.append((link,depth+1))
    driver.quit()

def detect_changes(page,sections):
    changes=[]
    existing_sections=Section.objects.filter(page=page)
    existing_map={}
    for sec in existing_sections:
        existing_map[sec.heading]=sec
    for heading,content,content_hash in sections:
        if heading in existing_map:
            old_section=existing_map[heading]
            if old_section.content_hash!=content_hash:
                diff="\n".join(difflib.unified_diff(
                    old_section.content.splitlines(),
                    content.splitlines(),
                    lineterm=""
                ))
                old_section.content=content
                old_section.content_hash=content_hash
                old_section.save()
                changes.append((heading,"CHANGED",diff))
            else:
                changes.append((heading,"UNCHANGED",""))
        else:
            Section.objects.create(
                page=page,
                heading=heading,
                content=content,
                content_hash=content_hash
            )
            changes.append((heading,"NEW",""))
    return changes
