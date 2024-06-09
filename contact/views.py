from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactDetailsForm


def contact(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')


def contact_form(request):
    """ Users can send a contact request to studio """
    form = ContactDetailsForm()

    if request.method == 'POST':
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Message Sent! \
                We will reply to you as soon as possible.')
            form.save()
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Message not sent, please try again!')
    else:
        form = ContactDetailsForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
