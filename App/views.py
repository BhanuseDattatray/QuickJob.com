from django.shortcuts import render, redirect
from App.models import JobCkrPrsnl_dtel, Skills_Type, IT_Skills
from App.models import Education_Cat, College, Softwares, Job_Ckr_Education, Course_Dtel,Plans_ForRec,Rec_PlansAssisment_Details
from App.models import Month_Years, City, Joining_Availability, Rec_Profile, Industry_Type, Departments 
from App.models import Candidate_Listing, Designation_Type, ITSkillsBelongToTable,Candidate_Job_Applied_Detail,BankingTransaction
import time
from datetime import date,datetime
import datetime
from django.contrib import messages

# Create your views here.


def Home(request):
    if (request.method == 'GET'):
        CompaniesData = Rec_Profile.objects.all()
        return render(request, 'Home.html', {'Companies':CompaniesData})


def Signin(request):
    U_Email = request.POST['Mail_Id']
    pwd = request.POST['Password']
    try:
        mail_id = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
        User_Password = JobCkrPrsnl_dtel.objects.get(Password=pwd)
    except:
        return redirect(Home)
    else:
        request.session['Mail_Id'] = U_Email
        request.session['Password'] = pwd
        messages.success(request,'Successfull Login')
        return redirect(Resume_Page)


def Signout(request):
    request.session.clear()
    return redirect(Home)


def Jobs(request):
    if ('Rec_Mail_Id' in request.session):
            return redirect(Cand_AppliedForJobs)
    elif('Mail_Id' in request.session):
        return redirect(Resume_Page)
    else:
        return redirect(Home) 


def Resume_Page(request):
    if ('Mail_Id' in request.session):
        U_Email = request.session['Mail_Id']
        User = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
        U_Id = User.id
        Skill = Skills_Type.objects.all()
        Locations = City.objects.all()
        Exp = Month_Years.objects.all()
        Avail = Joining_Availability.objects.all()
        Edu_Cat = Education_Cat.objects.all()
        Edu_collge = College.objects.all()
        Software = Softwares.objects.all()
        Main_Ed = Course_Dtel.objects.all()
        try:
            User_Education = Job_Ckr_Education.objects.filter(
                JobCkrBELONG=U_Id)
        except:
            User_Education = 0

        try:
            All_ITSkill = IT_Skills.objects.filter(JobCkrBELONG=U_Id)
        except:
            User_Education = 0

        return render(request, 'Resume_Page.html', {'ID': User, 'Skillset': Skill, 'Educations': Edu_Cat,
                                                    'Universities': Edu_collge, 'SoftwaresList': Software,
                                                    'Course_Dtel': Main_Ed, 'Experience': Exp,
                                                    'Cities': Locations, 'Availabality': Avail,
                                                    'User_Ed': User_Education, 'ITSkills': All_ITSkill, })
    else:
        return redirect(Home)


def Ed_Check(request):
    U_Email = request.session['Mail_Id']
    User = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
    U_Id = User.id
    try:
        User_Education = Job_Ckr_Education.objects.filter(JobCkrBELONG=U_Id)
    except:
        User_Education = 'Insert Education Details'
        return User_Education
    else:
        return User_Education


def ITSkill_Check(request):
    U_Email = request.session['Mail_Id']
    User = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
    U_Id = User.id
    try:
        All_ITSkill = IT_Skills.objects.filter(JobCkrBELONG=U_Id)
    except:
        All_ITSkill = 'No Software/Skill Added Yet'
        return All_ITSkill
    else:
        return All_ITSkill


def Forms(request):
    if request.method == 'POST':
        U_Email = request.session['Mail_Id']
        User = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
        id = User.id
        if ('Headline_Modal' in request.POST):
            Headline = request.POST['Headline']
            User.Resume_Headline = Headline
            User.save()
            return redirect(Resume_Page)
        elif ('Ed_Modal' in request.POST):
            Edu = request.POST['Selected_Ed']
            Coll = request.POST['Selected_College']
            Cors = request.POST['Selected_Course']
            Ed_f = request.POST['Ed_From']
            Education_Till = request.POST['Ed_Till']
            Ed_Gr = request.POST['Ed_Grade']
            UserEd = Job_Ckr_Education()
            UserEd.JobCkrBELONG = User
            UserEd.Education = Edu
            UserEd.University = Coll
            UserEd.Course = Cors
            UserEd.Course_Duration_From = Ed_f
            UserEd.Course_Duration_Till = Education_Till
            UserEd.Grade = Ed_Gr
            UserEd.save()
            return redirect(Resume_Page)
        elif ('Soft_Modal' in request.POST):
            Exp = request.POST['Selected_Exp']
            Version = request.POST['Version']
            U_Software = request.POST['Selected_Software']
            User_Soft = IT_Skills()
            User_Soft.JobCkrBELONG = User
            User_Soft.Software_Name = U_Software
            User_Soft.Experience = Exp
            User_Soft.Version = Version
            User_Soft.save()
            return redirect(Resume_Page)
        elif ('Personalinfo_Modal' in request.POST):
            U_Name = request.POST['Name']
            Birthday = request.POST['DOB']
            City = request.POST['Selected_City']
            Mobile_no = request.POST['MOB']
            Email = request.POST['Email']
            Experince = request.POST['Selected_Exp']
            Availabletojoin = request.POST['Selected_ATJ']
            try:
                ProfilePic = request.FILES['Photo']
            except:
                U_Gender = request.POST['Gender']
                Address = request.POST['Address']
                User.Name = U_Name
                User.DOB = Birthday
                User.MOB = Mobile_no
                User.Email = Email
                User.Experience = Experince
                User.Available_to_Join = Availabletojoin
                User.Gender = U_Gender
                User.Address = Address
                User.Hometown = City
                User.save()
            else:
                U_Gender = request.POST['Gender']
                Address = request.POST['Address']
                User.Name = U_Name
                User.DOB = Birthday
                User.MOB = Mobile_no
                User.Email = Email
                User.Experience = Experince
                User.Available_to_Join = Availabletojoin
                User.Photo = ProfilePic
                User.Gender = U_Gender
                User.Address = Address
                User.Hometown = City
                User.save()
            
            return redirect(Resume_Page)
    else:
        return redirect(Home)


def Update_Ed_Forms(request, id):
    if (request.method == 'POST'):
        Education_ID = id
        User_Ed = Job_Ckr_Education.objects.get(id=Education_ID)
        U_Email = request.session['Mail_Id']
        User = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
        Edu = request.POST['Selected_Ed']
        Coll = request.POST['Selected_College']
        Cors = request.POST['Selected_Course']
        Ed_f = request.POST['Ed_From']
        Education_Till = request.POST['Ed_Till']
        Ed_Gr = request.POST['Ed_Grade']
        User_Ed.Education = Edu
        User_Ed.University = Coll
        User_Ed.Course = Cors
        User_Ed.Course_Duration_From = Ed_f
        User_Ed.Course_Duration_Till = Education_Till
        User_Ed.Grade = Ed_Gr
        User_Ed.save()
        return redirect(Resume_Page)
    else:
        return redirect(Home)


def Update_Forms_ITSkill(request, id):
    if (request.method == 'POST'):
        Exp = request.POST['Selected_Exp']
        Version = request.POST['Version']
        U_Software = request.POST['Selected_Software']
        User_Soft = IT_Skills.objects.get(id=id)
        User_Soft.Software_Name = U_Software
        User_Soft.Experience = Exp
        User_Soft.Version = Version
        User_Soft.save()
        return redirect(Resume_Page)
    else:
        return redirect(Resume_Page)


def Delete_Forms_ITSkill(request, id):
    if (request.method == 'POST'):
        Skill = IT_Skills.objects.get(id=id)
        Skill.delete()
        return redirect(Resume_Page)
    else:
        return redirect(Resume_Page)


def Delete_Forms_Ed(request, id):
    if (request.method == 'POST'):
        Ed = Job_Ckr_Education.objects.get(id=id)
        Ed.delete()
        return redirect(Resume_Page)
    else:
        return redirect(Resume_Page)


def Signup(request):
    if (request.method == "GET"):
        return render(request, 'JS_Register.html', {})
    else:
        name = request.POST['Name']
        pwd = request.POST['pwd']
        MOB = request.POST['MOB']
        U_Email = request.POST['Email']
        Resume_New = request.FILES['Resume']
        try:
            my = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
        except:
            user = JobCkrPrsnl_dtel()
            user.Name = name
            user.Password = pwd
            user.MOB = MOB
            user.Email = U_Email
            user.Resume = Resume_New
            # Res = JobCkrPrsnl_dtel.objects.create(Resume=Resume_New)
            user.save()
            request.session['Mail_Id'] = U_Email
            request.session['Password'] = pwd
            return redirect(Resume_Page)
        else:
            messages.warning(request,'This Email Id Already Exist')
            return redirect(Signup)

def AddEducationNew(request):
    if request.method == 'POST':
        U_Email = request.session['Mail_Id']
        User = JobCkrPrsnl_dtel.objects.get(Email=U_Email)
        id = User.id
        Edu = request.POST['Selected_Ed']
        Coll = request.POST['Selected_College']
        Cors = request.POST['Selected_Course']
        Ed_f = request.POST['Ed_From']
        Education_Till = request.POST['Ed_Till']
        Ed_Gr = request.POST['Ed_Grade']
        UserEd = Job_Ckr_Education()
        UserEd.JobCkrBELONG = User
        UserEd.Education = Edu
        UserEd.University = Coll
        UserEd.Course = Cors
        UserEd.Course_Duration_From = Ed_f
        UserEd.Course_Duration_Till = Education_Till
        UserEd.Grade = Ed_Gr
        UserEd.save()
        return redirect(Resume_Page)


def EditEd(request, id):
    if (request.method == 'POST'):
        Education_ID = id
        User_Ed = Job_Ckr_Education.objects.get(id=Education_ID)
        Edu = request.POST['Selected_Ed']
        Coll = request.POST['Selected_College']
        Cors = request.POST['Selected_Course']
        Ed_f = request.POST['Ed_From']
        Education_Till = request.POST['Ed_Till']
        Ed_Gr = request.POST['Ed_Grade']
        User_Ed.Education = Edu
        User_Ed.University = Coll
        User_Ed.Course = Cors
        User_Ed.Course_Duration_From = Ed_f
        User_Ed.Course_Duration_Till = Education_Till
        User_Ed.Grade = Ed_Gr
        User_Ed.save()
        return redirect(Resume_Page)


def Recruiter_Profile_Page(request):
    if ('Rec_Mail_Id' in request.session):
        if (request.method == 'GET'):
            U_Mail = request.session['Rec_Mail_Id']
            ID = Rec_Profile.objects.get(Email=U_Mail)
            Locations = City.objects.all()
            messages.success(request,'Successfull Login')
            return render(request, 'Rec_Profile_Page.html', {'User': ID, 'Cities': Locations})
        else:
            if ('id' in request.POST):
                id = request.POST['id']
                User = Rec_Profile.objects.get(id=id)
                User_Name = request.POST['Name']
                User_Company_Name = request.POST['Company_Name']
                User_Email = request.POST['Rec_Mail_Id']
                User_Address = request.POST['Address']
                User_City = request.POST['City']
                User_MOB = request.POST['MOB']
                User_Logo = request.FILES['Logo']
                User_Manpower = request.POST['Manpower']
                User.Name = User_Name
                User.Company_Name = User_Company_Name
                User.Address = User_Address
                User.Email = User_Email
                User.City = User_City
                User.MOB = User_MOB
                User.Manpower = User_Manpower
                User.Logo = User_Logo
                User.save()
                messages.success(request,'Successfully Added')
                return redirect(Recruiter_Profile_Page)
            elif ('CompanyDetails' in request.POST):
                id = request.POST['CompanyDetails']
                User = Rec_Profile.objects.get(id=id)
                Detail = request.POST['Descriptions']
                try:
                    Photos = request.FILES['Carasoule']
                except:
                    User.Com_Description = Detail
                    User.save()
                else:
                    User.Com_Description = Detail
                    User.Photo = Photos
                    User.save()
                messages.success(request,'Successfully Added')
                return redirect(Recruiter_Profile_Page)
    else:
        return redirect(Rec_Register)


def Rec_Register(request):
    if (request.method == "GET"):
        return render(request, 'Rec_Register.html', {})
    else:
        name = request.POST['Name']
        Company = request.POST['Company_Name']
        PWD = request.POST['PWD']
        MOB = request.POST['MOB']
        Email = request.POST['Email']
        Logo_Photo = request.FILES['Logo']
        try:
            Mail_Check = Rec_Profile.objects.get(Email=Email)
            Company_Check = Rec_Profile.objects.get(Company_Name=Company)
        except:
            user = Rec_Profile()
            user.Name = name
            user.Company_Name = Company
            user.Password = PWD
            user.MOB = MOB
            user.Email = Email
            user.Logo = Logo_Photo
            user.save()
            request.session['Rec_Mail_Id'] = Email
            request.session['Rec_Password'] = PWD
            messages.success(request,'Welcome '+name+' to Quick Jobs')
            return redirect(Recruiter_Profile_Page)
        else:
            messages.warning(request,'This Email Id Already Exist')
            return redirect(Rec_Register)


def Rec_signin(request):
    Email = request.POST['Rec_Mail_Id']
    PWD = request.POST['Password']
    try:
        mail_id = Rec_Profile.objects.get(Email=Email)
        User_Password = Rec_Profile.objects.get(Password=PWD)
    except:
        return redirect(Home)
    else:
        request.session['Rec_Mail_Id'] = Email
        request.session['Rec_Password'] = PWD
        return redirect(Recruiter_Profile_Page)


def Rec_Signout(request):
    request.session.clear()
    return redirect(Home)


def Cand_AppliedForJobs(request):
    if ('Rec_Mail_Id' in request.session):
        if (request.method == 'GET'):
            Fetched_User = request.session['Rec_Mail_Id']
            UserCheck = Rec_Profile.objects.get(Email=Fetched_User)
            Userid = UserCheck.id
            ind = Industry_Type.objects.all()
            dept = Departments.objects.all()
            Main_Ed = Course_Dtel.objects.all()
            Software = Softwares.objects.all()
            Exp = Month_Years.objects.all()
            Locations = City.objects.all()
            User_Designations = Designation_Type.objects.all()
            try:
                user = Candidate_Listing.objects.filter(Company=Userid)
            except:
                user = 'No Job Posted Yet'

            #Try block used for Skills fetching with Listing Id

            try:
                AllSkills = ITSkillsBelongToTable.objects.filter(UserId=Userid)
            except:
                AllSkills = 'No Skills'
            
            Rec_PlansAssisment_Details
            U_ID = Rec_Profile.objects.get(Email = request.session['Rec_Mail_Id'])
            try:
                Recruiter = Rec_PlansAssisment_Details.objects.get(Rec = U_ID)
            except:
                Messaage = 'You have not activated any plan yet'
            else:
                if (Recruiter.Post_Counter <= 0):
                    Recruiter.delete()

            return render(request, 'PostJob.html', {'Industries': ind, 'Departments': dept, 'JobListing': user,
                                    'SoftwaresList': Software, 'Course_Dtel': Main_Ed, 'Experience': Exp,
                                    'Cities': Locations, 'Roles': User_Designations,'ITSkills':AllSkills})
        else:
            try:
                Detail = Rec_PlansAssisment_Details.objects.get(Rec = U_ID)
            except:
                Messaage = 'To Access Over a Job Post You need to Activate Paid Services'
                return redirect(Services_Rec)
            else:
                U_mail = request.session['Rec_Mail_Id']
                U_Role = request.POST['Role']
                U_Department = request.POST['Department']
                U_Industry_Type = request.POST['Industry_Type']
                U_Employment_Type = request.POST['Employment_Type']
                U_Education = request.POST['Education']
                U_ITSkill = request.POST.getlist('ITSkill')
                U_Experience = request.POST['Experience']
                U_Salary = request.POST['Salary']
                U_Job_Description = request.POST['Job_Description']
                User = Rec_Profile.objects.get(Email=U_mail)
                Jobslisting = Candidate_Listing()
                Userid = Jobslisting.id
                #Today = date.today()
                Today = datetime.datetime.now()
                curr_time = time.strftime("%H:%M:%S", time.localtime())
                Jobslisting.Date_Of_Post = Today
                Jobslisting.Time_Of_Post = curr_time
                Jobslisting.Experience = U_Experience
                Jobslisting.Salary = U_Salary
                Jobslisting.Location = User.City
                Jobslisting.Role = U_Role
                Jobslisting.Industry_Type = U_Industry_Type
                Jobslisting.Department = U_Department
                Jobslisting.Employment_Type = U_Employment_Type
                Jobslisting.Education = U_Education
                Jobslisting.Description = U_Job_Description
                Jobslisting.Company = User
                Jobslisting.save()
                joblisting_AddSkills = Candidate_Listing.objects.get(
                    Date_Of_Post=Today)
                for Job in U_ITSkill:
                    ITSkillsBelongToTable(
                        ITSkill=Job, SkillBelong_ToJob=joblisting_AddSkills, UserId=joblisting_AddSkills.Company).save()
                Recruiter.Post_Counter -= 1
                Recruiter.save()
                return redirect(Cand_AppliedForJobs)
                    

    else:
        return redirect(Home)


def UpdateJobListing(request,id):
    if (request.method == 'GET'):
        return redirect(Cand_AppliedForJobs)
    else:
        JobListId = id
        U_mail = request.session['Rec_Mail_Id']
        User = Rec_Profile.objects.get(Email=U_mail)
        U_Role = request.POST['Role']
        U_Department = request.POST['Department']
        U_Industry_Type = request.POST['Industry_Type']
        U_Employment_Type = request.POST['Employment_Type']
        U_Education = request.POST['Education']
        U_ITSkill = request.POST.getlist('ITSkill')
        U_Experience = request.POST['Experience']
        U_Salary = request.POST['Salary']
        U_Job_Description = request.POST['Job_Description']
        Jobslisting = Candidate_Listing.objects.get(id=JobListId)
        #Today = date.today()
        Today = datetime.datetime.now()
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        Jobslisting.Date_Of_Post = Today
        Jobslisting.Time_Of_Post = curr_time
        Jobslisting.Experience = U_Experience
        Jobslisting.Salary = U_Salary
        Jobslisting.Location = User.City
        Jobslisting.Role = U_Role
        Jobslisting.Industry_Type = U_Industry_Type
        Jobslisting.Department = U_Department
        Jobslisting.Employment_Type = U_Employment_Type
        Jobslisting.Education = U_Education
        Jobslisting.Description = U_Job_Description
        Jobslisting.Company = User
        Jobslisting.save()
        joblisting_AddSkills = Candidate_Listing.objects.get(
            Date_Of_Post=Today)
        try:
            ItSkillObject = ITSkillsBelongToTable.objects.filter(SkillBelong_ToJob =JobListId)
        except:
            for Job in U_ITSkill:
                ITSkillsBelongToTable(
                    ITSkill =Job, SkillBelong_ToJob=joblisting_AddSkills, UserId=joblisting_AddSkills.User.id).save()
        else:
            ItSkillObject.delete()
            for Job in U_ITSkill:
                    ITSkillsBelongToTable(
                        ITSkill =Job, SkillBelong_ToJob=joblisting_AddSkills, UserId=joblisting_AddSkills.User.id).save()

        return redirect(Cand_AppliedForJobs)

def DeleteJobListing(request,id):
    if (request.method == 'GET'):
        return redirect(Cand_AppliedForJobs)
    else:
        JobListObject = Candidate_Listing.objects.get(id=id)
        JobListObject.delete()
        return redirect(Cand_AppliedForJobs)

     
def Applied_frJobs(request,id):
    if ('Rec_Mail_Id' in request.session):
        if (request.method == 'GET'): 
            U_Mail = request.session['Rec_Mail_Id']
            Candidatelist = Candidate_Job_Applied_Detail.objects.filter(JobId=id)
            User_Education = Job_Ckr_Education.objects.all()
            Job = Candidate_Listing.objects.get(id=id)
            Skillsdata = ITSkillsBelongToTable.objects.filter(SkillBelong_ToJob= id )
            return render(request, 'Candidate_Who_Applied.html',{'Candidates':Candidatelist,'Education':User_Education
                                                                 ,'Jobs':Job,'Skills':Skillsdata})
        else:
            pass
    else:
        return redirect(Home)


def Posted_Jobs(request):
    if ('Mail_Id' in request.session):
        if (request.method == 'GET'):
            Locations = City.objects.all()
            # For Try block used for Job Listing
            try:
                user = Candidate_Listing.objects.all()
            except:
                user = 0

            return render(request, 'Jobs_For_Candidate.html', {'JobListing': user,'Cities': Locations})

        else:
            City_Name = request.POST['Selected_City']
            Locations = City.objects.all()
            # For Try block used for Job Listing
            try:
                user = Candidate_Listing.objects.filter(Location = City_Name)
            except:
                user = 0
            return render(request, 'Jobs_For_Candidate.html', {'JobListing': user,'Cities': Locations})

    else:
        return redirect(Home)
    
def Selected_JobDetails(request,id):
    if ('Mail_Id' in request.session):
        if (request.method == 'GET'):
            Job = Candidate_Listing.objects.get(id=id)
            return render(request,'Selected_JobDetails.html',{'JobListing':Job})
        else:
            pass
    else:
        return redirect(Home)

def SubmitAppliedJob(request,id):
    if ('Mail_Id' in request.session):
         if (request.method == 'GET'):
            U_Mail = request.session['Mail_Id']
            User = JobCkrPrsnl_dtel.objects.get(Email = U_Mail)
            Job = Candidate_Listing.objects.get(id=id)
            CJAD = Candidate_Job_Applied_Detail(JobId = Job, CandidateId = User)
            CJAD.save()
            return redirect(Posted_Jobs)
    else:
        return redirect(Home)
    
def SeeCandidate_Profile(request,id):
    if ('Rec_Mail_Id' in request.session):
        if (request.method == 'GET'):
            User = JobCkrPrsnl_dtel.objects.get(id=id)
            User_Education = Job_Ckr_Education.objects.filter(JobCkrBELONG=id)
            All_ITSkill = IT_Skills.objects.filter(JobCkrBELONG=id)
            return render(request,'CandidateProfileDescription.html',{'ID': User,'User_Ed': User_Education,'ITSkills': All_ITSkill})

def Services_Rec(request):
    if ('Rec_Mail_Id' in request.session):
        U_Mail = request.session['Rec_Mail_Id']
        Rec = Rec_Profile.objects.get(Email=U_Mail)
        Scheme = Plans_ForRec.objects.all()
        return render(request,'Services.html',{'Plans':Scheme})
    else:
        return redirect(Home)
    
def ActivatePlan(request,id):
    if ('Rec_Mail_Id' in request.session):
        if (request.method == 'GET'):
            Scheme = Plans_ForRec.objects.get(id=id)
            return render(request,'PaymentProcess.html',{'Plan':Scheme})
        else:
            U_Mail = request.session['Rec_Mail_Id']
            Rec = Rec_Profile.objects.get(Email=U_Mail)
            Name = request.POST['Name']
            Card = request.POST['CardNo']
            MonthYear  = request.POST['MonthYear']
            CVV = request.POST['CVV']
            # Payment BankingTransaction
            try:
                Banking = BankingTransaction.objects.get(Name=Name,CardNo=Card,ExpiryDate=MonthYear,CVV=CVV)
            except:
                Mesaage = 'Card Holder Doesnot Exist'
                return redirect(ActivatePlan)
            else:
                Banking = BankingTransaction.objects.get(Name=Name,CardNo=Card,ExpiryDate=MonthYear,CVV=CVV)
                Plan = request.POST['Planid']
                Scheme = Plans_ForRec.objects.get(id=Plan)
                Owner = BankingTransaction.objects.get(CardNo = str(999))
                Owner.Balance += float(Scheme.Price)
                Banking.Balance -= float(Scheme.Price)
                Banking.save()
                Owner.save()
                Plans = Rec_PlansAssisment_Details(Plan= Scheme ,Post_Counter= Scheme.MaxPost_Allowed ,Rec= Rec) 
                Plans.save()
                return redirect(Cand_AppliedForJobs)
             
def Companies(request):
    if ('Mail_Id' or 'Rec_Mail_Id' in request.session):
        CompaniesData = Rec_Profile.objects.all()
        return render(request,'Companies.html',{'Companies':CompaniesData})
    else:
        return redirect(Home)
    
def ViewDetails(request,id):
    if ('Mail_Id' or 'Rec_Mail_Id' in request.session):
        CompaniesData = Rec_Profile.objects.get(id=id)
        Locations = City.objects.all()
        U_mail = request.session['Rec_Mail_Id']
        RecId = Rec_Profile.objects.get(Email=U_mail)
        i = str(RecId.id)
        ii = str(id)
        if(i == ii):
            check = 1
            return render(request, 'Rec_Profile_Page.html', {'User': CompaniesData, 'Cities': Locations,'RecCheck':check})
        else:
            check = 0
            return render(request, 'Rec_Profile_Page.html', {'User': CompaniesData})
    else:
        return redirect(Home)