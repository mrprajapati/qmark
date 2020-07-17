from django.contrib import admin
from news.models import News


# @admin.register(Object)
class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'create_at', 'update_at',)

    search_fields = ['title']

    list_filter = ['create_at', ]

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ['create_at', 'author']
        else:
            return ['create_at']
    # Return user crated post only

    def get_queryset(self, request):
        qs = super(NewsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # save current user as Author
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(News, NewsAdmin)


admin.site.site_header = "Qmark Admin"
