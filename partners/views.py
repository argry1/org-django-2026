from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PartnerApplicationForm


@login_required
def partner_dashboard(request):
    if request.user.role != "partner":
        return redirect("home")

    if request.method == "POST":
        form = PartnerApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return redirect("partner_dashboard")

    else:
        form = PartnerApplicationForm()

    return render(
        request,
        "partners/dashboard.html",
        {"form": form},
    )