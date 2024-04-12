from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Reservation

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully!')
        else:
            messages.error(request, 'Updating failed, please try again.')
    else:
        form = UserProfileForm(instance=profile)
    reservations = profile.reservations.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'reservations': reservations,
        'on_profile_page': True,
    }

    return render(request, template, context)


def reservation_history(request, reservation_number):
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)

    messages.info(request, (
        f'This is a previous confirmation for { reservation_number }.'
        'A confirmation email was sent on the reservation date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'reservation': reservation,
        'from_profile': True,
    }

    return render(request, template, context)