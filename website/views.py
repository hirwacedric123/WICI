from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.utils import timezone
from pathlib import Path

from .forms import ContactInquiryForm
from .models import MediaGalleryItem, Partner
from .partner_logos import PARTNER_LOGOS


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def programs(request):
    return render(request, 'website/programs.html')


def membership(request):
    return render(request, 'website/membership.html')


def partners(request):
    partners_list = Partner.objects.filter(is_active=True)
    context = {
        "partner_logos": PARTNER_LOGOS,
        "partners_list": partners_list,
    }
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


def media_gallery(request):
    media_items = MediaGalleryItem.objects.all()

    photos_dir = Path(settings.BASE_DIR) / "static" / "website" / "img" / "wiciphoto"
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}

    def sort_key(path_obj):
        stem = path_obj.stem
        return (0, int(stem)) if stem.isdigit() else (1, stem.lower())

    folder_photos = []
    if photos_dir.exists():
        photo_files = sorted(
            (
                path_obj
                for path_obj in photos_dir.iterdir()
                if path_obj.is_file() and path_obj.suffix.lower() in allowed_extensions
            ),
            key=sort_key,
        )
        folder_photos = [
            {
                "title": f"WICI Moment {index}",
                "caption": "Women in Construction & Infrastructure Uganda in action.",
                "image_url": static(f"website/img/wiciphoto/{path_obj.name}"),
            }
            for index, path_obj in enumerate(photo_files, start=1)
        ]

    gallery_items = folder_photos or list(media_items)
    return render(request, "website/media_gallery.html", {"gallery_items": gallery_items})
