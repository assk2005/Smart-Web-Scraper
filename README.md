# 🕸️ Smart Web Scraper
**Web Scraping & Change Monitoring System**

---

## 📌 Project Overview

**Smart Web Scraper** is a web-based application designed to automatically scrape website content, monitor changes over time, and export structured data for further analysis.  
The system supports both **static and dynamic websites**, stores data in a relational database, and provides a **modern user interface** for real-time usability.

This project was developed as a **college mini project** with emphasis on real-world applicability, clean architecture, and explainable logic.

---

## 🎯 Problem Statement

Manually monitoring websites for content updates is:
- Time-consuming  
- Error-prone  
- Not scalable  

Websites such as documentation portals, policy pages, and knowledge bases update content frequently without notifications.  
There is a need for an **automated system** that can extract, track, and export web data in a structured format.

---

## ✅ Solution Approach

The Smart Web Scraper automates this process by:
- Crawling websites up to a defined depth
- Extracting content section-wise
- Detecting content changes using hashing
- Storing results in a database
- Providing CSV and JSON exports via a web interface

---

## 🧠 Key Features

- 🌐 Scrape any public website
- 🔁 Depth-limited crawling to avoid infinite loops
- ⚙️ Hybrid scraping:
  - Requests + BeautifulSoup for static pages
  - Selenium WebDriver for dynamic pages
- 📄 Section-wise content extraction
- 🔍 Change detection using SHA-256 hashing
- 🗄️ MySQL database storage
- 🎨 Modern Bootstrap-based UI
- 📤 Export data as CSV and JSON
- 🧪 Tested on real-world websites (Wikipedia, policy portals)

---

## 🛠️ Technology Stack

### Backend
- Python
- Django – web framework for routing, views, and ORM

### Scraping
- Requests – static HTML fetching
- BeautifulSoup – HTML parsing
- Selenium WebDriver – JavaScript-rendered content

### Database
- MySQL – relational data storage

### Frontend
- Bootstrap 5
- HTML & CSS (Django templates)

### Utilities
- hashlib (SHA-256)
- csv, json modules

---

## 🏗️ System Architecture

User Interface (Bootstrap)  
↓  
Django Views  
↓  
Scraping Engine (Requests / Selenium)  
↓  
Section Extractor  
↓  
Change Detection (Hash Comparison)  
↓  
MySQL Database  
↓  
Export Module (CSV / JSON)

---

## 🔄 Project Phases

### Phase 1: Requirement Analysis & Design
- Identified real-world scraping use cases
- Designed modular system architecture
- Planned database schema

### Phase 2: Backend Development

**Phase 2A – Project Setup**
- Django project initialization
- MySQL configuration

**Phase 2B – Database Models**
- Website: stores target URLs
- Page: stores crawled pages and depth
- Section: stores headings, content, and hashes

**Phase 2C – Scraping Engine**
- Breadth-First Search (BFS) crawling
- Depth-limited traversal
- Hybrid scraping logic
- Section extraction using h1–h3 tags

**Phase 2D – Change Detection**
- SHA-256 hash generation for sections
- Hash comparison across scrapes
- Updates only modified content

### Phase 3: Frontend & Export

**Phase 3A – User Interface**
- Bootstrap-based clean UI
- URL input and crawl depth selection
- Results displayed in tables

**Phase 3B – Export Module**
- CSV export for spreadsheets
- JSON export for APIs and analysis

---

## 🌍 Real-World Testing

### Wikipedia
- Successfully scraped large articles
- Clear section hierarchy
- Ideal demonstration site

Example:
https://en.wikipedia.org/wiki/Web_scraping

### Policy & Documentation Sites
- Government and institutional portals
- Long headings handled correctly

### E-commerce Websites
- Demo sites (BooksToScrape): Supported
- Large platforms (Amazon, Flipkart): Limited due to anti-bot protections

---

## ⚠️ Limitations

- Does not bypass anti-scraping mechanisms
- Infinite scrolling pages have limited support
- Scraping is manually triggered
- Large commercial platforms restrict automated access

These limitations are intentionally respected for ethical and academic reasons.

---

## 🚀 Future Enhancements

- Scheduled scraping with background tasks
- Notification alerts for content changes
- User authentication and dashboards
- AI-based content summarization
- Advanced analytics and visualization

---

## ▶️ How to Run the Project

1. Clone the repository
2. Install dependencies
3. Configure MySQL database
4. Run migrations
5. Start the Django server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open browser:
http://127.0.0.1:8000/

---

## 📌 Conclusion

Smart Web Scraper provides an automated, scalable, and practical solution for web data extraction and monitoring.  
The project demonstrates real-world usability and is suitable for academic, research, and learning purposes.
