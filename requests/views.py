from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


from .forms import HelpRequestForm
from .models import HelpRequest, Application
from django.utils import timezone




@login_required
def create_request(request):

    if request.user.role != "pensioner":
        return redirect("request_list")

    if request.method == "POST":
        form = HelpRequestForm(request.POST)

        if form.is_valid():
            help_request = form.save(commit=False)
            help_request.pensioner = request.user
            help_request.save()

            return redirect("request_list")

    else:
        form = HelpRequestForm()

    return render(
        request,
        "requests/request_create.html",
        {"form": form},
    )

def request_list(request):
    waiting_confirmation_ids = set()
    waiting_confirmation_requests = HelpRequest.objects.none()

    if not request.user.is_authenticated:
        requests = HelpRequest.objects.none()
        user_applications = set()
        in_progress_requests = HelpRequest.objects.none()
        completed_requests = HelpRequest.objects.none()

    elif request.user.role == "pensioner":
        requests = HelpRequest.objects.filter(
            pensioner=request.user
        ).order_by("-created_at")

        waiting_confirmation_ids = set(
            Application.objects.filter(
                request__pensioner=request.user,
                status=Application.Status.WAITING_CONFIRMATION,
            ).values_list("request_id", flat=True)
        )

        user_applications = set()
        in_progress_requests = HelpRequest.objects.none()
        completed_requests = HelpRequest.objects.none()

    elif request.user.role == "admin":
        requests = HelpRequest.objects.all().order_by("-created_at")

        user_applications = set()
        in_progress_requests = HelpRequest.objects.none()
        waiting_confirmation_requests = HelpRequest.objects.none()
        completed_requests = HelpRequest.objects.none()

    elif request.user.role == "volunteer":
        requests = HelpRequest.objects.filter(
            status=HelpRequest.Status.OPEN
        ).order_by("-created_at")

        user_applications = set(
            Application.objects.filter(
                volunteer=request.user
            ).values_list("request_id", flat=True)
        )

        in_progress_requests = HelpRequest.objects.filter(
            applications__volunteer=request.user,
            applications__status=Application.Status.ACCEPTED,
            status=HelpRequest.Status.IN_PROGRESS,
        ).distinct().order_by("-created_at")

        waiting_confirmation_requests = HelpRequest.objects.filter(
            applications__volunteer=request.user,
            applications__status=Application.Status.WAITING_CONFIRMATION,
            status=HelpRequest.Status.IN_PROGRESS,
        ).distinct().order_by("-created_at")

        completed_requests = HelpRequest.objects.filter(
            applications__volunteer=request.user,
            applications__status=Application.Status.COMPLETED,
            status=HelpRequest.Status.COMPLETED,
        ).distinct().order_by("-created_at")

    else:
        requests = HelpRequest.objects.none()
        user_applications = set()
        in_progress_requests = HelpRequest.objects.none()
        completed_requests = HelpRequest.objects.none()

    return render(
        request,
        "requests/request_list.html",
        {
            "requests": requests,
            "user_applications": user_applications,
            "in_progress_requests": in_progress_requests,
            "completed_requests": completed_requests,
            "waiting_confirmation_ids": waiting_confirmation_ids,
            "waiting_confirmation_requests": waiting_confirmation_requests,
        },
    )

@login_required
def apply_to_request(request, request_id):
    if request.user.role != "volunteer":
        return redirect("request_list")

    help_request = get_object_or_404(
        HelpRequest,
        id=request_id,
        status=HelpRequest.Status.OPEN,
    )

    existing_application = Application.objects.filter(
        request=help_request,
        volunteer=request.user,
    ).exists()

    if not existing_application:
        Application.objects.create(
            request=help_request,
            volunteer=request.user,
            status=Application.Status.ACCEPTED,
        )

        help_request.status = HelpRequest.Status.IN_PROGRESS
        help_request.save(update_fields=["status"])

    return redirect("request_list")

@login_required
def complete_request(request, request_id):
    if request.user.role != "volunteer":
        return redirect("request_list")

    help_request = get_object_or_404(
        HelpRequest,
        id=request_id,
        status=HelpRequest.Status.IN_PROGRESS,
        applications__volunteer=request.user,
        applications__status=Application.Status.ACCEPTED,
    )

    Application.objects.filter(
        request=help_request,
        volunteer=request.user,
        status=Application.Status.ACCEPTED,
    ).update(
        status=Application.Status.WAITING_CONFIRMATION
    )

    return redirect("request_list")

@login_required
def confirm_request(request, request_id):
    if request.user.role != "pensioner":
        return redirect("request_list")

    help_request = get_object_or_404(
        HelpRequest,
        id=request_id,
        pensioner=request.user,
        status=HelpRequest.Status.IN_PROGRESS,
        applications__status=Application.Status.WAITING_CONFIRMATION,
    )

    help_request.status = HelpRequest.Status.COMPLETED
    help_request.completed_at = timezone.now()
    help_request.save(
        update_fields=["status", "completed_at"]
    )

    Application.objects.filter(
        request=help_request,
        status=Application.Status.WAITING_CONFIRMATION,
    ).update(
        status=Application.Status.COMPLETED
    )

    return redirect("request_list")

@login_required
def edit_request(request, request_id):
    if request.user.role != "admin":
        return redirect("request_list")

    help_request = get_object_or_404(
        HelpRequest,
        id=request_id,
    )

    if request.method == "POST":
        help_request.title = request.POST.get("title")
        help_request.description = request.POST.get("description")
        help_request.status = request.POST.get("status")

        help_request.save()

    return redirect("request_list")