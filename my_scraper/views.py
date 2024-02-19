from django.http import HttpResponseRedirect
from django.shortcuts import render
from scrapy.crawler import CrawlerProcess

from .forms import LinkForm
from .models import ScrapedItem
from .scrape import Spider
def home_page(request):
    return render(request, 'home.html')

def scrape_view(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            process = CrawlerProcess(settings={
                'USER_AGENT': 'Mozilla/5.0',
            })
            process.crawl(Spider, start_urls=[url])
            process.start()
            return HttpResponseRedirect('/result')
    else:
        form = LinkForm()
    return render(request, 'form.html', {'form': form})

def scrape_view_result(request):
    scraped_data = ScrapedItem.objects.all()
    return render(request, 'result.html', {'scraped_data': scraped_data})