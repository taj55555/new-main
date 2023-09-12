from django.urls import path
from . import views

urlpatterns = [
    path('client-profile/', views.ClientProfileRetrieveUpdateDestroyAPIView.as_view(), name='client-profile'),
    path('user-profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('contact/', views.ContactCreateAPIView.as_view(), name='contact-create'),
    path('contact-list/', views.ContactListAPIView.as_view(), name='contact-list'),
    path('contact-list/<int:contact_id>/', views.ContactRetrieveAPIView.as_view(), name='contact-details'),
    path('service-category/', views.ServiceCategoryListCreateAPIView.as_view(), name='service-category-list-create'),
    path('service-category/<slug:slug>/', views.ServiceCategoryRetrieveUpdateDestroyAPIView.as_view(), name='service-category-retrieve-update-destroy'),
    path('projects/', views.ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<slug:slug>/', views.ProjectRetrieveCreateAPIView.as_view(), name='project-detail'),
    path('customer-support/', views.CustomerSupportListCreateAPIView.as_view(), name='customer-support-list-create'),
    path('customer-support/<int:msg_id>/', views.CustomerSupportDetailAPIView.as_view(), name='customer-support-details'),
    path('customer-support-admin-seen-list/', views.CustomerSupportListAPIViewAdminSeen.as_view(), name='customer-support-admin-seen-list'),
    path('customer-support-admin-unseen-list/', views.CustomerSupportListAPIViewAdminUnseen.as_view(), name='customer-support-admin-unseen-list'),
    path('customer-support-for-admin/', views.CustomerSupportListAPIViewForAdmin.as_view(), name='customer-support-list-for-admin-seen'),
    path('customer-support-for-admin/<int:msg_id>/', views.CustomerSupportDetailAPIViewForAdmin.as_view(), name='customer-support-details-for-admin-seen'),
    path('customer-support-reply/<int:msg_id>/', views.CustomerSupportReplyMessageAPIView.as_view(), name='customer-support-reply'),
    path('our-team/', views.OurTeamListCreateAPIView.as_view(), name='our-team-list-create'),
    path('course-type/', views.CourseTypeListCreateAPIView.as_view(), name='course-type-list-create'),
    path('course-type/<slug:slug>/', views.CourseTypeRetrieveUpdateDestroyAPIView.as_view(), name='course-type-retrieve-update-destroy'),
    path('courses/', views.CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<slug:type_slug>/<slug:course_slug>/', views.CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-retrieve-update-destroy'),
    path('available-time-slot/', views.AvailableTimeSlotListCreateAPIView.as_view(), name='available-time-slot-list-create'),
    path('booking-time-slot/', views.BookingTimeSlotListCreateAPIView.as_view(), name='booking-time-slot-list-create'),

    path('subscribe-email/create/', views.SubscribeEmailCreateView.as_view(), name='subscribe-email-create'),
    path('subscribe-email/list/', views.SubscribeEmailListView.as_view(), name='subscribe-email-list'),
    path('why-choose-us/', views.WhyChoseUsListCreateView.as_view(), name='why-choose-us-list-create'),
    path('why-choose-us/<slug:slug>/', views.WhyChoseUsListDetailView.as_view(), name='why-choose-us-details'),
    path('about-us/', views.AboutUsListCreateView.as_view(), name='about-us-list-create'),
    path('about-us/<slug:slug>//', views.AboutUsDetailsView.as_view(), name='about-us-details'),
    path('contact-and-address/', views.ContactAndAddressListCreateView.as_view(), name='contact-and-address-list-create'),

    path('picture-gallery/', views.pictureGalleryListCreateView.as_view(), name='picture-gallery-list-create'),
    path('picture-gallery/<int:id>/', views.pictureGalleryDetailView.as_view(), name='picture-gallery-detail'),
    path('live-links/', views.LiveLinkListCreateView.as_view(), name='live-link-list-create'),
    path('live-links/<int:id>/', views.LiveLinkDetailView.as_view(), name='live-link-detail'),

    path('home-page-content-type/', views.HomePageContentTypeListCreateAPIView.as_view(), name='home-page-content-type-list-create'),
    path('home-page-content-type/<int:type_id>/', views.HomePageContentTypeRetrieveUpdateDestroyAPIView.as_view(), name='home-page-content-type-retrieve-update-destroy'),
    path('home-page-content/', views.HomePageContentListCreateAPIView.as_view(), name='home-page-content-list-create'),
    path('home-page-content/<int:type_id>/<int:content_id>/', views.HomePageContentRetrieveUpdateDestroyAPIView.as_view(), name='home-page-content-retrieve-update-destroy'),
    
    




]
