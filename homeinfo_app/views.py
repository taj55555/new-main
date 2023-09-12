from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .permissions import IsOwner,IsOwnerOrReadOnly,IsAdminOrOwner,IsAdminOrReadOnly
from rest_framework.generics import get_object_or_404

from .models import (
    ClientProfile, Contact, HomePageContentType, HomePageContent,
    ServiceCategory, Project, CustomerSupport,SubscribeEmail,CustomerSupportReply,
    OurTeam, CourseType, Course, AvailableTimeSlot, BookingTimeSlot,UserIp,UserIpV,WhyChoseUs, 
    AboutUs, ContactAndAddress,pictureGallery, LiveLink
)

from .serializers import (
    ClientProfileSerializer, ContactSerializer, HomePageContentTypeSerializer,
    HomePageContentSerializer, ServiceCategorySerializer,ProjectSerializer, 
    CustomerSupportSerializer, OurTeamSerializer,CourseTypeSerializer, CourseSerializer, 
    AvailableTimeSlotSerializer,BookingTimeSlotSerializer,CourseTypeRetrieveSerializer,
    HomePageContentTypeRetrieveSerializer,CustomerSupportSerializerDetail,CustomerSupportReplySerializer,
    WhyChoseUsSerializer,AboutUsSerializer,ContactAndAddressSerializer,SubscribeEmailSerializer,LiveLinkSerializer,
    pictureGallerySerializer
)
from authentiation_app.models import User
import datetime
from django.utils import timezone
import requests,json


def trace_user_ip(request):
    # for user ip address trace (another one func like get_client_ip function)
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    uip = requests.get(f'http://ip-api.com/json/{ip}')
    response = uip.json()

    status = response.get('status')
    query = response.get('query')
    country = response.get('country')
    city = response.get('city')
    regionName = response.get('regionName')

    if status != 'fail':
        UserIpV.objects.get_or_create(
            user_ip=query,
            defaults={
                'country': country,
                'division': regionName,
                'city': city,
                'zip_code': response.get('zip'),
                'latitude': response.get('lat'),
                'longitude': response.get('lon'),
                'isp': response.get('isp'),
                'organization': response.get('org'),
                'timezone': response.get('timezone'),
                'date': timezone.now()
            }
        )
    else:
        UserIpV.objects.get_or_create(
            user_ip='traking not possible',
            defaults={'date': timezone.now()}
        )

    return response


def get_client_ip(request):
    
    # for user ip address trace (another one func like trace_user_ip function)
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    return ip, data.get("city"), data.get("region"), data.get("country")


def some_view(request):
    user_ip,city, region, country = get_client_ip(request)



def get_ip_address(request):
# for user ip address trace (another one func like trace_user_ip function from ott project copy)
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    uip = requests.get(f'http://ip-api.com/json/{ip}')
    response =json.loads(uip.content)

    status = response.get('status')
    query = response.get('query')
    country = response.get('country')
    city = response.get('city')
    regionName = response.get('regionName')

    if status != 'fail':
        if UserIp.objects.filter(user_ip=query,country=country,city=city,division=regionName).exists():
            UserIp.objects.get_or_create(user_ip=query,country=country,city=city,division=regionName,date=timezone.now())
        else:
            UserIp.objects.get_or_create(user_ip=query,country=country,city=city,division=regionName,date=timezone.now())
    else:
        if UserIp.objects.filter(user_ip='traking not possible').exists():
            UserIp.objects.update(user_ip='traking not possible',date=timezone.now())
        else:
            UserIp.objects.get_or_create(user_ip='traking not possible',date=timezone.now())
    return response





class ClientProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # for client profile Retrieve Update
    queryset = ClientProfile.objects.filter()
    serializer_class = ClientProfileSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)
    
    def get_object(self):
        user = user=self.request.user
        if not user.is_staff:
            obj, created = ClientProfile.objects.get_or_create(user=user)
            return obj
        return get_object_or_404(self.queryset,user=user)


class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            obj, created = ClientProfile.objects.get_or_create(user=request.user)
            serializer = ClientProfileSerializer(instance=obj)
        if request.user.is_staff:
            obj, created = OurTeam.objects.get_or_create(user=request.user)
            serializer = OurTeamSerializer(instance=obj)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        
        if not request.user.is_staff:
            obj, created = ClientProfile.objects.get_or_create(user=request.user)
            serializer = ClientProfileSerializer(instance=obj, data=request.data)
        if request.user.is_staff:
            obj, created = OurTeam.objects.get_or_create(user=request.user)
            serializer = OurTeamSerializer(instance=obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class ContactCreateAPIView(generics.CreateAPIView):
    # Create Contact anon user with admin 
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny,)


class ContactListAPIView(generics.ListAPIView):
    # List Contact anon user with admin  
    queryset = Contact.objects.filter()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,permissions.IsAdminUser)


class ContactRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Retrieve Contact anon user with admin  
    queryset = Contact.objects.filter()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAdminUser)
    
    def get_object(self):
        contact_id = self.kwargs.get('contact_id', None)
        return get_object_or_404(self.queryset,id=contact_id)


class ServiceCategoryListCreateAPIView(generics.ListCreateAPIView):
    # Provided services List & create
    
    queryset = ServiceCategory.objects.filter()
    serializer_class = ServiceCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ServiceCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Provided services Retrieve Update Destroy

    queryset = ServiceCategory.objects.filter()
    serializer_class = ServiceCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        slug = self.kwargs.get('slug', None)
        return get_object_or_404(self.queryset,slug=slug)



class ProjectListCreateAPIView(generics.ListCreateAPIView):
    # our existing project
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProjectRetrieveCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    # our existing project
    
    queryset = Project.objects.select_related('client_project','services_project')
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        slug = self.kwargs.get('slug', None)
        return get_object_or_404(self.queryset,slug=slug)



class CustomerSupportListCreateAPIView(generics.ListCreateAPIView):
    # Customer support msg list create for client (owner)
    queryset = CustomerSupport.objects.all()
    serializer_class = CustomerSupportSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        return serializer.save(client=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(client=self.request.user)


class CustomerSupportDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # customer support detail msg for client(owner)
    queryset = CustomerSupport.objects.prefetch_related('support_reply')
    serializer_class = CustomerSupportSerializerDetail
    permission_classes = (permissions.IsAuthenticated,IsOwner,)

    def get_object(self):
        msg_id = self.kwargs.get('msg_id', None)
        return get_object_or_404(self.queryset,client=self.request.user,id=msg_id)


class CustomerSupportListAPIViewAdminUnseen(generics.ListAPIView):
    # Customer support msg list create for admin (unseen msg list)
    queryset = CustomerSupport.objects.all()
    serializer_class = CustomerSupportSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return self.queryset.filter(status='unseen')



class CustomerSupportListAPIViewAdminSeen(generics.ListAPIView):
    # Customer support msg list create for admin (Seen msg list)
    queryset = CustomerSupport.objects.all()
    serializer_class = CustomerSupportSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return self.queryset.filter(status='seen')


class CustomerSupportListAPIViewForAdmin(generics.ListAPIView):
    # Customer support msg list create for admin 
    queryset = CustomerSupport.objects.all()
    serializer_class = CustomerSupportSerializer
    permission_classes = (permissions.IsAdminUser,)


class CustomerSupportDetailAPIViewForAdmin(generics.RetrieveUpdateDestroyAPIView):
    # Customer support msg RetrieveUpdateDestroyAPIView admin (Seen msg )
    queryset = CustomerSupport.objects.prefetch_related('support_reply')
    serializer_class = CustomerSupportSerializerDetail
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self):
        msg_id = self.kwargs.get('msg_id', None)
        msg = CustomerSupport.objects.get(pk=msg_id)
        if msg.status != 'seen':
            msg.status ='seen'
            msg.save()
        return get_object_or_404(self.queryset,id=msg_id)




class CustomerSupportReplyMessageAPIView(APIView):
    
    permission_classes = (permissions.IsAdminUser,)
    
    def post(self, request, *args, **kwargs):
        #  reply customer support msg from admin
        serializer = CustomerSupportReplySerializer(data=request.data)
        if serializer.is_valid():

            msg_id = kwargs.get('msg_id')
            support = CustomerSupport.objects.get(pk=msg_id)

            message = serializer.save(support=support, sender=request.user.username)
            return Response(CustomerSupportReplySerializer(message).data, status=status.HTTP_201_CREATED)
        
        # If the serializer data is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OurTeamListCreateAPIView(generics.ListCreateAPIView):
    # queryset = OurTeam.objects.select_related('employ_profile')
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes = (IsAdminOrReadOnly,)



class CourseTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CourseTypeRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    # provide course Retrieve etc 
    queryset = CourseType.objects.prefetch_related('corse_type')
    serializer_class = CourseTypeRetrieveSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        slug = self.kwargs.get('slug', None)
        return get_object_or_404(self.queryset,slug=slug)


class CourseListCreateAPIView(generics.ListCreateAPIView):
# course list create 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    
class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
# course Retrieve Update Destroy 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self):
        type_slug = self.kwargs.get('type_slug', None)
        course_slug = self.kwargs.get('course_slug', None)
        course_type = get_object_or_404(CourseType.objects.filter(slug=type_slug))
        return get_object_or_404(self.queryset,course_type=course_type,slug=course_slug)



##############
class SubscribeEmailCreateView(generics.CreateAPIView):
# Subscribe anon user for update news 
    queryset = SubscribeEmail.objects.all()
    serializer_class = SubscribeEmailSerializer
    permission_classes = (permissions.AllowAny,)


class SubscribeEmailListView(generics.ListAPIView):
# List of Subscribe anon user for update news 
    queryset = SubscribeEmail.objects.all()
    serializer_class = SubscribeEmailSerializer
    permission_classes = (permissions.IsAdminUser)
    
    
class WhyChoseUsListCreateView(generics.ListCreateAPIView):
# WhyChoseUs model List Create View (List & create)
    queryset = WhyChoseUs.objects.all()
    serializer_class = WhyChoseUsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
class WhyChoseUsListDetailView(generics.RetrieveUpdateDestroyAPIView):
# WhyChoseUs model details View (List & create)
    queryset = WhyChoseUs.objects.all()
    serializer_class = WhyChoseUsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        item_slug = self.kwargs.get('slug', None)
        return get_object_or_404(self.queryset,slug=item_slug)



class AboutUsListCreateView(generics.ListCreateAPIView):
#about us model list create view 
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
class AboutUsDetailsView(generics.RetrieveUpdateDestroyAPIView):
#about us model details view 
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        item_slug = self.kwargs.get('slug', None)
        return get_object_or_404(self.queryset,slug=item_slug)


class ContactAndAddressListCreateView(generics.ListCreateAPIView):
# ContactAndAddress List Create View
    queryset = ContactAndAddress.objects.all()
    serializer_class = ContactAndAddressSerializer
    permission_classes = (IsAdminOrReadOnly,)



class pictureGalleryListCreateView(generics.ListCreateAPIView):
    queryset = pictureGallery.objects.all()
    serializer_class = pictureGallerySerializer
    permission_classes = (IsAdminOrReadOnly,)

class pictureGalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = pictureGallery.objects.all()
    serializer_class = pictureGallerySerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        item_id = self.kwargs.get('id', None)
        return get_object_or_404(self.queryset,id=item_id)

class LiveLinkListCreateView(generics.ListCreateAPIView):
    queryset = LiveLink.objects.all()
    serializer_class = LiveLinkSerializer
    permission_classes = (IsAdminOrReadOnly,)

class LiveLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LiveLink.objects.all()
    serializer_class = LiveLinkSerializer
    permission_classes = (IsAdminOrReadOnly,)
    
    def get_object(self):
        item_id = self.kwargs.get('id', None)
        return get_object_or_404(self.queryset,id=item_id)




class AvailableTimeSlotListCreateAPIView(generics.ListCreateAPIView):
    queryset = AvailableTimeSlot.objects.all()
    serializer_class = AvailableTimeSlotSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BookingTimeSlotListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookingTimeSlot.objects.select_related('user', 'time_slot')
    serializer_class = BookingTimeSlotSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        today_date = datetime.date.today( )
        return self.queryset.filter( time_slot____gte=today_date)





class HomePageContentTypeListCreateAPIView(generics.ListCreateAPIView):
    # home page content section like nave, footer or hero section   
    queryset = HomePageContentType.objects.prefetch_related('home_content_ype')
    serializer_class = HomePageContentTypeSerializer
    permission_classes = (permissions.AllowAny,IsAdminOrReadOnly)
    
    
class HomePageContentTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    # home page content section like nave, footer or hero section 
    queryset = HomePageContentType.objects.prefetch_related('home_content_ype')
    serializer_class = HomePageContentTypeRetrieveSerializer
    permission_classes = (permissions.AllowAny,IsAdminOrReadOnly)
    
    def get_object(self):
        type_id = self.kwargs.get('type_id', None)
        return get_object_or_404(self.queryset,id=type_id)
    
    
class HomePageContentListCreateAPIView(generics.ListCreateAPIView):
    
    # home page content linkable title  like about ous, login , our client,etc 
    queryset = HomePageContent.objects.select_related('category')
    serializer_class = HomePageContentSerializer
    permission_classes = (IsAdminOrReadOnly,)


class HomePageContentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # home page content linkable title&link etc retrieve  like about ous, login , our client,etc 
    queryset = HomePageContent.objects.select_related('category')
    serializer_class = HomePageContentSerializer
    permission_classes = (IsAdminOrReadOnly,) 

    def get_object(self):
        type_id = self.kwargs.get('type_id', None)
        content_id = self.kwargs.get('content_id', None)
        content_type = get_object_or_404(HomePageContentType.objects.filter(id=type_id))
        return get_object_or_404(self.queryset,category=content_type,id=content_id)