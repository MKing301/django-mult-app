import requests
import os

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

              ''' Begin reCAPTCHA validation '''
              recaptcha_response = request.POST.get('g-recaptcha-response')
              data = {
                  'secret': os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY'),
                  'response': recaptcha_response
              }
              r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
              result = r.json()
              ''' End reCAPTCHA validation '''

              if result['success']:
                    form.save()

              return redirect("/")

      # if a GET (or any other method) we'll create a blank form
      else:
          form = ContactForm()

      return render(request=request,
                    template_name="portfolio/contact.html",
                    context={'form': form, "sitekey": os.environ.get('GOOGLE_RECAPTCHA_SITE_KEY')}
                  )