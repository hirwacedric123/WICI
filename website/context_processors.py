"""Expose official WICI Uganda contact details to all templates (single source of truth)."""


def site_contact(_request):
    return {
        "site_contact": {
            "physical_address": "Plot 29 Spine Road",
            "postal_address": "P.O Box 196112, Kampala",
            "email": "info@wiciuganda.org",
            "phones": [
                {"tel": "+256784565452", "display": "+256 784 565 452"},
                {"tel": "+256761664843", "display": "+256 761 664 843"},
            ],
            "maps_url": "https://maps.google.com/?q=Plot+29+Spine+Road,+Kampala,+Uganda",
        }
    }
