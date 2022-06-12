from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import datetime

    
class Closet(models.Model): #옷장모델

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    closet_title = models.CharField(max_length=200) #제목
    closet_url = models.CharField(max_length=300) #s3 url
    closet_create_date = models.DateTimeField(auto_now = True) #날자
    closet_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)#사진추가   

    closet_spring = models.BooleanField(default = True)
    closet_summer = models.BooleanField(default = True)
    closet_fall = models.BooleanField(default = True)
    closet_winter = models.BooleanField(default = True)

    closet_color = models.CharField(max_length=100,default='')
    closet_style = models.CharField(max_length=100, default='')
    closet_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

    closet_section_category = ((1, 'Top'),(2,'Pants'),(3, 'Outer'),(4, 'Onepiece'))
    section =  models.TextField(max_length=20, choices = closet_section_category, default='')
    
    closet_outer_category = ( (1,'Coat'), (2,'Jacket'), (3,'Jumper'), (4,'Padding'), (5,'Best'), (6,'Cardigan '), (7,'Zip-Up'))
    outer =  models.TextField(max_length=20, choices = closet_outer_category, default='')
    
    closet_top_category = ( (1,'Blouse'), (2,'T-shirt'), (3,'Knit'), (4,'Hoodie' ) )
    top =  models.TextField(max_length=20, choices = closet_top_category, default='')
    
    closet_pants_category = ( (1,'Blue jeans'), (2,'Pants'), (3,'Skirt'), (4,'Leggings'), (5,'Jogger pants') )
    pants =  models.TextField(max_length=20, choices = closet_pants_category, default='')
    
    closet_onepiece_category = ((1,'onepiece'),(2,'twopiece'))
    onepiece =  models.TextField(max_length=20, choices = closet_onepiece_category, default='')

    def __str__(self):
        return self.closet_title


class Musinsa_Closet(models.Model):
    clothesId = models.IntegerField( primary_key= True )
    closet_title = models.CharField(max_length=200, default='')
    imgUrl = models.CharField(max_length=50, default='')
    closet_maincategory = ((1, 'Top'),(2,'Pants'),(3, 'Outer'),(4, 'Onepiece'))
    mainCategory =  models.TextField(max_length=20, choices = closet_maincategory, default='')
    closet_outer_category = ( (0,'no'),(1,'Coat'), (2,'Jacket'), (3,'Jumper'), (4,'Padding'), (5,'Best'), (6,'Cardigan '), (7,'Zip-Up'))
    outer =  models.TextField(max_length=20, choices = closet_outer_category, default='0')
    closet_top_category = ( (0,'no'),(1,'Blouse'), (2,'T-shirt'), (3,'Knit'), (4,'Hoodie' ) )
    top =  models.TextField(max_length=20, choices = closet_top_category, default='0')
    closet_pants_category = ( (0,'no'),(1,'Blue jeans'), (2,'Pants'), (3,'Skirt'), (4,'Leggings'), (5,'Jogger pants') )
    pants =  models.TextField(max_length=20, choices = closet_pants_category, default='0')
    closet_onepiece_category = ((0,'no'),(1,'onepiece'),(2,'twopiece'))
    onepiece =  models.TextField(max_length=20, choices = closet_onepiece_category, default='0')
    closet_style = models.CharField(max_length=100, default='')
    closet_color = models.CharField(max_length=100,default='')
    barndName = models.CharField(max_length=50, default ='' )
    ragisterDate = models.DateTimeField(max_length=200, default='')
    spring = models.BooleanField(default = True)
    summer = models.BooleanField(default = True)
    autumn = models.BooleanField(default = True)
    windter = models.BooleanField(default = True)
    elasticity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    transparency = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    thickness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    texture = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    price = models.IntegerField(default=1, null=True)
    regDate = models.DateField(datetime.now)


# 무신사 클로젯
class codi_clothes(models.Model):
    cId = models.IntegerField( primary_key=True)
    codiId = models.IntegerField( default='')
    clothesId = models.ForeignKey(Musinsa_Closet, on_delete=models.CASCADE ,default='')



class codi(models.Model):
    codiId = models.ForeignKey(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    # codiId = models.OneToOneField(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    # codiId = models.ManyToManyField(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    coditype = models.CharField( max_length=10, default='')
    registerDate = models.DateField(datetime.now)
    
class preferences(models.Model):
    preferences_id1= models.IntegerField( primary_key=True )
    preferences_id2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  default= '')
    codiId = models.ForeignKey(codi,on_delete=models.CASCADE, default= '')
    ratingDate = models.DateField(datetime.now)