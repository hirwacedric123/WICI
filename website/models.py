from django.db import models


class PublishedModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    summary = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title


class Event(PublishedModel):
    event_date = models.DateField()
    location = models.CharField(max_length=180, blank=True)
    details = models.TextField(blank=True)

    class Meta(PublishedModel.Meta):
        ordering = ["event_date", "-created_at"]


class NewsUpdate(PublishedModel):
    body = models.TextField()
    author = models.CharField(max_length=120, blank=True)


class LeadershipProfile(models.Model):
    full_name = models.CharField(max_length=140)
    role_title = models.CharField(max_length=180)
    bio = models.TextField()
    photo_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "full_name"]

    def __str__(self):
        return f"{self.full_name} - {self.role_title}"


class Partner(models.Model):
    name = models.CharField(max_length=180)
    category = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class Resource(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    resource_url = models.URLField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.title


class MediaGalleryItem(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField(blank=True)
    image_url = models.URLField()
    event_name = models.CharField(max_length=180, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ContactInquiry(models.Model):
    INQUIRY_TYPES = [
        ("membership", "Membership"),
        ("partnership", "Partnership"),
        ("events", "Events"),
        ("general", "General Inquiry"),
    ]

    full_name = models.CharField(max_length=140)
    email = models.EmailField()
    organization = models.CharField(max_length=180, blank=True)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.get_inquiry_type_display()})"
