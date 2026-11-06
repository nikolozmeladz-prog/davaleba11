from django.contrib import admin
from .models import Profile, Author, Book, Student, Course

admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)