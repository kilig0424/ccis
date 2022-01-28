from django.contrib import admin

# Register your models here.

from .models import UserInfo, GroupInfo, SkillTable, ClassInfo, UserSkill

admin.site.register(GroupInfo)
admin.site.register(UserInfo)
admin.site.register(SkillTable)
admin.site.register(ClassInfo)
admin.site.register(UserSkill)


