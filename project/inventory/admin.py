from django.contrib import admin
from .models import (
    MapLocation,
    Area,
    Manufacturer,
    InventoryItem,
    ApprovalList,
    Assignee,
    ItemStatus,
    ItemNotes
    )


admin.site.register(MapLocation)
admin.site.register(Area)
admin.site.register(Manufacturer)
admin.site.register(InventoryItem)
admin.site.register(ApprovalList)
admin.site.register(Assignee)
admin.site.register(ItemStatus)
admin.site.register(ItemNotes)
