from django.contrib import admin
from .models import (
    ClientProfile, Contact, HomePageContentType, HomePageContent,
    ServiceCategory, Project, CustomerSupport,
    OurTeam, CourseType, Course, AvailableTimeSlot, BookingTimeSlot
)

# # Register your models here

# @admin.register(ClientProfile)
# class ClientProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'full_name', 'city', 'phone')
#     search_fields = ('user__username', 'full_name', 'city', 'phone')

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('email', 'phone', 'subject','details','attachment','site_url', 'created_at')
#     search_fields = ('email', 'phone', 'subject')

# @admin.register(HomePageContentType)
# class HomePageContentTypeAdmin(admin.ModelAdmin):
#     list_display = ('category_name', 'description', 'created_at')

# @admin.register(HomePageContent)
# class HomePageContentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'priority', 'created_at')

# @admin.register(ServiceCategory)
# class ServiceCategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'created_at')


# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('project_title', 'client', 'service', 'start_date', 'status', 'created_at')

# @admin.register(CustomerSupport)
# class CustomerSupportAdmin(admin.ModelAdmin):
#     list_display = ('Problem_title', 'client', 'service', 'status', 'created_at')

# @admin.register(OurTeam)
# class OurTeamAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'position', 'status')

# @admin.register(CourseType)
# class CourseTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at')

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'course_type', 'start_date', 'end_date', 'price', 'created_at')

# @admin.register(AvailableTimeSlot)
# class AvailableTimeSlotAdmin(admin.ModelAdmin):
#     list_display = ('date', 'start_time', 'end_time')

# @admin.register(BookingTimeSlot)
# class BookingTimeSlotAdmin(admin.ModelAdmin):
#     list_display = ('user', 'time_slot', 'created_at')

