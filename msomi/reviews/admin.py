from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
                            BookContributor, Review)
from django.contrib.admin import AdminSite


class BookAdminSite(AdminSite):
    title_header = 'Msomi'
    site_header = 'Msomi Administrator'
    index_title = 'Msomi Site Admin'


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('id', 'title', 'isbn')
    list_filter = ('publisher', 'publication_date')


def initialled_name(obj):
    """ obj.first_names='Jerome David', obj.last_names='Salinger'
        => 'Salinger, JD' """
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'email')


# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
admin_site = BookAdminSite(name='Msomi')
