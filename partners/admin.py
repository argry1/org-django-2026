from django.contrib import admin

from .models import Partner, PartnerOffer



from django.contrib import admin

from .models import Partner, PartnerOffer, PartnerApplication


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("organization_name", "owner", "phone")


@admin.register(PartnerOffer)
class PartnerOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "partner", "points_cost", "is_active")


@admin.register(PartnerApplication)
class PartnerApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "email", "message")