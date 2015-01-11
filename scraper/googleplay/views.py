from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from scraper.googleplay import HourlyGooglePlayScraper
from scraper.googleplay.models import GooglePlayTopFreeApps

__author__ = 'can'


'''
View for Crawled data
'''
class GooglePlayFreeAppListView(ListView):

    model = GooglePlayTopFreeApps
    template_name = "app_list.html"

    def get_context_data(self, **kwargs):
        context = super(GooglePlayFreeAppListView, self).get_context_data(**kwargs)

        if 'sort' in self.request.GET:
            app_list = self.model.objects.all().order_by(self.request.GET['sort'])
        else:
            app_list = self.model.objects.all()



        paginator = Paginator(app_list, 100) # Show 100 apps per page

        page = self.request.GET.get('page')
        try:
            apps = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            apps = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            apps = paginator.page(paginator.num_pages)


        context['apps'] = apps
        return context


def GooglePlayScraperRunner(request):

    scraper = GooglePlayScraperRunner()
    scraper.run()

    return HttpResponseRedirect('/googleplaytopfreeappslist/')