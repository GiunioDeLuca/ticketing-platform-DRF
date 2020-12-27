from django.contrib import admin
from .models import Stadium, Match, Ticket, Customer


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity', 'matches']

    def matches(self, obj):
        return "zozzo"



@admin.register(Match)
class MatchesAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass