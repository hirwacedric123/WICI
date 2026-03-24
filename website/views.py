from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import ContactInquiryForm
from .models import Event, LeadershipProfile, MediaGalleryItem, NewsUpdate, Partner, Resource


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def programs(request):
    return render(request, 'website/programs.html')


def events(request):
    upcoming_events = Event.objects.filter(is_published=True, event_date__gte=timezone.now().date())
    recent_events = Event.objects.filter(is_published=True, event_date__lt=timezone.now().date())[:6]
    context = {
        "upcoming_events": upcoming_events,
        "recent_events": recent_events,
    }
    return render(request, "website/events.html", context)


def membership(request):
    return render(request, 'website/membership.html')


def partners(request):
    partners_list = Partner.objects.filter(is_active=True)
    context = {"partners_list": partners_list}
    return render(request, "website/partners.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully. We will contact you soon.")
            return redirect("contact")
    else:
        form = ContactInquiryForm()

    return render(request, "website/contact.html", {"form": form})


def news(request):
    updates = NewsUpdate.objects.filter(is_published=True)
    return render(request, "website/news.html", {"updates": updates})


def leadership(request):
    leaders = LeadershipProfile.objects.filter(is_active=True)
    return render(request, "website/leadership.html", {"leaders": leaders})


def resources(request):
    resource_items = Resource.objects.all()
    return render(request, "website/resources.html", {"resource_items": resource_items})


def media_gallery(request):
    media_items = MediaGalleryItem.objects.all()
    return render(request, "website/media_gallery.html", {"media_items": media_items})
