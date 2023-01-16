from django.contrib import admin
from . models import *
# Register your models here.
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id','b_name','logo','big_logo','banner','ceo_pix','ceo_name','phone_no','phone_no2','favicon','about','copyright']

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id','type','main']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','slug','image','file','content','updated']
    prepopulated_fields = {'slug':('title',)}
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','value']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','commenter','post','body','status']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','message', 'sent']





admin.site.register(CompanyProfile,CompanyProfileAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Content,ContentAdmin)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Contact,ContactAdmin)