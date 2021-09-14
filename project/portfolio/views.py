from django.shortcuts import render


def index(request):
    return render(request=request,
                  template_name="portfolio/index.html"
                )