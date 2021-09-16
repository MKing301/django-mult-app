from django.shortcuts import render


def index(request):
    return render(request=request,
                  template_name="portfolio/index.html"
                )


def about(request):
    return render(request=request,
                  template_name="portfolio/about.html"
                )


def projects(request):
    return render(request=request,
                  template_name="portfolio/projects.html"
                )