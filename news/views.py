import csv
import pandas as pd
from django.shortcuts import render
from .models import Article

def count_links(file):
    df = pd.read_csv(file,encoding='utf-8')
    link_counts = {}
    for i in range(len(df["read_more"])):
        if df["read_more"][i]:
            if len(df["read_more"][i].split("/")) > 2:
                link = df["read_more"][i].split("/")[2]
                if link == "www.hindustantimes.com":
                    link_counts["Hindustantimes"] = link_counts.get("Hindustantimes", 0) + 1
                elif link == "www.thenewsminute.com":
                    link_counts["thenewsminute"] = link_counts.get("thenewsminute", 0) + 1
                elif link == "www.reuters.com":
                    link_counts["Reuters"] = link_counts.get("Reuters", 0) + 1
                elif link == "www.aninews.in":
                    link_counts["Aninews"] = link_counts.get("Aninews", 0) + 1
                elif link == "theprint.in":
                    link_counts["Theprint"] = link_counts.get("Theprint", 0) + 1
                elif link == "www.news18.com":
                    link_counts["News18"] = link_counts.get("News18", 0) + 1
                elif link == "www.independent.co.uk":
                    link_counts["Independent"] = link_counts.get("Independent", 0) + 1
                elif link == "www.timesnownews.com":
                    link_counts["Timesnow"] = link_counts.get("Timesnow", 0) + 1

    multiple_counts = {k: v for k, v in link_counts.items() if v > 1}
    return multiple_counts

def render_content(filename):
    articles = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            article = Article(
                headline=row['headlines'],
                date = row['date'],
                time = row['time'],
                image_url=row['image_url'],
                text=row['summary'],
                read_more_url=row['read_more']
            )
            articles.append(article) 
    return articles

def news(request):
    title = 'News Select'
    return render(request, 'news_main.html',{'title':title})

def article_misc(request):
    file_misc =  'project/media/output_misc_fin.csv'
    articles = render_content(file_misc)
    link_counts = count_links(file_misc)
    return render(request, 'news.html', {'articles': articles, 'link_counts': link_counts})
def article_pol(request):
    file_misc =  'project/media/output_pol_fin.csv'
    articles = render_content(file_misc)
    link_counts = count_links(file_misc)
    return render(request, 'news.html', {'articles': articles, 'link_counts': link_counts})
def article_world(request):
    file_misc =  'project/media/output_worl_fin.csv'
    articles = render_content(file_misc)
    link_counts = count_links(file_misc)
    return render(request, 'news.html', {'articles': articles, 'link_counts': link_counts})

def article_tech(request):
    file_misc =  'project/media/output_tech_fin.csv'
    articles = render_content(file_misc)
    link_counts = count_links(file_misc)
    return render(request, 'news.html', {'articles': articles, 'link_counts': link_counts})