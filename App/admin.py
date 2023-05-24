from django.contrib import admin
from .models import States_Cat, City, Skills_Type, Designation_Type, Education_Cat, Course_Dtel, College, JobCkrPrsnl_dtel,Softwares, Month_Years,Joining_Availability,Images,Industry_Type,Departments,Rec_PlansAssisment_Details,Plans_ForRec,BankingTransaction
# Register your models here.


class States(admin.ModelAdmin):
    list_display = ('id', 'State_Category')


class Cities(admin.ModelAdmin):
    list_display = ('id', 'City_Name', 'State_Belong')


class Skills_Cat_Admin(admin.ModelAdmin):
    list_display = ('id', 'Category')


class Skills(admin.ModelAdmin):
    list_display = ('id', 'Skills')


class Designations_Cat(admin.ModelAdmin):
    list_display = ('id', 'Designation')


class All_Education(admin.ModelAdmin):
    list_display = ('id', 'Education')


class Course(admin.ModelAdmin):
    list_display = ('id', 'Course')


class All_College(admin.ModelAdmin):
    list_display = ('id', 'College_Name')


class Experince_Duration(admin.ModelAdmin):
    list_display = ('id','Duration')

class ATJ(admin.ModelAdmin):
    list_display = ('id','ATJ')

class All_Static_Images(admin.ModelAdmin):
    list_display = ('id','Img')

class AllDepartment(admin.ModelAdmin):
    list_display = ('id','Department')

class All_Industry(admin.ModelAdmin):
    list_display = ('id','Industry')


class All_Plans_ForRec(admin.ModelAdmin):
    list_display = ('id','PlanName','MaxPost_Allowed')

class All_Rec_PlansAssisment_Details(admin.ModelAdmin):
    list_display =  ('id','Plan','Post_Counter','Rec')

class All_BankingTransaction(admin.ModelAdmin):
    list_display = ('id','Name','CardNo','CVV','Mail')

admin.site.register(Images,All_Static_Images)
admin.site.register(States_Cat, States)
admin.site.register(City, Cities)
admin.site.register(Designation_Type, Designations_Cat)
admin.site.register(Education_Cat, All_Education)
admin.site.register(Course_Dtel, Course)
admin.site.register(College, All_College)
admin.site.register(Skills_Type, Skills)
admin.site.register(JobCkrPrsnl_dtel)
admin.site.register(Softwares)
admin.site.register(Month_Years,Experince_Duration)
admin.site.register(Joining_Availability,ATJ)
admin.site.register(Departments,AllDepartment)
admin.site.register(Industry_Type,All_Industry)
admin.site.register(Plans_ForRec,All_Plans_ForRec)
admin.site.register(Rec_PlansAssisment_Details,All_Rec_PlansAssisment_Details)
admin.site.register(BankingTransaction,All_BankingTransaction)