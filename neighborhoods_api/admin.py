from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BoardMinutes, Blog1, Blog2, Blog1Category, Blog2Category

class BoardMinutesAdmin(admin.ModelAdmin):
    list_display = ['neighborhood', 'date']
    fields = ['date', 'content', 'file']

    def save_model(self, request, obj, form, change):
        # Automatically set the neighborhood based on the user's group
        obj.neighborhood = request.user.groups.first()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Filter objects based on the user's neighborhood
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(neighborhood=request.user.groups.first())
        return queryset

class Blog1Admin(admin.ModelAdmin):
    list_display = ['neighborhood', 'title', 'created_at', 'updated_at']
    fields = ['title', 'content', 'categories']

    def save_model(self, request, obj, form, change):
        # Automatically set the neighborhood based on the user's group
        obj.neighborhood = request.user.groups.first()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Filter objects based on the user's neighborhood
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(neighborhood=request.user.groups.first())
        return queryset

class Blog2Admin(admin.ModelAdmin):
    list_display = ['neighborhood', 'title', 'created_at', 'updated_at']
    fields = ['title', 'content', 'categories']

    def save_model(self, request, obj, form, change):
        # Automatically set the neighborhood based on the user's group
        obj.neighborhood = request.user.groups.first()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Filter objects based on the user's neighborhood
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(neighborhood=request.user.groups.first())
        return queryset

class Blog1CategoryAdmin(admin.ModelAdmin):
    list_display = ['neighborhood', 'name']

    def save_model(self, request, obj, form, change):
        # Automatically set the neighborhood based on the user's group
        obj.neighborhood = request.user.groups.first()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Filter categories based on the user's neighborhood
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(neighborhood=request.user.groups.first())
        return queryset

class Blog2CategoryAdmin(admin.ModelAdmin):
    list_display = ['neighborhood', 'name']

    def save_model(self, request, obj, form, change):
        # Automatically set the neighborhood based on the user's group
        obj.neighborhood = request.user.groups.first()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Filter categories based on the user's neighborhood
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(neighborhood=request.user.groups.first())
        return queryset

# Register the custom admin classes
admin.site.register(BoardMinutes, BoardMinutesAdmin)
admin.site.register(Blog1, Blog1Admin)
admin.site.register(Blog2, Blog2Admin)
admin.site.register(Blog1Category, Blog1CategoryAdmin)
admin.site.register(Blog2Category, Blog2CategoryAdmin)
