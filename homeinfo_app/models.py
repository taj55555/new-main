from django.db import models
from authentiation_app.models import User
from django.utils import timezone
from django.core.validators import EmailValidator
from django.utils.text import slugify


COUNTRY_CODES = (
    ('+1', '+1 (United States)'),
    ('+44', '+44 (United Kingdom)'),
    ('+33', '+33 (France)'),
    ('+49', '+49 (Germany)'),
    ('+81', '+81 (Japan)'),
    ('+86', '+86 (China)'),
    ('+91', '+91 (India)'),
    ('+61', '+61 (Australia)'),
    ('+55', '+55 (Brazil)'),
    ('+7', '+7 (Russia)'),
    ('+20', '+20 (Egypt)'),
    ('+82', '+82 (South Korea)'),
    ('+31', '+31 (Netherlands)'),
    ('+52', '+52 (Mexico)'),
    ('+34', '+34 (Spain)'),
    ('+39', '+39 (Italy)'),
    ('+64', '+64 (New Zealand)'),
    ('+86', '+86 (China)'),
    ('+91', '+91 (India)'),
    ('+92', '+92 (Pakistan)'),
    ('+880', '+880 (Bangladesh)'),
    ('+234', '+234 (Nigeria)'),
    ('+351', '+351 (Portugal)'),
    ('+55', '+55 (Brazil)'),
    ('+81', '+81 (Japan)'),
    ('+86', '+86 (China)'),
    ('+91', '+91 (India)'),
    ('+92', '+92 (Pakistan)'),
    ('+966', '+966 (Saudi Arabia)'),
    ('+61', '+61 (Australia)'),
    ('+64', '+64 (New Zealand)'),
    ('+27', '+27 (South Africa)'),
    ('+41', '+41 (Switzerland)'),
    ('+43', '+43 (Austria)'),
    ('+60', '+60 (Malaysia)'),
    ('+52', '+52 (Mexico)'),
    ('+971', '+971 (United Arab Emirates)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    # Add more country codes as needed
)


status_choices = (
        ('Pending', 'Pending'),
        ('In Review', 'In Review'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        
    )


class ClientProfile(models.Model):
# after user Registration
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    full_name = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=12,null=True, blank=True)  
    country_code = models.CharField(max_length=5, choices=COUNTRY_CODES,default='+880 (Bangladesh)')
    address = models.TextField(null=True,blank=True)
    site_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='client_profile_images/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + "'s Profile"
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Client Profile more info"
    


class Contact(models.Model):
# contact us without registration
    fullname = models.CharField(max_length=30, null=True, blank=True)  
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=12)  
    country_code = models.CharField(max_length=5, choices=COUNTRY_CODES,default='+880 (Bangladesh)')
    subject = models.CharField(max_length=64)
    details = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    image = models.ImageField(upload_to='customer_support_images/', blank=True, null=True, default='')
    site_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + ' '+ self.subject

    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Anonymous User message"




class HomePageContentType(models.Model):
# Home page content category
    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='home_page_images/', blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "HomePage Content Type"


# Home page content Title base on section 
class HomePageContent(models.Model):
    category = models.ForeignKey(HomePageContentType, on_delete=models.CASCADE, related_name='home_content_ype')
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    img = models.ImageField(upload_to='home_content_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering: ['-id']
        verbose_name_plural = "HomePage Contents"


#  provided service category
class ServiceCategory(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    tool_teq = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        # Generate the slug from the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our Services"




# Our working projects
class Project(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='client_project')
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services_project')
    project_title = models.CharField(max_length=64)
    project_url = models.URLField(null=True, blank=True) 
    start_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        # Generate the slug from the title
        self.slug = slugify(self.project_title)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.project_title
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our Projects"


class CustomerSupport(models.Model):
    # for existing customer support msg
    
    status_choices = (
        ('unseen', 'unseen'),
        ('seen', 'seen')
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_client')
    Problem_title = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)
    contact_with = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='customer_support_images/', blank=True, null=True)
    attachment = models.FileField(upload_to='customer_support_attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='unseen')
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Problem_title + ' for  user' + self.client.username
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our Customer message"


class CustomerSupportReply(models.Model):
    # for existing customer support msg admin reply 

    support = models.ForeignKey(CustomerSupport, on_delete=models.CASCADE, related_name='support_reply')
    sender=models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='customer_support_images/', blank=True, null=True)
    attachment = models.FileField(upload_to='customer_support_attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='In Review')
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.support.Problem_title + ' ->reply' 
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our Customer message"


# employ model
class OurTeam(models.Model):
    # employ Profile more info
    
    status_choices = (
        ('active', 'Active'),
        ('On Leave', 'On Leave'),
        ('inactive', 'Inactive'),
        ('Retirement', 'Retirement'),
        ('terminated', 'Terminated'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employ_profile')
    full_name = models.CharField(max_length=64,blank=True, null=True)
    position = models.CharField(max_length=255,blank=True, null=True)
    responsibility =  models.CharField(max_length=255,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(validators=[EmailValidator()],null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)  
    country_code = models.CharField(max_length=5, choices=COUNTRY_CODES,default='+880 (Bangladesh)')
    image = models.ImageField(upload_to='team_pro_pic/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='active')
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our OurTeam member"


# Courses
class CourseType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        # Generate the slug from the name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our Course Type "


class Course(models.Model):
    title = models.CharField(max_length=64)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE, related_name='corse_type')
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    total_class = models.CharField(max_length=12,blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    detail_link = models.URLField()
    video_link = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        # Generate the slug from the name
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f'{self.title} {self.course_type.name}'
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Our Courses"



# Available Time Date (TimeSlot)

class AvailableTimeSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.start_time} to {self.end_time}"
    
    class Meta:
        ordering = ['-date', '-start_time']
        verbose_name_plural = "Add Available TimeSlot"

# clint meeting appointment
class BookingTimeSlot(models.Model):
    user = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='client_appointment')
    time_slot = models.ForeignKey(AvailableTimeSlot, on_delete=models.CASCADE,related_name='available_time' )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} - {self.date} - {self.time_slot}"
    
    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Booked TimeSlot"




class UserIp(models.Model):
    user_ip = models.CharField(max_length = 150)
    country = models.CharField(max_length=1500, blank=True, null=True)
    division = models.CharField(max_length=1500, blank=True, null=True)
    city = models.CharField(max_length=1500, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user_ip
    
class UserIpV(models.Model):
    user_ip = models.CharField(max_length=150)
    country = models.CharField(max_length=1500, blank=True, null=True)
    division = models.CharField(max_length=1500, blank=True, null=True)
    city = models.CharField(max_length=1500, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    isp = models.CharField(max_length=500, blank=True, null=True)
    organization = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now) 
    timezone = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.user_ip
    
    

class SubscribeEmail(models.Model):
    email = models.EmailField(validators=[EmailValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_ip



class WhyChoseUs(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='why_chose_images/', blank=True, null=True)
    video_link = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        # Generate the slug from the name
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "Why Chose Us"


class AboutUs(models.Model):
    story_title = models.CharField(max_length=25,null=True, blank=True)
    mission_title = models.CharField(max_length=25,null=True, blank=True)
    vision_title = models.CharField(max_length=25,null=True, blank=True)
    growth_title = models.CharField(max_length=25,null=True, blank=True)
    story_description = models.TextField(null=True, blank=True)
    growth_description = models.TextField(null=True, blank=True)
    mission_description = models.TextField(null=True, blank=True)
    vision_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    video_link = models.URLField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        # Generate the slug from the name
        self.slug = slugify(self.story_title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.story_title

    class Meta:
        ordering: ['-created_at']
        verbose_name_plural = "About Us"



class ContactAndAddress(models.Model):
    phone_number1 = models.CharField(max_length=12)
    phone_number2 = models.CharField(max_length=12,null=True, blank=True)  
    country_code = models.CharField(max_length=5, choices=COUNTRY_CODES,default='+880 (Bangladesh)')
    address = models.CharField(max_length=255,null=True, blank=True)
    address_url = models.URLField(null=True, blank=True)
    email = models.EmailField(validators=[EmailValidator()],blank=True,null=True)
    email = models.EmailField(validators=[EmailValidator()],blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.country_code} {self.phone_number1}"





class pictureGallery(models.Model): 
    title = models.CharField(max_length=55,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='photo_galary/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LiveLink(models.Model): 
    title = models.CharField(max_length=55,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True,blank=True)
    image = models.ImageField(upload_to='live_link/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
