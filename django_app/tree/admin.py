from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Menu

admin.site.register(
    Menu,
    DraggableMPTTAdmin,
    list_display=(
        'id',
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),
)

