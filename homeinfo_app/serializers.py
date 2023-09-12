from rest_framework import serializers
from .models import ClientProfile, Contact, HomePageContentType, HomePageContent, ServiceCategory, Project, CustomerSupport, OurTeam, CourseType, Course, AvailableTimeSlot, BookingTimeSlot,SubscribeEmail,CustomerSupportReply,WhyChoseUs, AboutUs, ContactAndAddress,pictureGallery, LiveLink
from django.core.validators import EmailValidator


class ClientProfileSerializer(serializers.ModelSerializer):
# client user profile edit update , get etc  
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = ClientProfile
        exclude = ('id',)
        read_only_fields = ('user','date_joined','update_at')


class ContactSerializer(serializers.ModelSerializer):
# contact us without registration
    class Meta:
        model = Contact
        fields = ('id','fullname','email','phone','country_code','subject','details','attachment','image','site_url','created_at')
        read_only_fields = ('id','created_at')

class HomePageContentSerializerList(serializers.ModelSerializer):
# home page content type list for HomePageContentTypeRetrieveSerializer
    class Meta:
        model = HomePageContent
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')

class HomePageContentTypeRetrieveSerializer(serializers.ModelSerializer):
    home_content_ype=HomePageContentSerializerList(many=True, read_only=True)
    # home page content type Retrieve update......
    class Meta:
        model = HomePageContentType
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')
        
        
        
class HomePageContentTypeSerializer(serializers.ModelSerializer):
    
    # home page content type list......
    class Meta:
        model = HomePageContentType
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')

class HomePageContentSerializer(serializers.ModelSerializer):
    # home page content list create 
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = HomePageContent
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')
        
    def create(self, validated_data):
        category_name = validated_data.pop('category', '')
        category, _ = HomePageContentType.objects.get_or_create(category_name=category_name)
        content = HomePageContent.objects.create(**validated_data, category=category)
        return content






class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')



class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.user.username', read_only=True)
    service = serializers.CharField(source='service.title', read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id','client','service','created_at','update_at')


class CustomerSupportSerializer(serializers.ModelSerializer):
# for existing customer support msg list create 
    client = serializers.CharField(source='client.username', read_only=True)
    class Meta:
        model = CustomerSupport
        fields = '__all__'
        read_only_fields = ('id','client','status','created_at','update_at')



class CustomerSupportReplySerializer(serializers.ModelSerializer):
# for existing customer support msg reply
    support = serializers.CharField(source='support.Problem_title', read_only=True)
    class Meta:
        model = CustomerSupportReply
        fields = '__all__'
        read_only_fields = ('id','support','status','sender','created_at','update_at')


class CustomerSupportSerializerDetail(serializers.ModelSerializer):
# for existing customer support msg detail 
    support_reply = CustomerSupportReplySerializer(many=True, read_only=True)
    class Meta:
        model = CustomerSupport
        fields = '__all__'
        read_only_fields = ('id','client','support_reply','created_at','update_at')



class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'
        read_only_fields = ('id','user','created_at','update_at')



class CourseTypeSerializer(serializers.ModelSerializer):
    # for course type list,create view
    class Meta:
        model = CourseType
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')


class CourseForCategorySerializer(serializers.ModelSerializer):
    # Use with CourseTypeRetrieveSerializer
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')



class CourseTypeRetrieveSerializer(serializers.ModelSerializer):
    # for Course Type Retrieve view
    corse_type = CourseForCategorySerializer(many=True,read_only=True)

    class Meta:
        model = CourseType
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at','corse_type')

class CourseSerializer(serializers.ModelSerializer):
    course_type = CourseTypeSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id','created_at','update_at')
        
    def create(self, validated_data):
        type_name = validated_data.pop('course_type', '')
        course_type, _ = CourseType.objects.get_or_create(name=type_name)
        course = Course.objects.create(**validated_data, course_type=course_type)
        return course 




class AvailableTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTimeSlot
        fields = '__all__'
        read_only_fields = ('id','created_at')


class BookingTimeSlotSerializer(serializers.ModelSerializer):
    available_time=AvailableTimeSlotSerializer(many=True, read_only=True)
    class Meta:
        model = BookingTimeSlot
        fields = ('id','time_slot','created_at','update_at','available_time')
        read_only_fields = ('id','user','created_at','update_at')



class SubscribeEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = SubscribeEmail
        fields = ('email', 'created_at', 'update_at')
        read_only_fields = ('id','created_at', 'update_at')
        




class WhyChoseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoseUs
        fields = '__all__'
        read_only_fields = ('id','created_at', 'update_at')

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        read_only_fields = ('id','created_at', 'update_at')

class ContactAndAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAndAddress
        fields = '__all__'
        # read_only_fields = ('id',)
        read_only_fields = ('id','created_at', 'update_at')


class pictureGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = pictureGallery
        fields = '__all__'
        read_only_fields = ('id','created_at', 'update_at')



class LiveLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveLink
        fields = '__all__'
        read_only_fields = ('id','created_at', 'update_at')