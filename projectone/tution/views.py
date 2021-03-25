from django.shortcuts import render
from .models import Contact
from .forms import contactForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})
