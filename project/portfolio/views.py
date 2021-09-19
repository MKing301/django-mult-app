from django.shortcuts import redirect, render
from .models import Contact
from .forms import ContactForm


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


def contact(request):
      if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return 'hello'

      # if a GET (or any other method) we'll create a blank form
      else:
          form = ContactForm()

      return render(request=request,
                    template_name="portfolio/contact.html",
                    context={'form': form}
                  )