from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import resources
from market.models import User, VerificationCode

# Register your models here.


admin.site.site_header = '小码王市场后台管理系统'  # 设置header
admin.site.site_title = '小码王市场后台管理系统'  # 设置title
admin.site.index_title = '小码王市场后台管理系统'


class BookResource(resources.ModelResource):
    id = Field(attribute='id', column_name='编号')
    name = Field(attribute='name', column_name='姓名')
    phoneNumber = Field(attribute='phoneNumber', column_name='手机号码')
    grade = Field(attribute='grade', column_name='所属年级')
    add_date = Field(attribute='add_date', column_name='添加时间')

    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    resource_class = BookResource

    list_display = ['id', 'name', 'phoneNumber', 'grade', 'add_date']
    search_fields = ['id', 'name', 'phoneNumber', 'grade', 'add_date']
    list_filter = ['id', 'name', 'phoneNumber', 'grade', 'add_date']


class VerificationCodeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'code', 'phone_number', 'add_date']
    search_fields = ['id', 'code', 'phone_number', 'add_date']
    list_filter = ['id', 'code', 'phone_number', 'add_date']


admin.site.register(User, UserAdmin)
admin.site.register(VerificationCode, VerificationCodeAdmin)
