from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group,User
from django.conf import settings as conf_set
from django.contrib import messages
from django.contrib.auth.models import User,auth
from schAdmission.admForms.admissionForms import PriAdmForm,SecondAdmForm,CollegeAdmForm,RejoinForm,Form1710AdmForm,Form1712AdmForm,ATKT11AdmForm
from schAdmission.admModels.admissionModels import PrimAdm,SecondAdm,CollegeAdm,Form1710Adm,Form1712Adm,ATKT11Adm
from schSetup.setupModels.setup_cast_models import CastCategory,Cast,Religion,SubCast
from schSetup.setupModels.setup_models import Division
from seedData.models import Year
from schAdmission.admForms.admissionForms import GetAdmYearForm
import datetime

  

#Repeater Views
# Academic All add Views ::


sname=conf_set.SCHOOL_NAME


# Primary admission Add View
def admission_addPrim(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        if request.method == 'POST':
            priAdmForm= PriAdmForm(request.POST,request.FILES)
            if priAdmForm.is_valid():
                try:
                    if PrimAdm.objects.filter(prn__iexact=priAdmForm.cleaned_data['prn']).exists():
                        messages.error(request,"Register Number Already Exists")
                        return redirect('admission_primadd')
                    elif PrimAdm.objects.filter(aadhar__iexact=priAdmForm.cleaned_data['aadhar']).exists():
                        messages.error(request,"Aadhar Number Already Exists")
                        return redirect('admission_primadd')
                    elif PrimAdm.objects.filter(email__iexact=priAdmForm.cleaned_data['email']).exists():
                        messages.error(request,"Email Id Already Exists")
                        return redirect('admission_primadd')                        
                    else:
                        priAdmModule=PrimAdm()
                        priAdmModule.prn=priAdmForm.cleaned_data['prn']
                        priAdmModule.lname=priAdmForm.cleaned_data['lname']
                        priAdmModule.fname=priAdmForm.cleaned_data['fname']
                        priAdmModule.faname=priAdmForm.cleaned_data['faname']
                        priAdmModule.moname=priAdmForm.cleaned_data['moname']
                        priAdmModule.mrname=priAdmForm.cleaned_data['mrname']
                        priAdmModule.aadhar=priAdmForm.cleaned_data['aadhar']
                        priAdmModule.saral_id=priAdmForm.cleaned_data['saral_id']
                        priAdmModule.nationality=priAdmForm.cleaned_data['nationality']
                        priAdmModule.tongue=priAdmForm.cleaned_data['tongue']
                        priAdmModule.religion=priAdmForm.cleaned_data['religion']
                        priAdmModule.cast=priAdmForm.cleaned_data['cast']
                        priAdmModule.subcast=priAdmForm.cleaned_data['subcast']
                        priAdmModule.minority=priAdmForm.cleaned_data['minority']
                        priAdmModule.pob=priAdmForm.cleaned_data['pob']
                        priAdmModule.dob=priAdmForm.cleaned_data['dob']
                        priAdmModule.last_school=priAdmForm.cleaned_data['last_school']
                        priAdmModule.last_class=priAdmForm.cleaned_data['last_class']
                        priAdmModule.prevprn=priAdmForm.cleaned_data['prevprn']
                        priAdmModule.prevlcsrno=priAdmForm.cleaned_data['prevlcsrno']
                        priAdmModule.admdate=priAdmForm.cleaned_data['admdate']
                        y=priAdmForm.cleaned_data['admdate']
                        mon_list=['01','02','03','04','05']
                        if y[5:7] in mon_list:
                            y=str(int(y[0:4])-1)
                            priAdmModule.admyear=y[0:4]
                        else:
                            priAdmModule.admyear=y[0:4]
                        priAdmModule.adm_class=priAdmForm.cleaned_data['adm_class']
                        priAdmModule.division=priAdmForm.cleaned_data['division']
                        priAdmModule.rollno=priAdmForm.cleaned_data['rollno']
                        priAdmModule.lateadm=priAdmForm.cleaned_data['lateadm']
                        priAdmModule.admtype=priAdmForm.cleaned_data['admtype']
                        priAdmModule.hostel=priAdmForm.cleaned_data['hostel']
                        priAdmModule.sex=priAdmForm.cleaned_data['sex']
                        priAdmModule.pwd=priAdmForm.cleaned_data['pwd']
                        priAdmModule.bgroup=priAdmForm.cleaned_data['bgroup']
                        priAdmModule.fa_mob=priAdmForm.cleaned_data['fa_mob']
                        priAdmModule.mo_mob=priAdmForm.cleaned_data['mo_mob']
                        priAdmModule.fa_occu=priAdmForm.cleaned_data['fa_occu']
                        priAdmModule.mo_occu=priAdmForm.cleaned_data['mo_occu']
                        priAdmModule.fam_income=priAdmForm.cleaned_data['fam_income']
                        priAdmModule.bpl=priAdmForm.cleaned_data['bpl']
                        priAdmModule.gis=priAdmForm.cleaned_data['gis']
                        priAdmModule.ganame=priAdmForm.cleaned_data['ganame']
                        priAdmModule.ga_mob=priAdmForm.cleaned_data['ga_mob']
                        priAdmModule.ga_occu=priAdmForm.cleaned_data['ga_occu']
                        priAdmModule.gaddress=priAdmForm.cleaned_data['gaddress']
                        priAdmModule.ga_relation=priAdmForm.cleaned_data['ga_relation']
                        priAdmModule.email=priAdmForm.cleaned_data['email']
                        priAdmModule.areaType=priAdmForm.cleaned_data['areaType']
                        priAdmModule.caddress=priAdmForm.cleaned_data['caddress']
                        priAdmModule.ca_is_pa_addr=priAdmForm.cleaned_data['ca_is_pa_addr']
                        priAdmModule.paddress=priAdmForm.cleaned_data['paddress']
                        priAdmModule.baccount=priAdmForm.cleaned_data['baccount']
                        priAdmModule.bankname=priAdmForm.cleaned_data['bankname']
                        priAdmModule.ifsc=priAdmForm.cleaned_data['ifsc']
                        priAdmModule.branch=priAdmForm.cleaned_data['branch']
                        priAdmModule.micr=priAdmForm.cleaned_data['micr']
                        priAdmModule.marks_img=priAdmForm.cleaned_data['marks_img']
                        priAdmModule.prv_lc_img=priAdmForm.cleaned_data['prv_lc_img']
                        priAdmModule.addhar_img=priAdmForm.cleaned_data['addhar_img']
                        priAdmModule.cast_img=priAdmForm.cleaned_data['cast_img']
                        priAdmModule.castvald_img=priAdmForm.cleaned_data['castvald_img']
                        priAdmModule.nationality_img=priAdmForm.cleaned_data['nationality_img']
                        priAdmModule.noncrimy_img=priAdmForm.cleaned_data['noncrimy_img']
                        priAdmModule.std_img=priAdmForm.cleaned_data['std_img']
                        priAdmModule.birth_img=priAdmForm.cleaned_data['birth_img']
                        priAdmModule.note=priAdmForm.cleaned_data['note']
                        #for Academics  
                        no=int(priAdmForm.cleaned_data['adm_class'])
                        print(no)
                        if no==1:
                            priAdmModule.updateclass1 = priAdmForm.cleaned_data['adm_class']
                            priAdmModule.updateyear1 = y[0:4]
                            priAdmModule.updatedivision1 = str(priAdmForm.cleaned_data['division'])
                            priAdmModule.updaterollno1 = priAdmForm.cleaned_data['rollno']
                        elif no==2:
                            priAdmModule.updateclass2 = priAdmForm.cleaned_data['adm_class']
                            priAdmModule.updateyear2 = y[0:4]
                            priAdmModule.updatedivision2 = str(priAdmForm.cleaned_data['division'])
                            priAdmModule.updaterollno2 = priAdmForm.cleaned_data['rollno']
                        elif no==3:
                            priAdmModule.updateclass3 = priAdmForm.cleaned_data['adm_class']
                            priAdmModule.updateyear3 = y[0:4]
                            priAdmModule.updatedivision3 = str(priAdmForm.cleaned_data['division'])
                            priAdmModule.updaterollno3 = priAdmForm.cleaned_data['rollno']
                        elif no==4:
                            priAdmModule.updateclass4 = priAdmForm.cleaned_data['adm_class']
                            priAdmModule.updateyear4 = y[0:4]
                            priAdmModule.updatedivision4 = str(priAdmForm.cleaned_data['division'])
                            priAdmModule.updaterollno4 = priAdmForm.cleaned_data['rollno']
                        # Create User for Student
                        user=User.objects.create_user(username=priAdmForm.cleaned_data['aadhar'],email=priAdmForm.cleaned_data['email'],password="Admin@123",first_name=priAdmForm.cleaned_data['fname'],last_name=priAdmForm.cleaned_data['lname'])
                        user.save()
                        # create student id for rejoin
                        #studid=StudID()
                        #studid.stud_id=user
                        #studid.save()
                        priAdmModule.stud_id="p"+str(user.id)+""+priAdmForm.cleaned_data['prn']
                        my_group=Group.objects.get(name='student')
                        #my_group.user_set.add(user)
                        user.groups.add(my_group)
                        #priAdmModule.u_ref_student=User.objects.get(username=priAdmForm.cleaned_data['aadhar'])
                        priAdmModule.user=user
                        # priAdmModule.lcgenerated=False
                        print("fsdaf")
                        priAdmModule.save()
                        print("fsdaf")
                        # for academic
                        #priacd=PrimAcademic()
                        #priacd.prim_admission=priAdmModule
                        #priacd.save()
                        #print("fsdaf")
                        messages.success(request, priAdmForm.cleaned_data['fname']+" "+priAdmForm.cleaned_data['faname']+" "+priAdmForm.cleaned_data['lname']+' Student Admitted Sucessfully!')
                        return redirect('admission_primadd')
                except:
                    messages.error(request,"Invalid header found in Primary Admission form... Try again")
                    return redirect('admission_primadd')    
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            priAdmForm= PriAdmForm()
        priData = PrimAdm.objects.all()
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Student Admission /",
            'fname':fname,
            "page_path":" Primary Admission / Admission",
            "menu_icon":"nav-icon fas fa-address-card",
            "priAdmForm":priAdmForm,
            "priData":priData,
            }    
        return render(request, 'schoolviews/admission/prim_adm.html',context) 
    else:
        return redirect('login') 




# Secondary admission Add View
def admission_addSec(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        if request.method == 'POST':
            secAdmForm= SecondAdmForm(request.POST,request.FILES)
            if secAdmForm.is_valid():
                try:
                    print("ggfdsfd")
                    if SecondAdm.objects.filter(prn__iexact=secAdmForm.cleaned_data['prn']).exists():
                        messages.error(request,"Register Number Already Exists")
                        return redirect('admission_secadd')
                    elif SecondAdm.objects.filter(aadhar__iexact=secAdmForm.cleaned_data['aadhar']).exists():
                        messages.error(request,"Aadhar Number Already Exists")
                        return redirect('admission_secadd')
                    elif SecondAdm.objects.filter(email__iexact=secAdmForm.cleaned_data['email']).exists():
                        messages.error(request,"Email Id Already Exists")
                        return redirect('admission_secadd')                        
                    else:
                        print("ggfdsfd")
                        secAdmModule=SecondAdm()
                        secAdmModule.prn=secAdmForm.cleaned_data['prn']
                        secAdmModule.lname=secAdmForm.cleaned_data['lname']
                        secAdmModule.fname=secAdmForm.cleaned_data['fname']
                        secAdmModule.faname=secAdmForm.cleaned_data['faname']
                        secAdmModule.moname=secAdmForm.cleaned_data['moname']
                        secAdmModule.mrname=secAdmForm.cleaned_data['mrname']
                        secAdmModule.aadhar=secAdmForm.cleaned_data['aadhar']
                        secAdmModule.saral_id=secAdmForm.cleaned_data['saral_id']
                        secAdmModule.nationality=secAdmForm.cleaned_data['nationality']
                        secAdmModule.tongue=secAdmForm.cleaned_data['tongue']
                        secAdmModule.religion=secAdmForm.cleaned_data['religion']
                        secAdmModule.cast=secAdmForm.cleaned_data['cast']
                        secAdmModule.subcast=secAdmForm.cleaned_data['subcast']
                        secAdmModule.minority=secAdmForm.cleaned_data['minority']
                        secAdmModule.pob=secAdmForm.cleaned_data['pob']
                        secAdmModule.dob=secAdmForm.cleaned_data['dob']
                        secAdmModule.last_school=secAdmForm.cleaned_data['last_school']
                        secAdmModule.last_class=secAdmForm.cleaned_data['last_class']
                        secAdmModule.prevprn=secAdmForm.cleaned_data['prevprn']
                        secAdmModule.prevlcsrno=secAdmForm.cleaned_data['prevlcsrno']
                        secAdmModule.admdate=secAdmForm.cleaned_data['admdate']
                        y=secAdmForm.cleaned_data['admdate']                   
                        mon_list=['01','02','03','04','05']
                        if y[5:7] in mon_list:
                            y=str(int(y[0:4])-1)
                            secAdmModule.admyear=y[0:4]
                        else:
                            secAdmModule.admyear=y[0:4]
                        secAdmModule.adm_class=secAdmForm.cleaned_data['adm_class']
                        secAdmModule.division=secAdmForm.cleaned_data['division']
                        secAdmModule.rollno=secAdmForm.cleaned_data['rollno']
                        secAdmModule.lateadm=secAdmForm.cleaned_data['lateadm']
                        secAdmModule.admtype=secAdmForm.cleaned_data['admtype']
                        secAdmModule.hostel=secAdmForm.cleaned_data['hostel']
                        secAdmModule.sex=secAdmForm.cleaned_data['sex']
                        secAdmModule.pwd=secAdmForm.cleaned_data['pwd']
                        secAdmModule.bgroup=secAdmForm.cleaned_data['bgroup']
                        secAdmModule.fa_mob=secAdmForm.cleaned_data['fa_mob']
                        secAdmModule.mo_mob=secAdmForm.cleaned_data['mo_mob']
                        secAdmModule.fa_occu=secAdmForm.cleaned_data['fa_occu']
                        secAdmModule.mo_occu=secAdmForm.cleaned_data['mo_occu']
                        secAdmModule.fam_income=secAdmForm.cleaned_data['fam_income']
                        secAdmModule.bpl=secAdmForm.cleaned_data['bpl']
                        secAdmModule.gis=secAdmForm.cleaned_data['gis']
                        secAdmModule.ganame=secAdmForm.cleaned_data['ganame']
                        secAdmModule.ga_mob=secAdmForm.cleaned_data['ga_mob']
                        secAdmModule.ga_occu=secAdmForm.cleaned_data['ga_occu']
                        secAdmModule.gaddress=secAdmForm.cleaned_data['gaddress']
                        secAdmModule.ga_relation=secAdmForm.cleaned_data['ga_relation']
                        secAdmModule.email=secAdmForm.cleaned_data['email']
                        secAdmModule.areaType=secAdmForm.cleaned_data['areaType']
                        secAdmModule.caddress=secAdmForm.cleaned_data['caddress']
                        secAdmModule.ca_is_pa_addr=secAdmForm.cleaned_data['ca_is_pa_addr']
                        secAdmModule.paddress=secAdmForm.cleaned_data['paddress']
                        secAdmModule.baccount=secAdmForm.cleaned_data['baccount']
                        secAdmModule.bankname=secAdmForm.cleaned_data['bankname']
                        secAdmModule.ifsc=secAdmForm.cleaned_data['ifsc']
                        secAdmModule.branch=secAdmForm.cleaned_data['branch']
                        secAdmModule.micr=secAdmForm.cleaned_data['micr']
                        secAdmModule.marks_img=secAdmForm.cleaned_data['marks_img']
                        secAdmModule.prv_lc_img=secAdmForm.cleaned_data['prv_lc_img']
                        secAdmModule.addhar_img=secAdmForm.cleaned_data['addhar_img']
                        secAdmModule.cast_img=secAdmForm.cleaned_data['cast_img']
                        secAdmModule.castvald_img=secAdmForm.cleaned_data['castvald_img']
                        secAdmModule.nationality_img=secAdmForm.cleaned_data['nationality_img']
                        secAdmModule.noncrimy_img=secAdmForm.cleaned_data['noncrimy_img']
                        secAdmModule.std_img=secAdmForm.cleaned_data['std_img']
                        secAdmModule.birth_img=secAdmForm.cleaned_data['birth_img']
                        secAdmModule.note=secAdmForm.cleaned_data['note']
                        #for Academics
                        no=int(secAdmForm.cleaned_data['adm_class'])
                        print(no)
                        if no==5:
                            secAdmModule.updateclass5 = secAdmForm.cleaned_data['adm_class']
                            secAdmModule.updateyear5 = y[0:4]
                            secAdmModule.updatedivision5 = str(secAdmForm.cleaned_data['division'])
                            secAdmModule.updaterollno5 = secAdmForm.cleaned_data['rollno']
                        elif no==6:
                            secAdmModule.updateclass6 = secAdmForm.cleaned_data['adm_class']
                            secAdmModule.updateyear6 = y[0:4]
                            secAdmModule.updatedivision6 = str(secAdmForm.cleaned_data['division'])
                            secAdmModule.updaterollno6 = secAdmForm.cleaned_data['rollno']
                        elif no==7:
                            secAdmModule.updateclass7 = secAdmForm.cleaned_data['adm_class']
                            secAdmModule.updateyear7 = y[0:4]
                            secAdmModule.updatedivision7 = str(secAdmForm.cleaned_data['division'])
                            secAdmModule.updaterollno7 = secAdmForm.cleaned_data['rollno']
                        elif no==8:
                            secAdmModule.updateclass8 = secAdmForm.cleaned_data['adm_class']
                            secAdmModule.updateyear8 = y[0:4]
                            secAdmModule.updatedivision8 = str(secAdmForm.cleaned_data['division'])
                            secAdmModule.updaterollno8 = secAdmForm.cleaned_data['rollno']
                        elif no==9:
                            secAdmModule.updateclass9 = secAdmForm.cleaned_data['adm_class']
                            secAdmModule.updateyear9 = y[0:4]
                            secAdmModule.updatedivision9 = str(secAdmForm.cleaned_data['division'])
                            secAdmModule.updaterollno9 = secAdmForm.cleaned_data['rollno']
                        elif no==10:
                            secAdmModule.updateclass10 = secAdmForm.cleaned_data['adm_class']
                            secAdmModule.updateyear10 = y[0:4]
                            secAdmModule.updatedivision10 = str(secAdmForm.cleaned_data['division'])
                            secAdmModule.updaterollno10 = secAdmForm.cleaned_data['rollno']
                        # Create User for Student
                        print("sgds")
                        user=User.objects.create_user(username=secAdmForm.cleaned_data['aadhar'],email=secAdmForm.cleaned_data['email'],password="Admin@123",first_name=secAdmForm.cleaned_data['fname'],last_name=secAdmForm.cleaned_data['lname'])
                        user.save()
                        # create student id for rejoin
                        # studid=StudID()
                        # studid.stud_id=user
                        # studid.save()
                        secAdmModule.stud_id="s"+str(user.id)+""+secAdmForm.cleaned_data['prn']
                        my_group=Group.objects.get(name='student')
                        #my_group.user_set.add(user)
                        user.groups.add(my_group)
                        secAdmModule.user=user
                        secAdmModule.save()
                         # for academic
                        # secacd=SecAcademic()
                        # secacd.sec_admission=secAdmModule
                        # secacd.save()
                        messages.success(request, secAdmForm.cleaned_data['fname']+" "+secAdmForm.cleaned_data['faname']+" "+secAdmForm.cleaned_data['lname']+' Student Admitted Sucessfully!')
                        return redirect('admission_secadd')
                except:
                    messages.error(request,"Invalid header found in Secondary Admission form... Try again")
                    return redirect('admission_secadd')    
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            secAdmForm= SecondAdmForm()
        secData=SecondAdm.objects.all()
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Student Admission /",
            'fname':fname,
            "page_path":" Secondary Admission / Admission",
            "menu_icon":"nav-icon fas fa-address-card",
            "secAdmForm":secAdmForm,
            "secData":secData,
            }    
        return render(request, 'schoolviews/admission/secondary_adm.html',context) 
    else:
        return redirect('login')




# College admission Add View
def admission_addCol(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        if request.method == 'POST':
            colAdmForm= CollegeAdmForm(request.POST,request.FILES)
            if colAdmForm.is_valid():
                try:
                    print("ggfdsfd")
                    if CollegeAdm.objects.filter(prn__iexact=colAdmForm.cleaned_data['prn']).exists():
                        messages.error(request,"Register Number Already Exists")
                        return redirect('admission_coladd')
                    elif CollegeAdm.objects.filter(aadhar__iexact=colAdmForm.cleaned_data['aadhar']).exists():
                        messages.error(request,"Aadhar Number Already Exists")
                        return redirect('admission_coladd')
                    elif CollegeAdm.objects.filter(email__iexact=colAdmForm.cleaned_data['email']).exists():
                        messages.error(request,"Email Id Already Exists")
                        return redirect('admission_coladd')                        
                    else:
                        print("ggfdsfd")
                        colAdmModule=CollegeAdm()
                        colAdmModule.prn=colAdmForm.cleaned_data['prn']
                        colAdmModule.lname=colAdmForm.cleaned_data['lname']
                        colAdmModule.fname=colAdmForm.cleaned_data['fname']
                        colAdmModule.faname=colAdmForm.cleaned_data['faname']
                        colAdmModule.moname=colAdmForm.cleaned_data['moname']
                        colAdmModule.mrname=colAdmForm.cleaned_data['mrname']
                        colAdmModule.aadhar=colAdmForm.cleaned_data['aadhar']
                        colAdmModule.saral_id=colAdmForm.cleaned_data['saral_id']
                        colAdmModule.nationality=colAdmForm.cleaned_data['nationality']
                        colAdmModule.tongue=colAdmForm.cleaned_data['tongue']
                        colAdmModule.religion=colAdmForm.cleaned_data['religion']
                        colAdmModule.cast=colAdmForm.cleaned_data['cast']
                        colAdmModule.subcast=colAdmForm.cleaned_data['subcast']
                        colAdmModule.minority=colAdmForm.cleaned_data['minority']
                        colAdmModule.pob=colAdmForm.cleaned_data['pob']
                        colAdmModule.dob=colAdmForm.cleaned_data['dob']
                        colAdmModule.last_school=colAdmForm.cleaned_data['last_school']
                        colAdmModule.last_class=colAdmForm.cleaned_data['last_class']
                        colAdmModule.prevprn=colAdmForm.cleaned_data['prevprn']
                        colAdmModule.prevlcsrno=colAdmForm.cleaned_data['prevlcsrno']
                        colAdmModule.admdate=colAdmForm.cleaned_data['admdate']
                        y=colAdmForm.cleaned_data['admdate']                   
                        mon_list=['01','02','03','04','05']
                        if y[5:7] in mon_list:
                            y=str(int(y[0:4])-1)
                            colAdmModule.admyear=y[0:4]
                        else:
                            colAdmModule.admyear=y[0:4]  
                        colAdmModule.adm_class=colAdmForm.cleaned_data['adm_class']
                        colAdmModule.admission_faculty=colAdmForm.cleaned_data['admission_faculty']
                        colAdmModule.division=colAdmForm.cleaned_data['division']
                        colAdmModule.rollno=colAdmForm.cleaned_data['rollno']
                        colAdmModule.lateadm=colAdmForm.cleaned_data['lateadm']
                        colAdmModule.admtype=colAdmForm.cleaned_data['admtype']
                        colAdmModule.hostel=colAdmForm.cleaned_data['hostel']
                        colAdmModule.sex=colAdmForm.cleaned_data['sex']
                        colAdmModule.pwd=colAdmForm.cleaned_data['pwd']
                        colAdmModule.bgroup=colAdmForm.cleaned_data['bgroup']
                        colAdmModule.fa_mob=colAdmForm.cleaned_data['fa_mob']
                        colAdmModule.mo_mob=colAdmForm.cleaned_data['mo_mob']
                        colAdmModule.fa_occu=colAdmForm.cleaned_data['fa_occu']
                        colAdmModule.mo_occu=colAdmForm.cleaned_data['mo_occu']
                        colAdmModule.fam_income=colAdmForm.cleaned_data['fam_income']
                        colAdmModule.bpl=colAdmForm.cleaned_data['bpl']
                        colAdmModule.gis=colAdmForm.cleaned_data['gis']
                        colAdmModule.ganame=colAdmForm.cleaned_data['ganame']
                        colAdmModule.ga_mob=colAdmForm.cleaned_data['ga_mob']
                        colAdmModule.ga_occu=colAdmForm.cleaned_data['ga_occu']
                        colAdmModule.gaddress=colAdmForm.cleaned_data['gaddress']
                        colAdmModule.ga_relation=colAdmForm.cleaned_data['ga_relation']
                        colAdmModule.email=colAdmForm.cleaned_data['email']
                        colAdmModule.areaType=colAdmForm.cleaned_data['areaType']
                        colAdmModule.caddress=colAdmForm.cleaned_data['caddress']
                        colAdmModule.ca_is_pa_addr=colAdmForm.cleaned_data['ca_is_pa_addr']
                        colAdmModule.paddress=colAdmForm.cleaned_data['paddress']
                        colAdmModule.baccount=colAdmForm.cleaned_data['baccount']
                        colAdmModule.bankname=colAdmForm.cleaned_data['bankname']
                        colAdmModule.ifsc=colAdmForm.cleaned_data['ifsc']
                        colAdmModule.branch=colAdmForm.cleaned_data['branch']
                        colAdmModule.micr=colAdmForm.cleaned_data['micr']
                        colAdmModule.marks_img=colAdmForm.cleaned_data['marks_img']
                        colAdmModule.prv_lc_img=colAdmForm.cleaned_data['prv_lc_img']
                        colAdmModule.addhar_img=colAdmForm.cleaned_data['addhar_img']
                        colAdmModule.cast_img=colAdmForm.cleaned_data['cast_img']
                        colAdmModule.castvald_img=colAdmForm.cleaned_data['castvald_img']
                        colAdmModule.nationality_img=colAdmForm.cleaned_data['nationality_img']
                        colAdmModule.noncrimy_img=colAdmForm.cleaned_data['noncrimy_img']
                        colAdmModule.std_img=colAdmForm.cleaned_data['std_img']
                        colAdmModule.birth_img=colAdmForm.cleaned_data['birth_img']
                        colAdmModule.note=colAdmForm.cleaned_data['note']
                        #for Academics
                        no=int(colAdmForm.cleaned_data['adm_class'])
                        print(no)
                        if no==11:
                            colAdmModule.updateclass11 = colAdmForm.cleaned_data['adm_class']
                            colAdmModule.updateyear11 = y[0:4]
                            colAdmModule.updatedivision11 = str(colAdmForm.cleaned_data['division'])
                            colAdmModule.updaterollno11 = colAdmForm.cleaned_data['rollno']
                            colAdmModule.updatestream11 = colAdmForm.cleaned_data['admission_faculty']

                        elif no==12:
                            colAdmModule.updateclass12 = colAdmForm.cleaned_data['adm_class']
                            colAdmModule.updateyear12 = y[0:4]
                            colAdmModule.updatedivision12 = str(colAdmForm.cleaned_data['division'])
                            colAdmModule.updaterollno12 = colAdmForm.cleaned_data['rollno']
                            colAdmModule.updatestream12 = colAdmForm.cleaned_data['admission_faculty']

                        # Create User for Student
                        print("sgds")
                        user=User.objects.create_user(username=colAdmForm.cleaned_data['aadhar'],email=colAdmForm.cleaned_data['email'],password="Admin@123",first_name=colAdmForm.cleaned_data['fname'],last_name=colAdmForm.cleaned_data['lname'])
                        user.save()
                         # create student id for rejoin
                        # studid=StudID()
                        # studid.stud_id=user
                        # studid.save()
                        colAdmModule.stud_id="c"+str(user.id)+""+colAdmForm.cleaned_data['prn']
                        my_group=Group.objects.get(name='student')
                        #my_group.user_set.add(user)
                        user.groups.add(my_group)
                        colAdmModule.user=user
                        # colAdmModule.lcgenerated=False
                        colAdmModule.save()
                        #for Adademic table
                        # colacd=ColAcademic()
                        # colacd.col_admission=colAdmModule
                        # colacd.save()
                        messages.success(request, colAdmForm.cleaned_data['fname']+" "+colAdmForm.cleaned_data['faname']+" "+colAdmForm.cleaned_data['lname']+' Student Admitted Sucessfully!')
                        return redirect('admission_coladd')
                except:
                    messages.error(request,"Invalid header found in College Admission form... Try again")
                    return redirect('admission_coladd')    
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            colAdmForm = CollegeAdmForm()
            colData = CollegeAdm.objects.all()
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Student Admission /",
            'fname':fname,
            "page_path":" College Admission / Admission",
            "menu_icon":"nav-icon fas fa-address-card",
            "colAdmForm":colAdmForm,
            "colData":colData,
            }    
        return render(request, 'schoolviews/admission/college_adm.html',context) 
    else:
        return redirect('login')




# Form17-10 admission Add View
def admission_addForm1710(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        if request.method == 'POST':
            form1710Form= Form1710AdmForm(request.POST,request.FILES)
            if form1710Form.is_valid():
                try:
                    if Form1710Adm.objects.filter(prn__iexact=form1710Form.cleaned_data['prn']).exists():
                        messages.error(request,"Register Number Already Exists")
                        return redirect('admission_form1710add')
                    elif Form1710Adm.objects.filter(aadhar__iexact=form1710Form.cleaned_data['aadhar']).exists():
                        messages.error(request,"Aadhar Number Already Exists")
                        return redirect('admission_form1710add')
                    elif Form1710Adm.objects.filter(email__iexact=form1710Form.cleaned_data['email']).exists():
                        messages.error(request,"Email Id Already Exists")
                        return redirect('admission_form1710add')                        
                    else:
                        form1710Module=Form1710Adm()
                        form1710Module.prn=form1710Form.cleaned_data['prn']
                        form1710Module.lname=form1710Form.cleaned_data['lname']
                        form1710Module.fname=form1710Form.cleaned_data['fname']
                        form1710Module.faname=form1710Form.cleaned_data['faname']
                        form1710Module.moname=form1710Form.cleaned_data['moname']
                        form1710Module.mrname=form1710Form.cleaned_data['mrname']
                        form1710Module.aadhar=form1710Form.cleaned_data['aadhar']
                        form1710Module.saral_id=form1710Form.cleaned_data['saral_id']
                        form1710Module.nationality=form1710Form.cleaned_data['nationality']
                        form1710Module.tongue=form1710Form.cleaned_data['tongue']
                        form1710Module.religion=form1710Form.cleaned_data['religion']
                        form1710Module.cast=form1710Form.cleaned_data['cast']
                        form1710Module.subcast=form1710Form.cleaned_data['subcast']
                        form1710Module.minority=form1710Form.cleaned_data['minority']
                        form1710Module.pob=form1710Form.cleaned_data['pob']
                        form1710Module.dob=form1710Form.cleaned_data['dob']
                        form1710Module.last_school=form1710Form.cleaned_data['last_school']
                        form1710Module.last_class=form1710Form.cleaned_data['last_class']
                        form1710Module.prevprn=form1710Form.cleaned_data['prevprn']
                        form1710Module.prevlcsrno=form1710Form.cleaned_data['prevlcsrno']
                        form1710Module.admdate=form1710Form.cleaned_data['admdate']
                        y=form1710Form.cleaned_data['admdate']                   
                        mon_list=['01','02','03','04','05']
                        if y[5:7] in mon_list:
                            y=str(int(y[0:4])-1)
                            form1710Module.admyear=y[0:4]
                        else:
                            form1710Module.admyear=y[0:4]
                        form1710Module.adm_class=form1710Form.cleaned_data['adm_class']
                        form1710Module.rollno=form1710Form.cleaned_data['rollno']
                        form1710Module.lateadm=form1710Form.cleaned_data['lateadm']
                        form1710Module.admtype=form1710Form.cleaned_data['admtype']
                        form1710Module.hostel=form1710Form.cleaned_data['hostel']
                        form1710Module.sex=form1710Form.cleaned_data['sex']
                        form1710Module.pwd=form1710Form.cleaned_data['pwd']
                        form1710Module.bgroup=form1710Form.cleaned_data['bgroup']
                        form1710Module.fa_mob=form1710Form.cleaned_data['fa_mob']
                        form1710Module.mo_mob=form1710Form.cleaned_data['mo_mob']
                        form1710Module.fa_occu=form1710Form.cleaned_data['fa_occu']
                        form1710Module.mo_occu=form1710Form.cleaned_data['mo_occu']
                        form1710Module.fam_income=form1710Form.cleaned_data['fam_income']
                        form1710Module.bpl=form1710Form.cleaned_data['bpl']
                        form1710Module.gis=form1710Form.cleaned_data['gis']
                        form1710Module.ganame=form1710Form.cleaned_data['ganame']
                        form1710Module.ga_mob=form1710Form.cleaned_data['ga_mob']
                        form1710Module.ga_occu=form1710Form.cleaned_data['ga_occu']
                        form1710Module.gaddress=form1710Form.cleaned_data['gaddress']
                        form1710Module.ga_relation=form1710Form.cleaned_data['ga_relation']
                        form1710Module.email=form1710Form.cleaned_data['email']
                        form1710Module.areaType=form1710Form.cleaned_data['areaType']
                        form1710Module.caddress=form1710Form.cleaned_data['caddress']
                        form1710Module.ca_is_pa_addr=form1710Form.cleaned_data['ca_is_pa_addr']
                        form1710Module.paddress=form1710Form.cleaned_data['paddress']
                        form1710Module.baccount=form1710Form.cleaned_data['baccount']
                        form1710Module.bankname=form1710Form.cleaned_data['bankname']
                        form1710Module.ifsc=form1710Form.cleaned_data['ifsc']
                        form1710Module.branch=form1710Form.cleaned_data['branch']
                        form1710Module.micr=form1710Form.cleaned_data['micr']
                        form1710Module.marks_img=form1710Form.cleaned_data['marks_img']
                        form1710Module.prv_lc_img=form1710Form.cleaned_data['prv_lc_img']
                        form1710Module.addhar_img=form1710Form.cleaned_data['addhar_img']
                        form1710Module.cast_img=form1710Form.cleaned_data['cast_img']
                        form1710Module.castvald_img=form1710Form.cleaned_data['castvald_img']
                        form1710Module.nationality_img=form1710Form.cleaned_data['nationality_img']
                        form1710Module.noncrimy_img=form1710Form.cleaned_data['noncrimy_img']
                        form1710Module.std_img=form1710Form.cleaned_data['std_img']
                        form1710Module.birth_img=form1710Form.cleaned_data['birth_img']
                        form1710Module.note=form1710Form.cleaned_data['note']
                        # Create User for Student
                        user=User.objects.create_user(username=form1710Form.cleaned_data['aadhar'],email=form1710Form.cleaned_data['email'],password="Admin@123",first_name=form1710Form.cleaned_data['fname'],last_name=form1710Form.cleaned_data['lname'])
                        user.save()
                        # create student id for rejoin
                        # studid=StudID()
                        # studid.stud_id=user
                        # studid.save()
                        form1710Module.stud_id="f10"+str(user.id)+""+form1710Form.cleaned_data['prn']
                        my_group=Group.objects.get(name='student')
                        #my_group.user_set.add(user)
                        user.groups.add(my_group)
                        #form1710Module.u_ref_student=User.objects.get(username=form1710Form.cleaned_data['aadhar'])
                        form1710Module.user=user
                        # form1710Module.lcgenerated=False
                        # print("fsdaf")
                        form1710Module.save()
                        print("fsdaf")
                        messages.success(request, form1710Form.cleaned_data['fname']+" "+form1710Form.cleaned_data['faname']+" "+form1710Form.cleaned_data['lname']+' Student Admitted Sucessfully!')
                        return redirect('admission_form1710add')
                except:
                    messages.error(request,"Invalid header found in Form17 10 Admission form... Try again")
                    return redirect('admission_form1710add')    
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form1710Form = Form1710AdmForm()
            form10Data = Form1710Adm.objects.all()

        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Student Admission /",
            'fname':fname,
            "page_path":" Form17 10 Admission / Admission",
            "menu_icon":"nav-icon fas fa-address-card",
            "form1710Form":form1710Form,
            "form10Data":form10Data,
            }    
        return render(request, 'schoolviews/admission/form1710_adm.html',context) 
    else:
        return redirect('login') 




# Form17-12 admission Add View
def admission_addForm1712(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        if request.method == 'POST':
            form1712Form= Form1712AdmForm(request.POST,request.FILES)
            if form1712Form.is_valid():
                try:
                    print("ggfdsfd")
                    if Form1712Adm.objects.filter(prn__iexact=form1712Form.cleaned_data['prn']).exists():
                        messages.error(request,"Register Number Already Exists")
                        return redirect('admission_form1712add')
                    elif Form1712Adm.objects.filter(aadhar__iexact=form1712Form.cleaned_data['aadhar']).exists():
                        messages.error(request,"Aadhar Number Already Exists")
                        return redirect('admission_form1712add')
                    elif Form1712Adm.objects.filter(email__iexact=form1712Form.cleaned_data['email']).exists():
                        messages.error(request,"Email Id Already Exists")
                        return redirect('admission_form1712add')                        
                    else:
                        print("ggfdsfd")
                        form1712AdmModule=Form1712Adm()
                        form1712AdmModule.prn=form1712Form.cleaned_data['prn']
                        form1712AdmModule.lname=form1712Form.cleaned_data['lname']
                        form1712AdmModule.fname=form1712Form.cleaned_data['fname']
                        form1712AdmModule.faname=form1712Form.cleaned_data['faname']
                        form1712AdmModule.moname=form1712Form.cleaned_data['moname']
                        form1712AdmModule.mrname=form1712Form.cleaned_data['mrname']
                        form1712AdmModule.aadhar=form1712Form.cleaned_data['aadhar']
                        form1712AdmModule.saral_id=form1712Form.cleaned_data['saral_id']
                        form1712AdmModule.nationality=form1712Form.cleaned_data['nationality']
                        form1712AdmModule.tongue=form1712Form.cleaned_data['tongue']
                        form1712AdmModule.religion=form1712Form.cleaned_data['religion']
                        form1712AdmModule.cast=form1712Form.cleaned_data['cast']
                        form1712AdmModule.subcast=form1712Form.cleaned_data['subcast']
                        form1712AdmModule.minority=form1712Form.cleaned_data['minority']
                        form1712AdmModule.pob=form1712Form.cleaned_data['pob']
                        form1712AdmModule.dob=form1712Form.cleaned_data['dob']
                        form1712AdmModule.last_school=form1712Form.cleaned_data['last_school']
                        form1712AdmModule.last_class=form1712Form.cleaned_data['last_class']
                        form1712AdmModule.prevprn=form1712Form.cleaned_data['prevprn']
                        form1712AdmModule.prevlcsrno=form1712Form.cleaned_data['prevlcsrno']
                        form1712AdmModule.admdate=form1712Form.cleaned_data['admdate']
                        y=form1712Form.cleaned_data['admdate']                   
                        mon_list=['01','02','03','04','05']
                        if y[5:7] in mon_list:
                            y=str(int(y[0:4])-1)
                            form1712AdmModule.admyear=y[0:4]
                        else:
                            form1712AdmModule.admyear=y[0:4]
                        form1712AdmModule.adm_class=form1712Form.cleaned_data['adm_class']
                        form1712AdmModule.admission_faculty=form1712Form.cleaned_data['admission_faculty']
                        form1712AdmModule.rollno=form1712Form.cleaned_data['rollno']
                        form1712AdmModule.lateadm=form1712Form.cleaned_data['lateadm']
                        form1712AdmModule.admtype=form1712Form.cleaned_data['admtype']
                        form1712AdmModule.hostel=form1712Form.cleaned_data['hostel']
                        form1712AdmModule.sex=form1712Form.cleaned_data['sex']
                        form1712AdmModule.pwd=form1712Form.cleaned_data['pwd']
                        form1712AdmModule.bgroup=form1712Form.cleaned_data['bgroup']
                        form1712AdmModule.fa_mob=form1712Form.cleaned_data['fa_mob']
                        form1712AdmModule.mo_mob=form1712Form.cleaned_data['mo_mob']
                        form1712AdmModule.fa_occu=form1712Form.cleaned_data['fa_occu']
                        form1712AdmModule.mo_occu=form1712Form.cleaned_data['mo_occu']
                        form1712AdmModule.fam_income=form1712Form.cleaned_data['fam_income']
                        form1712AdmModule.bpl=form1712Form.cleaned_data['bpl']
                        form1712AdmModule.gis=form1712Form.cleaned_data['gis']
                        form1712AdmModule.ganame=form1712Form.cleaned_data['ganame']
                        form1712AdmModule.ga_mob=form1712Form.cleaned_data['ga_mob']
                        form1712AdmModule.ga_occu=form1712Form.cleaned_data['ga_occu']
                        form1712AdmModule.gaddress=form1712Form.cleaned_data['gaddress']
                        form1712AdmModule.ga_relation=form1712Form.cleaned_data['ga_relation']
                        form1712AdmModule.email=form1712Form.cleaned_data['email']
                        form1712AdmModule.areaType=form1712Form.cleaned_data['areaType']
                        form1712AdmModule.caddress=form1712Form.cleaned_data['caddress']
                        form1712AdmModule.ca_is_pa_addr=form1712Form.cleaned_data['ca_is_pa_addr']
                        form1712AdmModule.paddress=form1712Form.cleaned_data['paddress']
                        form1712AdmModule.baccount=form1712Form.cleaned_data['baccount']
                        form1712AdmModule.bankname=form1712Form.cleaned_data['bankname']
                        form1712AdmModule.ifsc=form1712Form.cleaned_data['ifsc']
                        form1712AdmModule.branch=form1712Form.cleaned_data['branch']
                        form1712AdmModule.micr=form1712Form.cleaned_data['micr']
                        form1712AdmModule.marks_img=form1712Form.cleaned_data['marks_img']
                        form1712AdmModule.prv_lc_img=form1712Form.cleaned_data['prv_lc_img']
                        form1712AdmModule.addhar_img=form1712Form.cleaned_data['addhar_img']
                        form1712AdmModule.cast_img=form1712Form.cleaned_data['cast_img']
                        form1712AdmModule.castvald_img=form1712Form.cleaned_data['castvald_img']
                        form1712AdmModule.nationality_img=form1712Form.cleaned_data['nationality_img']
                        form1712AdmModule.noncrimy_img=form1712Form.cleaned_data['noncrimy_img']
                        form1712AdmModule.std_img=form1712Form.cleaned_data['std_img']
                        form1712AdmModule.birth_img=form1712Form.cleaned_data['birth_img']
                        form1712AdmModule.note=form1712Form.cleaned_data['note']
                        # Create User for Student
                        print("sgds")
                        user=User.objects.create_user(username=form1712Form.cleaned_data['aadhar'],email=form1712Form.cleaned_data['email'],password="Admin@123",first_name=form1712Form.cleaned_data['fname'],last_name=form1712Form.cleaned_data['lname'])
                        user.save()
                         # create student id for rejoin
                        # studid=StudID()
                        # studid.stud_id=user
                        # studid.save()
                        form1712AdmModule.stud_id="f12"+str(user.id)+""+form1712Form.cleaned_data['prn']
                        my_group=Group.objects.get(name='student')
                        #my_group.user_set.add(user)
                        user.groups.add(my_group)
                        form1712AdmModule.user=user
                        # form1712AdmModule.lcgenerated=False
                        form1712AdmModule.save()
                        messages.success(request, form1712Form.cleaned_data['fname']+" "+form1712Form.cleaned_data['faname']+" "+form1712Form.cleaned_data['lname']+' Student Admitted Sucessfully!')
                        return redirect('admission_form1712add')
                except:
                    messages.error(request,"Invalid header found in Form17 12 Admission form... Try again")
                    return redirect('admission_form1712add')    
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form1712Form= Form1712AdmForm()
            form12Data = Form1712Adm.objects.all()
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Student Admission /",
            'fname':fname,
            "page_path":"  Form17 12 Admission / Admission",
            "menu_icon":"nav-icon fas fa-address-card",
            "form1712Form":form1712Form,
            "form12Data":form12Data,
            }    
        return render(request, 'schoolviews/admission/form1712_adm.html',context) 
    else:
        return redirect('login')



# 11-ATKT admission Add View
def admission_addATKT11(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        atktData = ATKT11Adm.objects.all()
        if request.method == 'POST':
            atktAdmForm= ATKT11AdmForm(request.POST,request.FILES)
            if atktAdmForm.is_valid():
                try:
                    print("ggfdsfd")
                    if ATKT11Adm.objects.filter(prn__iexact=atktAdmForm.cleaned_data['prn']).exists():
                        messages.error(request,"Register Number Already Exists")
                        return redirect('admission_addATKT11')
                    elif ATKT11Adm.objects.filter(aadhar__iexact=atktAdmForm.cleaned_data['aadhar']).exists():
                        messages.error(request,"Aadhar Number Already Exists")
                        return redirect('admission_addATKT11')
                    elif ATKT11Adm.objects.filter(email__iexact=atktAdmForm.cleaned_data['email']).exists():
                        messages.error(request,"Email Id Already Exists")
                        return redirect('admission_addATKT11')                        
                    else:
                        print("ggfdsfd")
                        atktAdmModule=ATKT11Adm()
                        atktAdmModule.prn=atktAdmForm.cleaned_data['prn']
                        atktAdmModule.lname=atktAdmForm.cleaned_data['lname']
                        atktAdmModule.fname=atktAdmForm.cleaned_data['fname']
                        atktAdmModule.faname=atktAdmForm.cleaned_data['faname']
                        atktAdmModule.moname=atktAdmForm.cleaned_data['moname']
                        atktAdmModule.mrname=atktAdmForm.cleaned_data['mrname']
                        atktAdmModule.aadhar=atktAdmForm.cleaned_data['aadhar']
                        atktAdmModule.saral_id=atktAdmForm.cleaned_data['saral_id']
                        atktAdmModule.nationality=atktAdmForm.cleaned_data['nationality']
                        atktAdmModule.tongue=atktAdmForm.cleaned_data['tongue']
                        atktAdmModule.religion=atktAdmForm.cleaned_data['religion']
                        atktAdmModule.cast=atktAdmForm.cleaned_data['cast']
                        atktAdmModule.subcast=atktAdmForm.cleaned_data['subcast']
                        atktAdmModule.minority=atktAdmForm.cleaned_data['minority']
                        atktAdmModule.pob=atktAdmForm.cleaned_data['pob']
                        atktAdmModule.dob=atktAdmForm.cleaned_data['dob']
                        atktAdmModule.last_school=atktAdmForm.cleaned_data['last_school']
                        atktAdmModule.last_class=atktAdmForm.cleaned_data['last_class']
                        atktAdmModule.prevprn=atktAdmForm.cleaned_data['prevprn']
                        atktAdmModule.prevlcsrno=atktAdmForm.cleaned_data['prevlcsrno']
                        atktAdmModule.admdate=atktAdmForm.cleaned_data['admdate']
                        y=atktAdmForm.cleaned_data['admdate']
                        mon_list=['01','02','03','04','05']
                        if y[5:7] in mon_list:
                            y=str(int(y[0:4])-1)
                            atktAdmModule.admyear=y[0:4]
                        else:
                            atktAdmModule.admyear=y[0:4]
                        atktAdmModule.adm_class=atktAdmForm.cleaned_data['adm_class']
                        atktAdmModule.admission_faculty=atktAdmForm.cleaned_data['admission_faculty']
                        atktAdmModule.division=atktAdmForm.cleaned_data['division']
                        atktAdmModule.rollno=atktAdmForm.cleaned_data['rollno']
                        atktAdmModule.lateadm=atktAdmForm.cleaned_data['lateadm']
                        atktAdmModule.admtype=atktAdmForm.cleaned_data['admtype']
                        atktAdmModule.hostel=atktAdmForm.cleaned_data['hostel']
                        atktAdmModule.sex=atktAdmForm.cleaned_data['sex']
                        atktAdmModule.pwd=atktAdmForm.cleaned_data['pwd']
                        atktAdmModule.bgroup=atktAdmForm.cleaned_data['bgroup']
                        atktAdmModule.fa_mob=atktAdmForm.cleaned_data['fa_mob']
                        atktAdmModule.mo_mob=atktAdmForm.cleaned_data['mo_mob']
                        atktAdmModule.fa_occu=atktAdmForm.cleaned_data['fa_occu']
                        atktAdmModule.mo_occu=atktAdmForm.cleaned_data['mo_occu']
                        atktAdmModule.fam_income=atktAdmForm.cleaned_data['fam_income']
                        atktAdmModule.bpl=atktAdmForm.cleaned_data['bpl']
                        atktAdmModule.gis=atktAdmForm.cleaned_data['gis']
                        atktAdmModule.ganame=atktAdmForm.cleaned_data['ganame']
                        atktAdmModule.ga_mob=atktAdmForm.cleaned_data['ga_mob']
                        atktAdmModule.ga_occu=atktAdmForm.cleaned_data['ga_occu']
                        atktAdmModule.gaddress=atktAdmForm.cleaned_data['gaddress']
                        atktAdmModule.ga_relation=atktAdmForm.cleaned_data['ga_relation']
                        atktAdmModule.email=atktAdmForm.cleaned_data['email']
                        atktAdmModule.areaType=atktAdmForm.cleaned_data['areaType']
                        atktAdmModule.caddress=atktAdmForm.cleaned_data['caddress']
                        atktAdmModule.ca_is_pa_addr=atktAdmForm.cleaned_data['ca_is_pa_addr']
                        atktAdmModule.paddress=atktAdmForm.cleaned_data['paddress']
                        atktAdmModule.baccount=atktAdmForm.cleaned_data['baccount']
                        atktAdmModule.bankname=atktAdmForm.cleaned_data['bankname']
                        atktAdmModule.ifsc=atktAdmForm.cleaned_data['ifsc']
                        atktAdmModule.branch=atktAdmForm.cleaned_data['branch']
                        atktAdmModule.micr=atktAdmForm.cleaned_data['micr']
                        atktAdmModule.marks_img=atktAdmForm.cleaned_data['marks_img']
                        atktAdmModule.prv_lc_img=atktAdmForm.cleaned_data['prv_lc_img']
                        atktAdmModule.addhar_img=atktAdmForm.cleaned_data['addhar_img']
                        atktAdmModule.cast_img=atktAdmForm.cleaned_data['cast_img']
                        atktAdmModule.castvald_img=atktAdmForm.cleaned_data['castvald_img']
                        atktAdmModule.nationality_img=atktAdmForm.cleaned_data['nationality_img']
                        atktAdmModule.noncrimy_img=atktAdmForm.cleaned_data['noncrimy_img']
                        atktAdmModule.std_img=atktAdmForm.cleaned_data['std_img']
                        atktAdmModule.birth_img=atktAdmForm.cleaned_data['birth_img']
                        atktAdmModule.note=atktAdmForm.cleaned_data['note']
                        #for bonafide
                        atktAdmModule.bonafide_img=atktAdmForm.cleaned_data['bonafide_img']
                        atktAdmModule.bonaissuedate=atktAdmForm.cleaned_data['bonaissuedate']
                        atktAdmModule.bonasrno=atktAdmForm.cleaned_data['bonasrno']
                        # Create User for Student
                        print("sgds")
                        user=User.objects.create_user(username=atktAdmForm.cleaned_data['aadhar'],email=atktAdmForm.cleaned_data['email'],password="Admin@123",first_name=atktAdmForm.cleaned_data['fname'],last_name=atktAdmForm.cleaned_data['lname'])
                        user.save()
                         # create student id for rejoin
                        # studid=StudID()
                        # studid.stud_id=user
                        # studid.save()
                        atktAdmModule.stud_id="atkt"+str(user.id)+""+atktAdmForm.cleaned_data['prn']
                        my_group=Group.objects.get(name='student')
                        #my_group.user_set.add(user)
                        user.groups.add(my_group)
                        atktAdmModule.user=user
                        # atktAdmModule.lcgenerated=False
                        atktAdmModule.save()
                        #for Adademic table
                        # colacd=ColAcademic()
                        # colacd.col_admission=atktAdmModule
                        # colacd.save()
                        messages.success(request, atktAdmForm.cleaned_data['fname']+" "+atktAdmForm.cleaned_data['faname']+" "+atktAdmForm.cleaned_data['lname']+' Student Admitted Sucessfully!')
                        return redirect('admission_addATKT11')
                except:
                    messages.error(request,"Invalid header found in 11-ATKT Admission form... Try again")
                    return redirect('admission_addATKT11')    
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            atktAdmForm = ATKT11AdmForm()
            atktData = ATKT11Adm.objects.all()
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Student Admission /",
            'fname':fname,
            "page_path":" 11-ATKT Admission / Admission",
            "menu_icon":"nav-icon fas fa-address-card",
            "atktAdmForm":atktAdmForm,
            "atktData":atktData,
            }    
        return render(request, 'schoolviews/admission/atkt11_adm.html',context) 
    else:
        return redirect('login')



# for Cast Category
def load_castCat(request):
    caste = request.GET.get('caste')
    casteData = Cast.objects.get(pk=caste)
    return render(request,'schoolviews/admission/castCatAjax.html',{"casteData":casteData})


# for primary division assign
def admission_pridivassign(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['priclass'])
                dData = Division.objects.get(division=request.POST['division'])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    priData = PrimAdm.objects.get(pk=studid[x])
                    print(studid[x])
                    priData.division=dData
                    if class1 == 1:
                        priData.updatedivision1=request.POST['division']
                    elif class1 == 2:
                        priData.updatedivision2=request.POST['division']
                    elif class1 == 3:
                        priData.updatedivision3=request.POST['division']
                    elif class1 == 4:
                        priData.updatedivision4=request.POST['division']
                    priData.save()
                messages.success(request,'Division Assigned Sucessfully!')
                return redirect('admission_pridivassign')
            except:
                messages.error(request,"Invalid header found in Division Assign form... Try again")
                return redirect('admission_pridivassign')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Primary Division Assign ",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/primarydivisionassign.html',context) 
    else:
        return redirect('login')


# for primary division 
def load_pristudents(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    if class1 == 1:
        students = PrimAdm.objects.filter(updateclass1=class1,updateyear1=year[0:4],updateclass2=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 2:
        students = PrimAdm.objects.filter(updateclass2=class1,updateyear2=year[0:4],updateclass3=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 3:
        students = PrimAdm.objects.filter(updateclass3=class1,updateyear3=year[0:4],updateclass4=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 4:
        students = PrimAdm.objects.filter(updateclass4=class1,updateyear4=year[0:4],lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/students.html',{"students":students})


# for Secondary division assign
def admission_secdivassign(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                dData = Division.objects.get(division=request.POST['division'])
                class1 = int(request.POST['secclass'])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    secData = SecondAdm.objects.get(pk=studid[x])
                    secData.division=dData
                    if class1 == 5:
                        secData.updatedivision5 = request.POST['division']
                    elif class1 == 6:
                        secData.updatedivision6 = request.POST['division']
                    elif class1 == 7:
                        secData.updatedivision7 = request.POST['division']
                    elif class1 == 8:
                        secData.updatedivision8 = request.POST['division']
                    elif class1 == 9:
                        secData.updatedivision9 = request.POST['division']
                    elif class1 == 10:
                        secData.updatedivision10 = request.POST['division']
                    secData.save()
                messages.success(request,'Secondary Division Assigned Sucessfully!')
                return redirect('admission_secdivassign')
            except:
                messages.error(request,"Invalid header found in Division Assign form... Try again")
                return redirect('admission_secdivassign')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Secondary Division Assign ",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/secondarydivisionassign.html',context) 
    else:
        return redirect('login')


# for Secondary division 
def load_secstudents(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    if class1 == 5:
        students = SecondAdm.objects.filter(updateclass5=class1,updateyear5=year[0:4],updateclass6=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 6:
        students = SecondAdm.objects.filter(updateclass6=class1,updateyear6=year[0:4],updateclass7=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 7:
        students = SecondAdm.objects.filter(updateclass7=class1,updateyear7=year[0:4],updateclass8=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 8:
        students = SecondAdm.objects.filter(updateclass8=class1,updateyear8=year[0:4],updateclass9=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 9:
        students = SecondAdm.objects.filter(updateclass9=class1,updateyear9=year[0:4],updateclass10=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 10:
        students = SecondAdm.objects.filter(updateclass10=class1,updateyear10=year[0:4],lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/students.html',{"students":students})



# for College division assign
def admission_coldivassign(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                print(1)
                dData = Division.objects.get(division=request.POST['division'])
                class1 = int(request.POST['colclass'])
                studid=request.POST['studid'].split(",")
                print(studid[0])
                for x in range(0,len(studid)):
                    if CollegeAdm.objects.filter(prn=studid[x]).exists():
                        colData = CollegeAdm.objects.get(prn=studid[x])
                        colData.division=dData
                        if class1 == 11:
                            colData.updatedivision11=request.POST['division']
                        elif class1 == 12:
                            colData.updatedivision12=request.POST['division']
                        colData.save()
                    elif ATKT11Adm.objects.filter(prn=studid[x]).exists():
                        atkt11Data = ATKT11Adm.objects.get(prn=studid[x])
                        atkt11Data.division=dData
                        atkt11Data.save()
                messages.success(request,'College Division Assigned Sucessfully!')
                return redirect('admission_coldivassign')
            except:
                messages.error(request,"Invalid header found in Division Assign form... Try again")
                return redirect('admission_coldivassign')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" College Division Assign ",
            "menu_icon":"nav-icon fas fa-university",
            }
        return render(request,'schoolviews/academics/collegedivisionassign.html',context) 
    else:
        return redirect('login')


# for College division 
def load_colstudents(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    stream = request.GET.get('stream')
    atktstudents=""
    if class1 == 11:
        atktstudents = ATKT11Adm.objects.filter(adm_class=class1,admyear=year[0:4],admission_faculty=stream,lcgenerated=0)  
        students = CollegeAdm.objects.filter(updateclass11=class1,updateyear11=year[0:4],admission_faculty=stream,updateclass12=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 12:
        students = CollegeAdm.objects.filter(updateclass12=class1,updateyear12=year[0:4],admission_faculty=stream,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    print(atktstudents)
    return render(request,'schoolviews/academics/studentsclg.html',{"students":students,'atktstudents':atktstudents})



# for primary Standardpromote
def admission_pristdpromote(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['priclass_to_pro'])
                year = str(request.POST['priyear_pro'])
                year = int(year[0:4])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    priData = PrimAdm.objects.get(pk=studid[x])
                    print(studid[x])
                    if class1 == 2:
                        priData.updateclass2=str(class1)
                        priData.updateyear2=year+1
                        priData.updatedivision2=priData.updatedivision1
                        priData.updaterollno2=priData.rollno
                        print(1234)
                    elif class1 == 3:
                        priData.updateclass3=str(class1)
                        priData.updateyear3=year+1
                        priData.updatedivision3=priData.updatedivision2
                        priData.updaterollno3=priData.rollno
                    elif class1 == 4:
                        priData.updateclass4=str(class1)
                        priData.updateyear4=year+1
                        priData.updatedivision4=priData.updatedivision3
                        priData.updaterollno4=priData.rollno
                    priData.save()
                messages.success(request,'Standard Promoted Sucessfully!')
                return redirect('admission_pristdpromote')
            except:
                messages.error(request,"Invalid header found in Standard Promote form... Try again")
                return redirect('admission_pristdpromote')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Primary Standard Promote",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/primarystdpromote.html',context) 
    else:
        return redirect('login')


# for primary promote 
def load_pristudents_pro(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 1:
        students = PrimAdm.objects.filter(updateclass1=class1,updateyear1=year[0:4],updatedivision1=div,updateclass2=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 2:
        students = PrimAdm.objects.filter(updateclass2=class1,updateyear2=year[0:4],updatedivision2=div,updateclass3=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 3:
        students = PrimAdm.objects.filter(updateclass3=class1,updateyear3=year[0:4],updatedivision3=div,updateclass4=None,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentspromote.html',{"students":students})




# for Secondary Standardpromote
def admission_secstdpromote(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['secclass_to_pro'])
                year = str(request.POST['secyear_pro'])
                year = int(year[0:4])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    secData = SecondAdm.objects.get(pk=studid[x])
                    if class1 == 6:
                        secData.updateclass6="6"
                        secData.updateyear6=year+1
                        secData.updatedivision6=secData.updatedivision5
                        secData.updaterollno6=secData.rollno
                    elif class1 == 7:
                        secData.updateclass7="7"
                        secData.updateyear7=year+1
                        secData.updatedivision7=secData.updatedivision6
                        secData.updaterollno7=secData.rollno
                    elif class1 == 8:
                        secData.updateclass8="8"
                        secData.updateyear8=year+1
                        secData.updatedivision8=secData.updatedivision7
                        secData.updaterollno8=secData.rollno
                    elif class1 == 9:
                        secData.updateclass9="9"
                        secData.updateyear9=year+1
                        secData.updatedivision9=secData.updatedivision8
                        secData.updaterollno9=secData.rollno
                    elif class1 == 10:
                        secData.updateclass10="10"
                        secData.updateyear10=year+1
                        secData.updatedivision10=secData.updatedivision9
                        secData.updaterollno10=secData.rollno
                    secData.save()
                messages.success(request,'Standard Promoted Sucessfully!')
                return redirect('admission_secstdpromote')
            except:
                messages.error(request,"Invalid header found in Standard Promote form... Try again")
                return redirect('admission_secstdpromote')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Secondary Standard Promote",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/secondarystdpromote.html',context) 
    else:
        return redirect('login')


# for Secondary promote 
def load_secstudents_pro(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 5:
        students = SecondAdm.objects.filter(updateclass5=class1,updateyear5=year[0:4],updatedivision5=div,updateclass6=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 6:
        students = SecondAdm.objects.filter(updateclass6=class1,updateyear6=year[0:4],updatedivision6=div,updateclass7=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 7:
        students = SecondAdm.objects.filter(updateclass7=class1,updateyear7=year[0:4],updatedivision7=div,updateclass8=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 8:
        students = SecondAdm.objects.filter(updateclass8=class1,updateyear8=year[0:4],updatedivision8=div,updateclass9=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 9:
        students = SecondAdm.objects.filter(updateclass9=class1,updateyear9=year[0:4],updatedivision9=div,updateclass10=None,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentspromote.html',{"students":students})




# for Secondary Standardpromote
def admission_colstdpromote(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['colclass_to_pro'])
                year = str(request.POST['colyear_pro'])
                year = int(year[0:4])
                stream = request.POST['colstream_promote']
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    colData = CollegeAdm.objects.get(pk=studid[x])
                    if class1 == 12:
                        colData.updateclass12="12"
                        colData.updatestream12=stream
                        colData.updateyear12=year+1
                        colData.updatedivision12=colData.updatedivision11
                        colData.updaterollno12=colData.rollno
                    colData.save()
                messages.success(request,'Standard Promoted Sucessfully!')
                return redirect('admission_colstdpromote')
            except:
                messages.error(request,"Invalid header found in Standard Promote form... Try again")
                return redirect('admission_colstdpromote')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" College Standard Promote",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/collegestdpromote.html',context) 
    else:
        return redirect('login')


# for College promote 
def load_colstudents_pro(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    stream = request.GET.get('stream')
    print(class1,year,div,stream)
    if class1 == 11:
        students = CollegeAdm.objects.filter(updateclass11=class1,updateyear11=year[0:4],updatedivision11=div,updatestream11=stream,updateclass12=None,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentspromote.html',{"students":students})



# for primary Standard demote
def admission_pristddemote(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['priclass_to_de'])
                year = str(request.POST['priyear_de'])
                year = int(year[0:4])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    priData = PrimAdm.objects.get(pk=studid[x])
                    print(studid[x])
                    if class1 == 1:
                        priData.updateclass1=str(class1)
                        priData.updateyear1=year-1
                        priData.updatedivision1=priData.updatedivision2
                        priData.updaterollno1=priData.rollno

                        priData.updateclass2=priData.updateyear2=priData.updatedivision2=priData.updaterollno2=None
                        priData.updateclass3=priData.updateyear3=priData.updatedivision3=priData.updaterollno3=None
                        priData.updateclass4=priData.updateyear4=priData.updatedivision4=priData.updaterollno4=None
                    elif class1 == 2:
                        priData.updateclass2=str(class1)
                        priData.updateyear2=year-1
                        priData.updatedivision2=priData.updatedivision3
                        priData.updaterollno2=priData.rollno

                        priData.updateclass3=priData.updateyear3=priData.updatedivision3=priData.updaterollno3=None
                        priData.updateclass4=priData.updateyear4=priData.updatedivision4=priData.updaterollno4=None
                    elif class1 == 3:
                        priData.updateclass3=str(class1)
                        priData.updateyear3=year-1
                        priData.updatedivision3=priData.updatedivision4
                        priData.updaterollno3=priData.rollno

                        priData.updateclass4=priData.updateyear4=priData.updatedivision4=priData.updaterollno4=None
                    priData.save()
                messages.success(request,'Standard Demote Sucessfully!')
                return redirect('admission_pristddemote')
            except:
                messages.error(request,"Invalid header found in Standard Demote form... Try again")
                return redirect('admission_pristddemote')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Primary Standard Demote",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/primarystddemote.html',context) 
    else:
        return redirect('login')


# for primary demote 
def load_pristudents_de(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 2:
        students = PrimAdm.objects.filter(updateclass2=class1,updateyear2=year[0:4],updatedivision2=div,updateclass3=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 3:
        students = PrimAdm.objects.filter(updateclass3=class1,updateyear3=year[0:4],updatedivision3=div,updateclass4=None,lcgenerated=0,terminatebyprincipal=0)
    if class1 == 4:
        students = PrimAdm.objects.filter(updateclass4=class1,updateyear4=year[0:4],updatedivision4=div,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentsdemote.html',{"students":students})




# for Secondary Standard demote
def admission_secstddemote(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['secclass_to_de'])
                year = str(request.POST['secyear_de'])
                year = int(year[0:4])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    secData = SecondAdm.objects.get(pk=studid[x])
                    if class1 == 5:
                        secData.updateclass5="5"
                        secData.updateyear5=year-1
                        secData.updatedivision5=secData.updatedivision6
                        secData.updaterollno5=secData.rollno

                        secData.updateclass6=secData.updateyear6=secData.updatedivision6=secData.updaterollno6=None
                        secData.updateclass7=secData.updateyear7=secData.updatedivision7=secData.updaterollno7=None
                        secData.updateclass8=secData.updateyear8=secData.updatedivision8=secData.updaterollno8=None
                        secData.updateclass9=secData.updateyear9=secData.updatedivision9=secData.updaterollno9=None
                        secData.updateclass10=secData.updateyear10=secData.updatedivision10=secData.updaterollno10=None
                    elif class1 == 6:
                        secData.updateclass6="6"
                        secData.updateyear6=year-1
                        secData.updatedivision6=secData.updatedivision7
                        secData.updaterollno6=secData.rollno

                        secData.updateclass7=secData.updateyear7=secData.updatedivision7=secData.updaterollno7=None
                        secData.updateclass8=secData.updateyear8=secData.updatedivision8=secData.updaterollno8=None
                        secData.updateclass9=secData.updateyear9=secData.updatedivision9=secData.updaterollno9=None
                        secData.updateclass10=secData.updateyear10=secData.updatedivision10=secData.updaterollno10=None
                    elif class1 == 7:
                        secData.updateclass7="7"
                        secData.updateyear7=year-1
                        secData.updatedivision7=secData.updatedivision8
                        secData.updaterollno7=secData.rollno

                        secData.updateclass8=secData.updateyear8=secData.updatedivision8=secData.updaterollno8=None
                        secData.updateclass9=secData.updateyear9=secData.updatedivision9=secData.updaterollno9=None
                        secData.updateclass10=secData.updateyear10=secData.updatedivision10=secData.updaterollno10=None
                    elif class1 == 8:
                        secData.updateclass8="8"
                        secData.updateyear8=year-1
                        secData.updatedivision8=secData.updatedivision9
                        secData.updaterollno8=secData.rollno

                        secData.updateclass9=secData.updateyear9=secData.updatedivision9=secData.updaterollno9=None
                        secData.updateclass10=secData.updateyear10=secData.updatedivision10=secData.updaterollno10=None
                    elif class1 == 9:
                        secData.updateclass9="9"
                        secData.updateyear9=year-1
                        secData.updatedivision9=secData.updatedivision10
                        secData.updaterollno9=secData.rollno

                        secData.updateclass10=secData.updateyear10=secData.updatedivision10=secData.updaterollno10=None
                    secData.save()
                messages.success(request,'Standard Demote Sucessfully!')
                return redirect('admission_secstddemote')
            except:
                messages.error(request,"Invalid header found in Standard Demote form... Try again")
                return redirect('admission_secstddemote')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Secondary Standard Demote",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/secondarystddemote.html',context) 
    else:
        return redirect('login')





# for Secondary demote 
def load_secstudents_de(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 6:
        students = SecondAdm.objects.filter(updateclass6=class1,updateyear6=year[0:4],updatedivision6=div,updateclass7=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 7:
        students = SecondAdm.objects.filter(updateclass7=class1,updateyear7=year[0:4],updatedivision7=div,updateclass8=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 8:
        students = SecondAdm.objects.filter(updateclass8=class1,updateyear8=year[0:4],updatedivision8=div,updateclass9=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 9:
        students = SecondAdm.objects.filter(updateclass9=class1,updateyear9=year[0:4],updatedivision9=div,updateclass10=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 10:
        students = SecondAdm.objects.filter(updateclass10=class1,updateyear10=year[0:4],updatedivision10=div,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentsdemote.html',{"students":students})




# for College Standard demote
def admission_colstddemote(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['colclass_to_de'])
                year = str(request.POST['colyear_de'])
                year = int(year[0:4])
                stream = request.POST['colstream_demote']
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    colData = CollegeAdm.objects.get(pk=studid[x])                    
                    if class1 == 11:
                        colData.updateclass11="11"
                        colData.updatestream11=stream
                        colData.updateyear11=year-1
                        colData.updatedivision11=colData.updatedivision12
                        colData.updaterollno11=colData.rollno

                        colData.updateclass12=colData.updateyear12=colData.updatedivision12=colData.updaterollno12=colData.updatestream12=None
                    colData.save()
                messages.success(request,'Standard Demote Sucessfully!')
                return redirect('admission_colstddemote')
            except:
                messages.error(request,"Invalid header found in Standard Demote form... Try again")
                return redirect('admission_colstddemote')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" College Standard Demote",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/collegestddemote.html',context) 
    else:
        return redirect('login')


# for College demote
def load_colstudents_de(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    stream = request.GET.get('stream')
    if class1 == 12:
        students = CollegeAdm.objects.filter(updateclass12=class1,updateyear12=year[0:4],updatedivision12=div,updatestream12=stream,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentsdemote.html',{"students":students})




# for primary Roll No
def admissionpri_rollno(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['priclass_rollno'])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    priData = PrimAdm.objects.get(pk=studid[x])
                    print(studid[x])
                    if class1 == 1:
                        priData.updaterollno1=x+1
                        priData.rollno=x+1
                    elif class1 == 2:
                        priData.updaterollno2=x+1
                        priData.rollno=x+1
                    elif class1 == 3:
                        priData.updaterollno3=x+1
                        priData.rollno=x+1
                    elif class1 == 4:
                        priData.updaterollno4=x+1
                        priData.rollno=x+1
                    priData.save()
                messages.success(request,'Roll No Assigned Sucessfully!')
                return redirect('admissionpri_rollno')
            except:
                messages.error(request,"Invalid header found in Roll No form... Try again")
                return redirect('admissionpri_rollno')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Primary Roll No Assign",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/primaryrollno.html',context) 
    else:
        return redirect('login')


# for primary Roll No 
def load_pristudentsrollno(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 1:
        students = PrimAdm.objects.filter(updateclass1=class1,updateyear1=year[0:4],updatedivision1=div,updateclass2=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 2:
        students = PrimAdm.objects.filter(updateclass2=class1,updateyear2=year[0:4],updatedivision2=div,updateclass3=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 3:
        students = PrimAdm.objects.filter(updateclass3=class1,updateyear3=year[0:4],updatedivision3=div,updateclass4=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 4:
        students = PrimAdm.objects.filter(updateclass4=class1,updateyear4=year[0:4],updatedivision4=div,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentsrollno.html',{"students":students})




# for Secondary Roll No
def admissionsec_rollno(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['secclass_rollno'])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    secData = SecondAdm.objects.get(pk=studid[x])
                    print(studid[x])
                    if class1 == 5:
                        secData.updaterollno5=x+1
                        secData.rollno=x+1
                    elif class1 == 6:
                        secData.updaterollno6=x+1
                        secData.rollno=x+1
                    elif class1 == 7:
                        secData.updaterollno7=x+1
                        secData.rollno=x+1
                    elif class1 == 8:
                        secData.updaterollno8=x+1
                        secData.rollno=x+1
                    elif class1 == 9:
                        secData.updaterollno9=x+1
                        secData.rollno=x+1
                    elif class1 == 10:
                        secData.updaterollno10=x+1
                        secData.rollno=x+1
                    secData.save()
                messages.success(request,'Roll No Assigned Sucessfully!')
                return redirect('admissionsec_rollno')
            except:
                messages.error(request,"Invalid header found in Roll No form... Try again")
                return redirect('admissionsec_rollno')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" Secondary Roll No Assign",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/secondaryrollno.html',context) 
    else:
        return redirect('login')


# for Secondary Roll No 
def load_secstudentsrollno(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 5:
        students = SecondAdm.objects.filter(updateclass5=class1,updateyear5=year[0:4],updatedivision5=div,updateclass6=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 6:
        students = SecondAdm.objects.filter(updateclass6=class1,updateyear6=year[0:4],updatedivision6=div,updateclass7=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 7:
        students = SecondAdm.objects.filter(updateclass7=class1,updateyear7=year[0:4],updatedivision7=div,updateclass8=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 8:
        students = SecondAdm.objects.filter(updateclass8=class1,updateyear8=year[0:4],updatedivision8=div,updateclass9=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 9:
        students = SecondAdm.objects.filter(updateclass9=class1,updateyear9=year[0:4],updatedivision9=div,updateclass10=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 10:
        students = SecondAdm.objects.filter(updateclass10=class1,updateyear10=year[0:4],updatedivision10=div,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/studentsrollno.html',{"students":students})




# for College Roll No
def admissioncol_rollno(request):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['colclass_rollno'])
                studid=request.POST['studid'].split(",")
                for x in range(0,len(studid)):
                    if  CollegeAdm.objects.filter(prn=studid[x]).exists():
                        colData = CollegeAdm.objects.get(prn=studid[x])
                        print(studid[x])
                        if class1 == 11:
                            colData.updaterollno11=x+1
                            colData.rollno=x+1
                        elif class1 == 12:
                            colData.updaterollno12=x+1
                            colData.rollno=x+1
                        colData.save()
                    elif ATKT11Adm.objects.filter(prn=studid[x]).exists():
                        atktData = ATKT11Adm.objects.get(prn=studid[x])
                        atktData.rollno=x+1
                        atktData.save()
                messages.success(request,'Roll No Assigned Sucessfully!')
                return redirect('admissioncol_rollno')
            except:
                messages.error(request,"Invalid header found in Roll No form... Try again")
                return redirect('admissioncol_rollno')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":" College Roll No Assign",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/collegerollno.html',context) 
    else:
        return redirect('login')


# for College Roll No 
def load_colstudentsrollno(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    stream = request.GET.get('stream')
    dData = Division.objects.get(division=div)
    atktstudents=""
    if class1 == 11:
        atktstudents = ATKT11Adm.objects.filter(adm_class=class1,admyear=year[0:4],admission_faculty=stream,division=dData,lcgenerated=0)  
        students = CollegeAdm.objects.filter(updateclass11=class1,updateyear11=year[0:4],updatedivision11=div,updatestream11=stream,updateclass12=None,lcgenerated=0,terminatebyprincipal=0)
    elif class1 == 12:
        students = CollegeAdm.objects.filter(updateclass12=class1,updateyear12=year[0:4],updatedivision12=div,updatestream12=stream,lcgenerated=0,terminatebyprincipal=0)
    print(students)
    print(atktstudents)
    return render(request,'schoolviews/academics/studentsclg.html',{"students":students,"atktstudents":atktstudents})



# for College Repeater Views
def admissioncol_repeaterview(request,user_id):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        if request.method == 'POST':
            try:
                colData = CollegeAdm.objects.get(pk=user_id)
                colData.updateyearrep1=request.POST['updateyearrep1']
                colData.updateclassrep1=request.POST['updateclassrep1']
                colData.updatestreamrep1=request.POST['updatestreamrep1']
                colData.updatedivisionrep1=request.POST['updatedivisionrep1']
                colData.updaterollnorep1=request.POST['updaterollnorep1']
                colData.updateyearrep2=request.POST['updateyearrep2']
                colData.updateclassrep2=request.POST['updateclassrep2']
                colData.updatestreamrep2=request.POST['updatestreamrep2']
                colData.updatedivisionrep2=request.POST['updatedivisionrep2']
                colData.updaterollnorep2=request.POST['updaterollnorep2']
                colData.updateyearrep3=request.POST['updateyearrep3']
                colData.updateclassrep3=request.POST['updateclassrep3']
                colData.updatestreamrep3=request.POST['updatestreamrep3']
                colData.updatedivisionrep3=request.POST['updatedivisionrep3']
                colData.updaterollnorep3=request.POST['updaterollnorep3']
                colData.save()
                messages.success(request,'Repeater Field Added Sucessfully!')
                return redirect('academic_colAcademiclist')
            except:
                messages.error(request,"Invalid header found in Repeater form... Try again")
                return redirect('academic_colAcademiclist')
    else:
        return redirect('login')




# for primary Student Terminate
def admission_priterminate(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['priterclass'])
                studid = int(request.POST['terminatestud'])
                treason = request.POST['treason']
                tdate = request.POST['tdate']
                print(tdate)
                priData = PrimAdm.objects.get(pk=studid)
                priData.terminatebyteacher=True
                priData.treason=treason
                priData.tclass=str(class1)
                priData.tdate=tdate
                priData.save()
                messages.success(request,'Student Terminated Sucessfully!')
                return redirect('admission_priterminate')
            except:
                messages.error(request,"Invalid header found in Student Terminate form... Try again")
                return redirect('admission_priterminate')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":"Primary Student Terminate",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/primaryterminate.html',context) 
    else:
        return redirect('login')


# for primary Student Terminate 
def load_priterminate(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 1:
        students = PrimAdm.objects.filter(updateclass1=class1,updateyear1=year[0:4],updatedivision1=div,updateclass2=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 2:
        students = PrimAdm.objects.filter(updateclass2=class1,updateyear2=year[0:4],updatedivision2=div,updateclass3=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 3:
        students = PrimAdm.objects.filter(updateclass3=class1,updateyear3=year[0:4],updatedivision3=div,updateclass4=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 4:
        students = PrimAdm.objects.filter(updateclass4=class1,updateyear4=year[0:4],updatedivision4=div,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/terminatestudent.html',{"students":students})



# for Secondary Student Terminate
def admission_secterminate(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['secterclass'])
                studid = int(request.POST['terminatestud'])
                treason = request.POST['treason']
                tdate = request.POST['tdate']
                print(tdate)
                secData = SecondAdm.objects.get(pk=studid)
                secData.terminatebyteacher=True
                secData.treason=treason
                secData.tclass=str(class1)
                secData.tdate=tdate
                secData.save()
                messages.success(request,'Student Terminated Sucessfully!')
                return redirect('admission_secterminate')
            except:
                messages.error(request,"Invalid header found in Student Terminate form... Try again")
                return redirect('admission_secterminate')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":"Secondary Student Terminate",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/secondaryterminate.html',context) 
    else:
        return redirect('login')


# for Secondary Student Terminate 
def load_secterminate(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    if class1 == 5:
        students = SecondAdm.objects.filter(updateclass5=class1,updateyear5=year[0:4],updatedivision5=div,updateclass6=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 6:
        students = SecondAdm.objects.filter(updateclass6=class1,updateyear6=year[0:4],updatedivision6=div,updateclass7=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 7:
        students = SecondAdm.objects.filter(updateclass7=class1,updateyear7=year[0:4],updatedivision7=div,updateclass8=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 8:
        students = SecondAdm.objects.filter(updateclass8=class1,updateyear8=year[0:4],updatedivision8=div,updateclass9=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 9:
        students = SecondAdm.objects.filter(updateclass9=class1,updateyear9=year[0:4],updatedivision9=div,updateclass10=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 10:
        students = SecondAdm.objects.filter(updateclass10=class1,updateyear10=year[0:4],updatedivision10=div,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/terminatestudent.html',{"students":students})



# for College Student Terminate
def admission_colterminate(request):
    if request.session.has_key('username'):
        lname=request.user.last_name 
        fname=request.user.first_name
        divData = Division.objects.all()
        yearData = Year.objects.all()
        if request.method == 'POST':
            try:
                class1 = int(request.POST['colterclass'])
                stream = request.POST['colterstream']
                studid = int(request.POST['terminatestud'])
                treason = request.POST['treason']
                tdate = request.POST['tdate']
                print(tdate)
                colData = CollegeAdm.objects.get(pk=studid)
                colData.terminatebyteacher=True
                colData.treason=treason
                colData.tclass=str(class1)
                colData.tstream=stream
                colData.tdate=tdate
                colData.save()
                messages.success(request,'Student Terminated Sucessfully!')
                return redirect('admission_colterminate')
            except:
                messages.error(request,"Invalid header found in Student Terminate form... Try again")
                return redirect('admission_colterminate')
        else:
            pass
        context = {
            'sname':sname,
            'lname':lname,
            'page_title':" Academics /",
            'fname':fname,
            "divData":divData,
            "yearData":yearData,
            "page_path":"College Student Terminate",
            "menu_icon":"nav-icon fas fa-university",
            }    
        return render(request,'schoolviews/academics/collegeterminate.html',context) 
    else:
        return redirect('login')


# for College Student Terminate 
def load_colterminate(request):
    class1 = int(request.GET.get('class1'))
    year = request.GET.get('year')
    div = request.GET.get('div')
    stream = request.GET.get('stream')
    if class1 == 11:
        students = CollegeAdm.objects.filter(updateclass11=class1,updateyear11=year[0:4],updatedivision11=div,updatestream11=stream,updateclass12=None,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    elif class1 == 12:
        students = CollegeAdm.objects.filter(updateclass12=class1,updateyear12=year[0:4],updatedivision12=div,updatestream12=stream,lcgenerated=0,terminatebyteacher=0,terminatebyprincipal=0)
    print(students)
    return render(request,'schoolviews/academics/terminatestudent.html',{"students":students})




# for Secondary Repeater Views
def admissionsec_repeaterview(request,user_id):
    if request.session.has_key('username'):
        lname=request.user.last_name
        fname=request.user.first_name
        if request.method == 'POST':
            try:
                secData = SecondAdm.objects.get(pk=user_id)
                secData.repyear1=request.POST['repyear1']
                secData.repclass1=request.POST['repclass1']
                secData.repdivision1=request.POST['repdivision1']
                secData.reprollno1=request.POST['reprollno1']
                secData.repyear2=request.POST['repyear2']
                secData.repclass2=request.POST['repclass2']
                secData.repdivision2=request.POST['repdivision2']
                secData.reprollno2=request.POST['reprollno2']
                secData.repyear3=request.POST['repyear3']
                secData.repclass3=request.POST['repclass3']
                secData.repdivision3=request.POST['repdivision3']
                secData.reprollno3=request.POST['reprollno3']
                secData.save()
                messages.success(request,'Repeater Field Added Sucessfully!')
                return redirect('academic_secAcademiclist')
            except:
                messages.error(request,"Invalid header found in Repeater form... Try again")
                return redirect('academic_secAcademiclist')
    else:
        return redirect('login')