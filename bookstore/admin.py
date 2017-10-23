from django.contrib import admin
from bookstore.models import *


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
