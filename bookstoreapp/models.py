from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.
class Authors(models.Model):

    def validate_phone(phone):
        regexmob = r"^\d{10}$"
        matchvalue = re.match(regexmob, str(phone))
        if phone == "" or matchvalue == None:
            raise ValidationError(f"{phone} is invalid")
    
    def validate_author_name(auther_name):
        if len(auther_name)<2 or len(auther_name)>50 :
            raise ValidationError(f"{auther_name} is invalid")
        
    def validate_user_name(user_name):
        if len(user_name)<2 or len(user_name)>50 :
            raise ValidationError(f"{user_name} is invalid")

    author_name = models.CharField(max_length = 50, null = False, validators=[validate_author_name])
    user_name = models.CharField(max_length = 50, null = False, validators=[validate_user_name])
    email = models.EmailField(null=False) #django it self provide email validation based on the field type
    phone = models.BigIntegerField(null = False, validators=[validate_phone])
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.author_name
    


class Books(models.Model):
    book_name = models.CharField(max_length = 50, null = False)
    author_id = models.ForeignKey(Authors, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default=True)
   

    def __str__(self):
        return self.book_name
    
