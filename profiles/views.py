from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully!')

    form = UserProfileForm(instance=profile)
    reservations = profile.reservations.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'reservations': reservations,
        'on_profile_page': True,
    }

    return render(request, template, context)