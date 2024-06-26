from django.contrib import admin
from word.models import Question
from word.models import Person
from .models import Person, Address

admin.site.register(Question)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'phone',  'city')
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ('person', 'state','street','zip_code') 
   
admin.site.register(Person, PersonAdmin)
admin.site.register(Address)





