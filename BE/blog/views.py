import datetime

from django.views.generic import DetailView, ListView

from .models import Article, City, Country
from forms.forms import CommentForm


class BlogHomePageView(ListView):
    template_name = "blog/blog_home.html"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(publish_on__lte=datetime.date.today()).order_by(
            "-publish_on", "created_at"
        )


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["site"] = f"https://easy-snack.com/"
        return context


class CityHomePageView(ListView):
    queryset = City.objects.all()
    template_name = "blog/city_home.html"


class CityDetailView(DetailView):
    model = City
    template_name = "blog/city_detail.html"


class CountryHomePageView(ListView):
    queryset = Country.objects.all()
    template_name = "blog/country_home.html"


class CountryDetailView(DetailView):
    model = Country
    template_name = "blog/country_detail.html"
