from django.db import models

# Create your models here.

class States_Cat(models.Model):
    State_Category = models.CharField(max_length=30)

    def __str__(self):
        return self.State_Category
    
    class Meta:
        db_table = 'States_Cat'    

class City(models.Model):
    City_Name = models.CharField(max_length=30)
    State_Belong = models.ForeignKey(States_Cat,on_delete=models.CASCADE)

    class Meta:
        db_table = 'City'

class Softwares(models.Model):
    Software = models.CharField(max_length=60)

    def __str__(self):
        return self.Software
    
    class Meta:
        db_table = 'Softwares'

class Skills_Type(models.Model):
    Skills = models.CharField(max_length=30)

    class Meta:
        db_table = 'Skills_Type'


class Education_Cat(models.Model):
    Education = models.CharField(max_length=30)

    def __str__(self):
        return self.Education
    
    class Meta:
        db_table = 'Education_Cat'    

class Course_Dtel(models.Model):
    Course = models.CharField(max_length=30)

    class Meta:
        db_table = 'Course_Dtel'

class College(models.Model):
    College_Name = models.CharField(max_length=100)

    class Meta:
        db_table = 'College'

class Joining_Availability(models.Model):
    ATJ = models.CharField(max_length=60)

    class Meta:
        db_table = 'Joining_Availability'

class JobCkrPrsnl_dtel(models.Model):
    Name = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    MOB = models.IntegerField()
    Email = models.CharField(max_length=30)
    Resume = models.FileField(upload_to='Resume/',default=None,null=True)   
    Experience = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    DOB = models.DateField(default=None,null=True)
    Address = models.CharField(max_length=30)
    Hometown = models.CharField(max_length=20)
    Resume_Headline = models.CharField(max_length=200) 
    Photo = models.ImageField(upload_to='ProfilePhotos/',default=None,null=True) 
    Available_to_Join = models.CharField(max_length=60,default=None,null=True) 
    Salary = models.FloatField(default=None,null=True)  
    
    class Meta:
        db_table = 'JobCkrPrsnl_Dtel'

class JobCkrPrfessional_dtel(models.Model):
    Current_Industry = models.CharField(max_length=30)
    Department = models.CharField(max_length=30)
    Role_Category = models.CharField(max_length=30)
    Job_Role = models.CharField(max_length=30)
    Dzird_Job_Typ = models.CharField(max_length=30)
    Dzird_Emp_Typ = models.CharField(max_length=30)
    Prfrd_Shift = models.CharField(max_length=30)
    Expktd_Salary = models.FloatField()
    JobCkrBELONG = models.ForeignKey(JobCkrPrsnl_dtel,on_delete=models.CASCADE)

    class Meta:
        db_table = 'JobCkrPrfessional_dtel'


class Project_Dtel(models.Model):
    Project_Title = models.CharField(max_length=40)
    Client = models.CharField(max_length=30)
    Project_Status = models.CharField(max_length=20)
    Project_Description = models.CharField(max_length=30)
    JobCkrBELONG = models.ForeignKey(JobCkrPrsnl_dtel,on_delete=models.CASCADE)


    class Meta:
        db_table = 'Project_Dtel'

class Designation_Type(models.Model):
    Designation = models.CharField(max_length=30)

    class Meta:
        db_table = 'Designation_Type'


class IT_Skills(models.Model):
    JobCkrBELONG = models.ForeignKey(JobCkrPrsnl_dtel,on_delete=models.CASCADE)
    Software_Name = models.CharField(max_length=30)
    Version = models.CharField(max_length=20)
    Experience = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'IT_Skills'

class Job_Ckr_Education(models.Model):
    JobCkrBELONG = models.ForeignKey(JobCkrPrsnl_dtel,on_delete=models.CASCADE)
    Education = models.CharField(max_length=20)
    University = models.CharField(max_length=100)
    Course = models.CharField(max_length=20)
    Course_Duration_From = models.DateField(default=None,null=True)
    Course_Duration_Till = models.DateField(default=None,null=True)
    Grade = models.CharField(max_length=10)

    class Meta:
        db_table = 'Job_Ckr_Education'    



class Month_Years(models.Model):
    Duration = models.CharField(max_length=80)

    class Meta:
        db_table = 'Month_Years'

class Rec_Profile(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=40)
    Password = models.CharField(max_length=20)
    Address = models.CharField(max_length=30)
    City = models.CharField(max_length=50)
    MOB = models.IntegerField()
    Company_Name = models.CharField(max_length=60)
    Designation = models.CharField(max_length=30)
    Manpower = models.IntegerField(null=True,default=None)
    Com_Description = models.CharField(max_length=200)
    Logo = models.ImageField(upload_to='CompanyLogos/',null=True,default=None)
    Photo = models.ImageField(upload_to='Companies_Photos/',default=None,null=True)

    class Meta:
        db_table = 'Rec_Profile'

class Images(models.Model):
    Img = models.ImageField(upload_to='static/images/', default=None,null=True)

    class Meta:
        db_table = 'Images'

class Candidate_Listing(models.Model):
    Experience = models.CharField(max_length=60)
    Salary = models.FloatField()
    Location = models.CharField(max_length=30)
    Role = models.CharField(max_length=30)
    Industry_Type = models.CharField(max_length=30)
    Department = models.CharField(max_length=30)
    Employment_Type = models.CharField(max_length=30)
    Education = models.CharField(max_length=30)
    Description = models.CharField(max_length=300)
    Date_Of_Post = models.DateTimeField(null=True,default=None)
    Time_Of_Post = models.TimeField(null=True,default=None)
    Company = models.ForeignKey(Rec_Profile,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Candidate_Listing'

class Departments(models.Model):
    Department = models.CharField(max_length=30)

    class Meta:
        db_table = 'Departments'

class Industry_Type(models.Model):
    Industry = models.CharField(max_length=30)

    class Meta:
        db_table = 'Industry_Type'


class ITSkillsBelongToTable(models.Model):
    ITSkill = models.CharField(max_length=60)
    SkillBelong_ToJob = models.ForeignKey(Candidate_Listing,on_delete=models.CASCADE)
    UserId = models.ForeignKey(Rec_Profile,on_delete=models.CASCADE)

    class Meta:
        db_table = 'ITSkillsBelongToTable'

class Candidate_Job_Applied_Detail(models.Model):
    JobId = models.ForeignKey(Candidate_Listing,on_delete=models.CASCADE)
    CandidateId = models.ForeignKey(JobCkrPrsnl_dtel,on_delete=models.CASCADE)
    DateandTime = models.DateTimeField(default=None,null=True)

    class Meta:
        db_table = 'Candidate_Job_Applied_Detail'



class Plans_ForRec(models.Model):
    PlanName = models.CharField(max_length=60)
    MaxPost_Allowed = models.IntegerField()
    Price = models.FloatField()

    class Meta:
        db_table = 'Plans_ForRec'

class Rec_PlansAssisment_Details(models.Model):
    Plan = models.ForeignKey(Plans_ForRec,on_delete=models.CASCADE)
    Post_Counter = models.IntegerField()
    Rec = models.ForeignKey(Rec_Profile,on_delete=models.CASCADE)
    #Plan Post_Counter Rec
    class Meta:
        db_table = 'Rec_PlansAssisment_Details'

class BankingTransaction(models.Model):
    Name = models.CharField(max_length=60)
    CardNo = models.CharField(max_length=16)
    CVV = models.CharField(max_length=6)
    ExpiryDate = models.CharField(max_length=15)
    Balance = models.FloatField()
    Mail = models.EmailField(max_length=60)

    class Meta:
        db_table = 'BankingTransaction'