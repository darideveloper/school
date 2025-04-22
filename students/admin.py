from students import models

from django.contrib import admin


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(models.Percentage)
class PercentageAdmin(admin.ModelAdmin):
    list_display = (
        "group",
        "partial",
        "exam_points",
        "assistances_amount",
        "exam_percentage",
        "assistances_percentage",
        "homework_percentage",
        "class_work_percentage",
    )
    ordering = ("group", "partial")
    list_filter = ("group", "partial")
    search_fields = ("group__name",)
    list_per_page = 10
    list_editable = (
        "exam_points",
        "assistances_amount",
        "exam_percentage",
        "assistances_percentage",
        "homework_percentage",
        "class_work_percentage",
    )


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("group", "first_name", "last_name", "age", "email")
    ordering = ("group", "first_name")
    list_filter = ("group",)
    search_fields = ("first_name", "last_name", "group__name")
    list_per_page = 10
