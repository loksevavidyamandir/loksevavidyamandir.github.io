from django.db import models
from django.contrib.auth.models import Group,User
from schSetup.setupModels.setup_cast_models import CastCategory,Cast,Religion,SubCast
from schSetup.setupModels.setup_models import  Division,MTongue,OtherSch


# Primary Admission Model
class PrimAdm(models.Model):
    stud_id=models.CharField(max_length=200,null=True)
    prn=models.CharField(max_length=50,unique=True)
    lname=models.CharField(max_length=20)   
    fname=models.CharField(max_length=20)    
    faname=models.CharField(max_length=20) 
    moname=models.CharField(max_length=20) 
    mrname=models.CharField(max_length=50,null=True)  
    aadhar=models.CharField(max_length=13)
    saral_id=models.CharField(max_length=25,null=True) 
    nationality=models.CharField(max_length=15) 
    tongue=models.ForeignKey(MTongue,on_delete=models.SET_NULL,null=True)
    religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True)
    cast=models.ForeignKey(Cast,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(CastCategory,on_delete=models.SET_NULL,null=True)
    subcast=models.ForeignKey(SubCast,on_delete=models.SET_NULL,null=True)
    minority=models.CharField(max_length=4)
    pob=models.CharField(max_length=100,null=True)  
    dob=models.CharField(max_length=10)
    last_school=models.ForeignKey(OtherSch,on_delete=models.SET_NULL,null=True) 
    last_class=models.CharField(max_length=10,null=True)
    admdate=models.CharField(max_length=10)
    admyear=models.CharField(max_length=4)
    adm_class=models.CharField(max_length=2)
    prevlcsrno=models.CharField(max_length=10,null=True)
    prevprn=models.CharField(max_length=50,null=True)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL,null=True) 
    rollno=models.CharField(max_length=10,null=True) 
    lateadm=models.CharField(max_length=4)  
    admtype=models.CharField(max_length=10) 
    hostel=models.CharField(max_length=4)
    #Health details
    sex=models.CharField(max_length=6)
    pwd=models.CharField(max_length=4)
    bgroup=models.CharField(max_length=4,null=True)  
    #Parents details
    fa_mob=models.CharField(max_length=10,null=True)
    mo_mob=models.CharField(max_length=10,null=True)
    fa_occu=models.CharField(max_length=15,null=True) 
    mo_occu=models.CharField(max_length=15,null=True) 
    fam_income=models.CharField(max_length=10,null=True)
    bpl=models.CharField(max_length=4)
    #Guardian
    gis=models.CharField(max_length=10) 
    ganame=models.CharField(max_length=50,null=True) 
    ga_mob=models.CharField(max_length=10,null=True)
    ga_occu=models.CharField(max_length=15,null=True) 
    gaddress=models.CharField(max_length=100,null=True) 
    ga_relation=models.CharField(max_length=15,null=True) 
    #Address
    areaType=models.CharField(max_length=6)
    email=models.CharField(max_length=50) 
    caddress=models.CharField(max_length=100) 
    ca_is_pa_addr=models.CharField(max_length=3,null=True)  
    paddress=models.CharField(max_length=100) 
    #Bank Details
    baccount=models.CharField(max_length=20,null=True)
    bankname=models.CharField(max_length=20,null=True) 
    ifsc=models.CharField(max_length=15,null=True) 
    branch=models.CharField(max_length=20,null=True) 
    micr=models.CharField(max_length=20,null=True) 
    #Documents
    marks_img=models.ImageField(upload_to="imgs/primadm/marksheet",null=True)
    prv_lc_img=models.ImageField(upload_to="imgs/primadm/lc",null=True)
    addhar_img=models.ImageField(upload_to="imgs/primadm/aadhar",null=True)
    cast_img=models.ImageField(upload_to="imgs/primadm/cast",null=True)
    castvald_img=models.ImageField(upload_to="imgs/primadm/castval",null=True)
    nationality_img=models.ImageField(upload_to="imgs/primadm/nationality",null=True)
    noncrimy_img=models.ImageField(upload_to="imgs/primadm/noncrimy",null=True)
    std_img=models.ImageField(upload_to="imgs/primadm/stdimg",null=True)
    birth_img=models.ImageField(upload_to="imgs/primadm/birth",null=True)  
    note=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #Academics
    #for 1 std
    updateclass1 = models.CharField(max_length=10,null=True)
    updateyear1 = models.CharField(max_length=10,null=True)
    updatedivision1 = models.CharField(max_length=10,null=True)
    updaterollno1 = models.CharField(max_length=10,null=True)
    #for 2 std
    updateclass2 = models.CharField(max_length=10,null=True)
    updateyear2 = models.CharField(max_length=10,null=True)
    updatedivision2 = models.CharField(max_length=10,null=True)
    updaterollno2 = models.CharField(max_length=10,null=True)
    #for 3 std
    updateclass3 = models.CharField(max_length=10,null=True)
    updateyear3 = models.CharField(max_length=10,null=True)
    updatedivision3 = models.CharField(max_length=10,null=True)
    updaterollno3 = models.CharField(max_length=10,null=True)
    #for 4 std
    updateclass4 = models.CharField(max_length=10,null=True)
    updateyear4 = models.CharField(max_length=10,null=True)
    updatedivision4 = models.CharField(max_length=10,null=True)
    updaterollno4 = models.CharField(max_length=10,null=True)
    #Terminate
    terminatebyteacher=models.BooleanField(null=True,default=0)
    terminatebyprincipal=models.BooleanField(null=True,default=0)
    treason = models.CharField(max_length=200,null=True)   
    tclass = models.CharField(max_length=10,null=True)   
    tdate = models.CharField(max_length=10,null=True)
    tyear = models.CharField(max_length=10,null=True)
    #LC Gen
    lcgenerated=models.BooleanField(null=True,default=0)
    lcsrno=models.CharField(max_length=10,null=True)
    lcprogress=models.CharField(max_length=200,null=True)
    lcconduct=models.CharField(max_length=200,null=True)
    lcdateofleaving=models.CharField(max_length=10,null=True)
    lcyearofleaving=models.CharField(max_length=5,null=True)
    lcreason=models.CharField(max_length=200,null=True)
    lcremarks=models.CharField(max_length=200,null=True)
    lcstudyinginclass=models.CharField(max_length=200,null=True)
    lctongue=models.CharField(max_length=100,null=True)
    lcreligion=models.CharField(max_length=100,null=True)
    lccaste=models.CharField(max_length=100,null=True)
    lcadmdate=models.CharField(max_length=10,null=True)
    lcdobinwords=models.CharField(max_length=100,null=True)
    lcissuedate=models.CharField(max_length=10,null=True)
    lcdob=models.CharField(max_length=10,null=True)
    lcprintcount=models.CharField(max_length=2,null=True,default=0)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"primadmi"



# Secondary Admission Model
class SecondAdm(models.Model):
    stud_id=models.CharField(max_length=200,null=True)
    prn=models.CharField(max_length=50,unique=True)
    lname=models.CharField(max_length=20)   
    fname=models.CharField(max_length=20)    
    faname=models.CharField(max_length=20) 
    moname=models.CharField(max_length=20) 
    mrname=models.CharField(max_length=50,null=True)  
    aadhar=models.CharField(max_length=13)
    saral_id=models.CharField(max_length=25,null=True) 
    nationality=models.CharField(max_length=15) 
    tongue=models.ForeignKey(MTongue,on_delete=models.SET_NULL,null=True)
    religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True)
    cast=models.ForeignKey(Cast,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(CastCategory,on_delete=models.SET_NULL,null=True)
    subcast=models.ForeignKey(SubCast,on_delete=models.SET_NULL,null=True)
    minority=models.CharField(max_length=4)
    pob=models.CharField(max_length=100,null=True)  
    dob=models.CharField(max_length=10)
    last_school=models.ForeignKey(OtherSch,on_delete=models.SET_NULL,null=True) 
    last_class=models.CharField(max_length=10,null=True)
    prevlcsrno=models.CharField(max_length=10,null=True)
    prevprn=models.CharField(max_length=50,null=True)
    admdate=models.CharField(max_length=10)
    admyear=models.CharField(max_length=4)
    adm_class=models.CharField(max_length=2)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL,null=True) 
    rollno=models.CharField(max_length=10,null=True) 
    lateadm=models.CharField(max_length=4)  
    admtype=models.CharField(max_length=10) 
    hostel=models.CharField(max_length=4)
    #Health details
    sex=models.CharField(max_length=6)
    pwd=models.CharField(max_length=4)
    bgroup=models.CharField(max_length=4,null=True)  
    #Parents details
    fa_mob=models.CharField(max_length=10,null=True)
    mo_mob=models.CharField(max_length=10,null=True)
    fa_occu=models.CharField(max_length=15,null=True) 
    mo_occu=models.CharField(max_length=15,null=True) 
    fam_income=models.CharField(max_length=10,null=True)
    bpl=models.CharField(max_length=4) 
    #Guardian
    gis=models.CharField(max_length=10) 
    ganame=models.CharField(max_length=50,null=True)
    ga_mob=models.CharField(max_length=10,null=True)
    ga_occu=models.CharField(max_length=15,null=True) 
    gaddress=models.CharField(max_length=100,null=True) 
    ga_relation=models.CharField(max_length=15,null=True) 
    #Address
    areaType=models.CharField(max_length=6)
    email=models.CharField(max_length=50) 
    caddress=models.CharField(max_length=100) 
    ca_is_pa_addr=models.CharField(max_length=3,null=True)  
    paddress=models.CharField(max_length=100) 
    #Bank Details
    baccount=models.CharField(max_length=20,null=True)
    bankname=models.CharField(max_length=20,null=True) 
    ifsc=models.CharField(max_length=15,null=True) 
    branch=models.CharField(max_length=20,null=True) 
    micr=models.CharField(max_length=20,null=True) 
    #Documents
    marks_img=models.ImageField(upload_to="imgs/secondadm/marksheet",null=True)
    prv_lc_img=models.ImageField(upload_to="imgs/secondadm/lc",null=True)
    addhar_img=models.ImageField(upload_to="imgs/secondadm/aadhar",null=True)
    cast_img=models.ImageField(upload_to="imgs/secondadm/cast",null=True)
    castvald_img=models.ImageField(upload_to="imgs/secondadm/castval",null=True)
    nationality_img=models.ImageField(upload_to="imgs/secondadm/nationality",null=True)
    noncrimy_img=models.ImageField(upload_to="imgs/secondadm/noncrimy",null=True)
    std_img=models.ImageField(upload_to="imgs/secondadm/stdimg",null=True)
    birth_img=models.ImageField(upload_to="imgs/secondadm/birth",null=True)
    note=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #for 5 std
    #Academics
    updateclass5 = models.CharField(max_length=10,null=True)   
    updateyear5 = models.CharField(max_length=10,null=True)   
    updatedivision5 = models.CharField(max_length=10,null=True)   
    updaterollno5 = models.CharField(max_length=10,null=True) 
    #for 6 std
    updateclass6 = models.CharField(max_length=10,null=True)   
    updateyear6 = models.CharField(max_length=10,null=True)   
    updatedivision6 = models.CharField(max_length=10,null=True)   
    updaterollno6 = models.CharField(max_length=10,null=True) 
    #for 7 std
    updateclass7 = models.CharField(max_length=10,null=True)   
    updateyear7 = models.CharField(max_length=10,null=True)   
    updatedivision7 = models.CharField(max_length=10,null=True)   
    updaterollno7 = models.CharField(max_length=10,null=True) 
    #for 8 std
    updateclass8 = models.CharField(max_length=10,null=True)   
    updateyear8 = models.CharField(max_length=10,null=True)   
    updatedivision8 = models.CharField(max_length=10,null=True)   
    updaterollno8 = models.CharField(max_length=10,null=True) 

    #for 8th pass certificate
    sec8pass = models.BooleanField(null=True,default=0)
    sec8passdate = models.CharField(null=True,max_length=10)
    sec8passyear = models.CharField(null=True,max_length=4)
    #for 9 std
    updateclass9 = models.CharField(max_length=10,null=True)   
    updateyear9 = models.CharField(max_length=10,null=True)   
    updatedivision9 = models.CharField(max_length=10,null=True)   
    updaterollno9 = models.CharField(max_length=10,null=True) 
    #for 10 std
    updateclass10 = models.CharField(max_length=10,null=True)
    updateyear10 = models.CharField(max_length=10,null=True)
    updatedivision10 = models.CharField(max_length=10,null=True)
    updaterollno10 = models.CharField(max_length=10,null=True)
    #for repeater 1
    repclass1 = models.CharField(max_length=10,null=True)
    repyear1 = models.CharField(max_length=10,null=True)
    repdivision1 = models.CharField(max_length=10,null=True)
    reprollno1 = models.CharField(max_length=10,null=True)
    #for repeater 2
    repclass2 = models.CharField(max_length=10,null=True)
    repyear2 = models.CharField(max_length=10,null=True)
    repdivision2 = models.CharField(max_length=10,null=True)
    reprollno2 = models.CharField(max_length=10,null=True)
    #for repeater 3
    repclass3 = models.CharField(max_length=10,null=True)
    repyear3 = models.CharField(max_length=10,null=True)
    repdivision3 = models.CharField(max_length=10,null=True)
    reprollno3 = models.CharField(max_length=10,null=True)

    #Terminate
    terminatebyteacher=models.BooleanField(null=True,default=0) 
    terminatebyprincipal=models.BooleanField(null=True,default=0)
    treason = models.CharField(max_length=200,null=True)   
    tclass = models.CharField(max_length=10,null=True)   
    tdate = models.CharField(max_length=10,null=True)
    tyear = models.CharField(max_length=10,null=True)
    #LC Gen
    lcgenerated=models.BooleanField(null=True,default=0)
    lcsrno=models.CharField(max_length=10,null=True)
    lcprogress=models.CharField(max_length=200,null=True)
    lcconduct=models.CharField(max_length=200,null=True)
    lcdateofleaving=models.CharField(max_length=10,null=True)
    lcyearofleaving=models.CharField(max_length=5,null=True)
    lcreason=models.CharField(max_length=200,null=True)
    lcremarks=models.CharField(max_length=200,null=True)
    lctongue=models.CharField(max_length=100,null=True)
    lcreligion=models.CharField(max_length=100,null=True)
    lccaste=models.CharField(max_length=100,null=True)
    lcstudyinginclass=models.CharField(max_length=200,null=True)
    lcdob=models.CharField(max_length=10,null=True)
    lcdobinwords=models.CharField(max_length=100,null=True)
    lcadmdate=models.CharField(max_length=10,null=True)
    lcissuedate=models.CharField(max_length=10,null=True)
    lcprintcount=models.CharField(max_length=2,null=True,default=0)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"secondadmi"




# College Admission Model
class CollegeAdm(models.Model):
    stud_id=models.CharField(max_length=200,null=True)
    prn=models.CharField(max_length=50,unique=True)
    lname=models.CharField(max_length=20)   
    fname=models.CharField(max_length=20)    
    faname=models.CharField(max_length=20) 
    moname=models.CharField(max_length=20) 
    mrname=models.CharField(max_length=50,null=True)  
    aadhar=models.CharField(max_length=13)
    saral_id=models.CharField(max_length=25,null=True) 
    nationality=models.CharField(max_length=15) 
    tongue=models.ForeignKey(MTongue,on_delete=models.SET_NULL,null=True)
    religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True)
    cast=models.ForeignKey(Cast,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(CastCategory,on_delete=models.SET_NULL,null=True)
    subcast=models.ForeignKey(SubCast,on_delete=models.SET_NULL,null=True)
    minority=models.CharField(max_length=4)
    pob=models.CharField(max_length=100,null=True)  
    dob=models.CharField(max_length=10)
    last_school=models.ForeignKey(OtherSch,on_delete=models.SET_NULL,null=True) 
    last_class=models.CharField(max_length=10,null=True)
    prevlcsrno=models.CharField(max_length=10,null=True)
    prevprn=models.CharField(max_length=50,null=True)
    admdate=models.CharField(max_length=10)
    admyear=models.CharField(max_length=4)
    adm_class=models.CharField(max_length=2)
    admission_faculty=models.CharField(max_length=20)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL,null=True)
    rollno=models.CharField(max_length=10,null=True) 
    lateadm=models.CharField(max_length=4)  
    admtype=models.CharField(max_length=10) 
    hostel=models.CharField(max_length=4)
    #Health details
    sex=models.CharField(max_length=6)
    pwd=models.CharField(max_length=4)
    bgroup=models.CharField(max_length=4,null=True)  
    #Parents details
    fa_mob=models.CharField(max_length=10,null=True)
    mo_mob=models.CharField(max_length=10,null=True)
    fa_occu=models.CharField(max_length=15,null=True) 
    mo_occu=models.CharField(max_length=15,null=True) 
    fam_income=models.CharField(max_length=10,null=True)
    bpl=models.CharField(max_length=4) 
    #Guardian
    gis=models.CharField(max_length=10) 
    ganame=models.CharField(max_length=50,null=True) 
    ga_mob=models.CharField(max_length=10,null=True)
    ga_occu=models.CharField(max_length=15,null=True) 
    gaddress=models.CharField(max_length=100,null=True) 
    ga_relation=models.CharField(max_length=15,null=True) 
    #Address
    areaType=models.CharField(max_length=6)
    email=models.CharField(max_length=50) 
    caddress=models.CharField(max_length=100) 
    ca_is_pa_addr=models.CharField(max_length=3,null=True)  
    paddress=models.CharField(max_length=100) 
    #Bank Details
    baccount=models.CharField(max_length=20,null=True)
    bankname=models.CharField(max_length=20,null=True) 
    ifsc=models.CharField(max_length=15,null=True) 
    branch=models.CharField(max_length=20,null=True) 
    micr=models.CharField(max_length=20,null=True) 
    #Documents
    marks_img=models.ImageField(upload_to="imgs/collegeadm/marksheet",null=True)
    prv_lc_img=models.ImageField(upload_to="imgs/collegeadm/lc",null=True)
    addhar_img=models.ImageField(upload_to="imgs/collegeadm/aadhar",null=True)
    cast_img=models.ImageField(upload_to="imgs/collegeadm/cast",null=True)
    castvald_img=models.ImageField(upload_to="imgs/collegeadm/castval",null=True)
    nationality_img=models.ImageField(upload_to="imgs/collegeadm/nationality",null=True)
    noncrimy_img=models.ImageField(upload_to="imgs/collegeadm/noncrimy",null=True)
    std_img=models.ImageField(upload_to="imgs/collegeadm/stdimg",null=True)
    birth_img=models.ImageField(upload_to="imgs/collegeadm/birth",null=True)
    note=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #Academics
    #for 11 std
    updateclass11 = models.CharField(max_length=10,null=True)   
    updateyear11 = models.CharField(max_length=10,null=True)   
    updatedivision11 = models.CharField(max_length=10,null=True)   
    updaterollno11 = models.CharField(max_length=10,null=True) 
    updatestream11 =  models.CharField(max_length=20,null=True) 
    #for 12 std
    updateclass12 = models.CharField(max_length=10,null=True)   
    updateyear12 = models.CharField(max_length=10,null=True)   
    updatedivision12 = models.CharField(max_length=10,null=True)   
    updaterollno12 = models.CharField(max_length=10,null=True)   
    updatestream12 =  models.CharField(max_length=20,null=True) 
    #for repeater 
    updateclassrep1 = models.CharField(max_length=10,null=True)   
    updateyearrep1 = models.CharField(max_length=10,null=True)   
    updatedivisionrep1 = models.CharField(max_length=10,null=True)   
    updaterollnorep1 = models.CharField(max_length=10,null=True)   
    updatestreamrep1 =  models.CharField(max_length=20,null=True) 
    #for repeater
    updateclassrep2 = models.CharField(max_length=10,null=True)   
    updateyearrep2 = models.CharField(max_length=10,null=True)   
    updatedivisionrep2 = models.CharField(max_length=10,null=True)   
    updaterollnorep2 = models.CharField(max_length=10,null=True)   
    updatestreamrep2 =  models.CharField(max_length=20,null=True) 
    #for repeater
    updateclassrep3 = models.CharField(max_length=10,null=True)   
    updateyearrep3 = models.CharField(max_length=10,null=True)   
    updatedivisionrep3 = models.CharField(max_length=10,null=True)   
    updaterollnorep3 = models.CharField(max_length=10,null=True)   
    updatestreamrep3 =  models.CharField(max_length=20,null=True)     
    #Terminate
    terminatebyteacher=models.BooleanField(null=True,default=0) 
    terminatebyprincipal=models.BooleanField(null=True,default=0)
    treason = models.CharField(max_length=200,null=True)
    tclass = models.CharField(max_length=10,null=True)
    tstream = models.CharField(max_length=10,null=True)
    tdate = models.CharField(max_length=10,null=True)
    tyear = models.CharField(max_length=10,null=True)
    #LC Gen
    lcgenerated=models.BooleanField(null=True,default=0)
    lcsrno=models.CharField(max_length=10,null=True)
    lcprogress=models.CharField(max_length=200,null=True)
    lcconduct=models.CharField(max_length=200,null=True)
    lcdateofleaving=models.CharField(max_length=10,null=True)
    lcyearofleaving=models.CharField(max_length=5,null=True)
    lcreason=models.CharField(max_length=200,null=True)
    lcremarks=models.CharField(max_length=200,null=True)
    lctongue=models.CharField(max_length=100,null=True)
    lcreligion=models.CharField(max_length=100,null=True)
    lccaste=models.CharField(max_length=100,null=True)
    lcstudyinginclass=models.CharField(max_length=200,null=True)
    lcdob=models.CharField(max_length=10,null=True)
    lcdobinwords=models.CharField(max_length=100,null=True)
    lcissuedate=models.CharField(max_length=10,null=True)
    lcadmdate=models.CharField(max_length=10,null=True)
    lcprintcount=models.CharField(max_length=2,null=True,default=0)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"collegeadmi"



# 11-ATKT Admission Model
class ATKT11Adm(models.Model):
    stud_id=models.CharField(max_length=200,null=True)
    prn=models.CharField(max_length=50,unique=True)
    lname=models.CharField(max_length=20)   
    fname=models.CharField(max_length=20)    
    faname=models.CharField(max_length=20) 
    moname=models.CharField(max_length=20) 
    mrname=models.CharField(max_length=50,null=True)  
    aadhar=models.CharField(max_length=13)
    saral_id=models.CharField(max_length=25,null=True) 
    nationality=models.CharField(max_length=15) 
    tongue=models.ForeignKey(MTongue,on_delete=models.SET_NULL,null=True)
    religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True)
    cast=models.ForeignKey(Cast,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(CastCategory,on_delete=models.SET_NULL,null=True)
    subcast=models.ForeignKey(SubCast,on_delete=models.SET_NULL,null=True)
    minority=models.CharField(max_length=4)
    pob=models.CharField(max_length=100,null=True)  
    dob=models.CharField(max_length=10)
    last_school=models.ForeignKey(OtherSch,on_delete=models.SET_NULL,null=True) 
    last_class=models.CharField(max_length=10,null=True)
    prevlcsrno=models.CharField(max_length=10,null=True)
    prevprn=models.CharField(max_length=50,null=True)
    admdate=models.CharField(max_length=10)
    admyear=models.CharField(max_length=4)
    adm_class=models.CharField(max_length=2)
    admission_faculty=models.CharField(max_length=20)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL,null=True)
    rollno=models.CharField(max_length=10,null=True) 
    lateadm=models.CharField(max_length=4)  
    admtype=models.CharField(max_length=10) 
    hostel=models.CharField(max_length=4)
    #Health details
    sex=models.CharField(max_length=6)
    pwd=models.CharField(max_length=4)
    bgroup=models.CharField(max_length=4,null=True)  
    #Parents details
    fa_mob=models.CharField(max_length=10,null=True)
    mo_mob=models.CharField(max_length=10,null=True)
    fa_occu=models.CharField(max_length=15,null=True) 
    mo_occu=models.CharField(max_length=15,null=True) 
    fam_income=models.CharField(max_length=10,null=True)
    bpl=models.CharField(max_length=4) 
    #Guardian
    gis=models.CharField(max_length=10) 
    ganame=models.CharField(max_length=50,null=True) 
    ga_mob=models.CharField(max_length=10,null=True)
    ga_occu=models.CharField(max_length=15,null=True) 
    gaddress=models.CharField(max_length=100,null=True) 
    ga_relation=models.CharField(max_length=15,null=True) 
    #Address
    areaType=models.CharField(max_length=6)
    email=models.CharField(max_length=50) 
    caddress=models.CharField(max_length=100) 
    ca_is_pa_addr=models.CharField(max_length=3,null=True)  
    paddress=models.CharField(max_length=100) 
    #Bank Details
    baccount=models.CharField(max_length=20,null=True)
    bankname=models.CharField(max_length=20,null=True) 
    ifsc=models.CharField(max_length=15,null=True) 
    branch=models.CharField(max_length=20,null=True) 
    micr=models.CharField(max_length=20,null=True) 
    #Documents
    marks_img=models.ImageField(upload_to="imgs/atkt11adm/marksheet",null=True)
    prv_lc_img=models.ImageField(upload_to="imgs/atkt11adm/lc",null=True)
    addhar_img=models.ImageField(upload_to="imgs/atkt11adm/aadhar",null=True)
    cast_img=models.ImageField(upload_to="imgs/atkt11adm/cast",null=True)
    castvald_img=models.ImageField(upload_to="imgs/atkt11adm/castval",null=True)
    nationality_img=models.ImageField(upload_to="imgs/atkt11adm/nationality",null=True)
    noncrimy_img=models.ImageField(upload_to="imgs/atkt11adm/noncrimy",null=True)
    std_img=models.ImageField(upload_to="imgs/atkt11adm/stdimg",null=True)
    birth_img=models.ImageField(upload_to="imgs/atkt11adm/birth",null=True)
    bonafide_img=models.ImageField(upload_to="imgs/atkt11adm/bonafide",null=True)
    note=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)   
    #Bonafide Details
    bonaissuedate=models.CharField(max_length=10,null=True)
    bonasrno=models.CharField(max_length=20,null=True)
    #LC Gen
    lcgenerated=models.BooleanField(null=True,default=0)
    lcsrno=models.CharField(max_length=10,null=True)
    lcprogress=models.CharField(max_length=200,null=True)
    lcconduct=models.CharField(max_length=200,null=True)
    lcdateofleaving=models.CharField(max_length=10,null=True)
    lcyearofleaving=models.CharField(max_length=5,null=True)
    lcreason=models.CharField(max_length=200,null=True)
    lcremarks=models.CharField(max_length=200,null=True)
    lctongue=models.CharField(max_length=100,null=True)
    lcreligion=models.CharField(max_length=100,null=True)
    lccaste=models.CharField(max_length=100,null=True)
    lcstudyinginclass=models.CharField(max_length=200,null=True)
    lcdob=models.CharField(max_length=10,null=True)
    lcdobinwords=models.CharField(max_length=100,null=True)
    lcissuedate=models.CharField(max_length=10,null=True)
    lcadmdate=models.CharField(max_length=10,null=True)
    lcprintcount=models.CharField(max_length=2,null=True,default=0)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"atkt11admi"




# From1710 Admission Model
class Form1710Adm(models.Model):
    stud_id=models.CharField(max_length=200,null=True)
    prn=models.CharField(max_length=50,unique=True)
    lname=models.CharField(max_length=20)   
    fname=models.CharField(max_length=20)    
    faname=models.CharField(max_length=20) 
    moname=models.CharField(max_length=20) 
    mrname=models.CharField(max_length=50,null=True)  
    aadhar=models.CharField(max_length=13)
    saral_id=models.CharField(max_length=25,null=True)
    nationality=models.CharField(max_length=15) 
    tongue=models.ForeignKey(MTongue,on_delete=models.SET_NULL,null=True)
    religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True)
    cast=models.ForeignKey(Cast,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(CastCategory,on_delete=models.SET_NULL,null=True)
    subcast=models.ForeignKey(SubCast,on_delete=models.SET_NULL,null=True)
    minority=models.CharField(max_length=4)
    pob=models.CharField(max_length=100,null=True)  
    dob=models.CharField(max_length=10)
    last_school=models.ForeignKey(OtherSch,on_delete=models.SET_NULL,null=True)
    last_class=models.CharField(max_length=10,null=True)
    prevlcsrno=models.CharField(max_length=10,null=True)
    prevprn=models.CharField(max_length=50,null=True)
    admdate=models.CharField(max_length=10)
    admyear=models.CharField(max_length=4)
    adm_class=models.CharField(max_length=2)
    rollno=models.CharField(max_length=10,null=True)
    lateadm=models.CharField(max_length=4)  
    admtype=models.CharField(max_length=10) 
    hostel=models.CharField(max_length=4)
    #Health details
    sex=models.CharField(max_length=6)
    pwd=models.CharField(max_length=4)
    bgroup=models.CharField(max_length=4,null=True)  
    #Parents details
    fa_mob=models.CharField(max_length=10,null=True)
    mo_mob=models.CharField(max_length=10,null=True)
    fa_occu=models.CharField(max_length=15,null=True) 
    mo_occu=models.CharField(max_length=15,null=True) 
    fam_income=models.CharField(max_length=10,null=True)
    bpl=models.CharField(max_length=4) 
    #Guardian
    gis=models.CharField(max_length=10) 
    ganame=models.CharField(max_length=50,null=True) 
    ga_mob=models.CharField(max_length=10,null=True)
    ga_occu=models.CharField(max_length=15,null=True) 
    gaddress=models.CharField(max_length=100,null=True) 
    ga_relation=models.CharField(max_length=15,null=True) 
    #Address
    areaType=models.CharField(max_length=6)
    email=models.CharField(max_length=50) 
    caddress=models.CharField(max_length=100) 
    ca_is_pa_addr=models.CharField(max_length=3,null=True)  
    paddress=models.CharField(max_length=100) 
    #Bank Details
    baccount=models.CharField(max_length=20,null=True)
    bankname=models.CharField(max_length=20,null=True) 
    ifsc=models.CharField(max_length=15,null=True) 
    branch=models.CharField(max_length=20,null=True) 
    micr=models.CharField(max_length=20,null=True) 
    #Documents
    marks_img=models.ImageField(upload_to="imgs/form1710adm/marksheet",null=True)
    prv_lc_img=models.ImageField(upload_to="imgs/form1710adm/lc",null=True)
    addhar_img=models.ImageField(upload_to="imgs/form1710adm/aadhar",null=True)
    cast_img=models.ImageField(upload_to="imgs/form1710adm/cast",null=True)
    castvald_img=models.ImageField(upload_to="imgs/form1710adm/castval",null=True)
    nationality_img=models.ImageField(upload_to="imgs/form1710adm/nationality",null=True)
    noncrimy_img=models.ImageField(upload_to="imgs/form1710adm/noncrimy",null=True)
    std_img=models.ImageField(upload_to="imgs/form1710adm/stdimg",null=True)
    birth_img=models.ImageField(upload_to="imgs/form1710adm/birth",null=True)
    note=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #LC GEn
    lcgenerated=models.BooleanField(null=True,default=0) 
    lcsrno=models.CharField(max_length=10,null=True)
    seatnoandyear=models.CharField(max_length=5,null=True)
    lcdateofpassing=models.CharField(max_length=10,null=True)
    lcyearofpassing=models.CharField(max_length=5,null=True)
    lctongue=models.CharField(max_length=100,null=True)
    lcreligion=models.CharField(max_length=100,null=True)
    lccaste=models.CharField(max_length=100,null=True)
    lcadmdate=models.CharField(max_length=10,null=True)
    lcdob=models.CharField(max_length=10,null=True)
    lcdobinwords=models.CharField(max_length=100,null=True)
    lcissuedate=models.CharField(max_length=10,null=True)
    lcprintcount=models.CharField(max_length=2,null=True,default=0)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"form1710admi"




# Form1712 Admission Model
class Form1712Adm(models.Model):
    stud_id=models.CharField(max_length=200,null=True)
    prn=models.CharField(max_length=50,unique=True)
    lname=models.CharField(max_length=20)   
    fname=models.CharField(max_length=20)    
    faname=models.CharField(max_length=20) 
    moname=models.CharField(max_length=20) 
    mrname=models.CharField(max_length=50,null=True)  
    aadhar=models.CharField(max_length=13)
    saral_id=models.CharField(max_length=25,null=True) 
    nationality=models.CharField(max_length=15) 
    tongue=models.ForeignKey(MTongue,on_delete=models.SET_NULL,null=True)
    religion=models.ForeignKey(Religion,on_delete=models.SET_NULL,null=True)
    cast=models.ForeignKey(Cast,on_delete=models.SET_NULL,null=True)
    # category=models.ForeignKey(CastCategory,on_delete=models.SET_NULL,null=True)
    subcast=models.ForeignKey(SubCast,on_delete=models.SET_NULL,null=True)
    minority=models.CharField(max_length=4)
    pob=models.CharField(max_length=100,null=True)
    dob=models.CharField(max_length=10)
    last_school=models.ForeignKey(OtherSch,on_delete=models.SET_NULL,null=True) 
    last_class=models.CharField(max_length=10,null=True)
    prevlcsrno=models.CharField(max_length=10,null=True)
    prevprn=models.CharField(max_length=50,null=True)
    admdate=models.CharField(max_length=10)
    admyear=models.CharField(max_length=4)
    adm_class=models.CharField(max_length=2)
    admission_faculty=models.CharField(max_length=20) 
    rollno=models.CharField(max_length=10,null=True) 
    lateadm=models.CharField(max_length=4)  
    admtype=models.CharField(max_length=10) 
    hostel=models.CharField(max_length=4)
    #Health details
    sex=models.CharField(max_length=6)
    pwd=models.CharField(max_length=4)
    bgroup=models.CharField(max_length=4,null=True)  
    #Parents details
    fa_mob=models.CharField(max_length=10,null=True)
    mo_mob=models.CharField(max_length=10,null=True)
    fa_occu=models.CharField(max_length=15,null=True) 
    mo_occu=models.CharField(max_length=15,null=True) 
    fam_income=models.CharField(max_length=10,null=True)
    bpl=models.CharField(max_length=4) 
    #Guardian
    gis=models.CharField(max_length=10) 
    ganame=models.CharField(max_length=50,null=True) 
    ga_mob=models.CharField(max_length=10,null=True)
    ga_occu=models.CharField(max_length=15,null=True) 
    gaddress=models.CharField(max_length=100,null=True) 
    ga_relation=models.CharField(max_length=15,null=True) 
    #Address
    areaType=models.CharField(max_length=6)
    email=models.CharField(max_length=50) 
    caddress=models.CharField(max_length=100) 
    ca_is_pa_addr=models.CharField(max_length=3,null=True)  
    paddress=models.CharField(max_length=100) 
    #Bank Details
    baccount=models.CharField(max_length=20,null=True)
    bankname=models.CharField(max_length=20,null=True) 
    ifsc=models.CharField(max_length=15,null=True) 
    branch=models.CharField(max_length=20,null=True) 
    micr=models.CharField(max_length=20,null=True) 
    #Documents
    marks_img=models.ImageField(upload_to="imgs/form1712adm/marksheet",null=True)
    prv_lc_img=models.ImageField(upload_to="imgs/form1712adm/lc",null=True)
    addhar_img=models.ImageField(upload_to="imgs/form1712adm/aadhar",null=True)
    cast_img=models.ImageField(upload_to="imgs/form1712adm/cast",null=True)
    castvald_img=models.ImageField(upload_to="imgs/form1712adm/castval",null=True)
    nationality_img=models.ImageField(upload_to="imgs/form1712adm/nationality",null=True)
    noncrimy_img=models.ImageField(upload_to="imgs/form1712adm/noncrimy",null=True)
    std_img=models.ImageField(upload_to="imgs/form1712adm/stdimg",null=True)
    birth_img=models.ImageField(upload_to="imgs/form1712adm/birth",null=True)
    note=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #LC Gen
    lcgenerated=models.BooleanField(null=True,default=0) 
    lcsrno=models.CharField(max_length=10,null=True)
    seatnoandyear=models.CharField(max_length=5,null=True)
    lcdateofpassing=models.CharField(max_length=10,null=True)
    lcyearofpassing=models.CharField(max_length=5,null=True)
    lctongue=models.CharField(max_length=100,null=True)
    lcreligion=models.CharField(max_length=100,null=True)
    lccaste=models.CharField(max_length=100,null=True)
    lcadmdate=models.CharField(max_length=10,null=True)
    lcdob=models.CharField(max_length=10,null=True)
    lcdobinwords=models.CharField(max_length=100,null=True)
    lcissuedate=models.CharField(max_length=10,null=True)
    lcprintcount=models.CharField(max_length=2,null=True,default=0)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"form1712admi"



# # Primary LC SrNo Model
class PriLCSrNo(models.Model):
    srnotext=models.CharField(max_length=2,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"prilcserialno"



# Secondary LC SrNo Model
class SecLCSrNo(models.Model):
    srnotext=models.CharField(max_length=2,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"seclcserialno"



# College LC SrNo Model
class ColLCSrNo(models.Model):
    srnotext=models.CharField(max_length=2,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"collcserialno"



# ATKT11 LC SrNo Model
class ATKT11LCSrNo(models.Model):
    srnotext=models.CharField(max_length=2,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"collcserialno"



# Form1710 LC SrNo Model
class Form1710LCSrNo(models.Model):
    srnotext=models.CharField(max_length=2,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"form1710lcserialno"



# Form1712 LC SrNo Model
class Form1712LCSrNo(models.Model):
    srnotext=models.CharField(max_length=2,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"form1712lcserialno"


    