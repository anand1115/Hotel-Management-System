from django import forms
from django.utils.regex_helper import Choice
import datetime

country=[('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'),
('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), 
('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'),('Bangladesh', 'Bangladesh'), 
('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), 
('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'),
('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), 
('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Costa Rica', 'Costa Rica'), 
('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ("CÃ´te d'Ivoire", "CÃ´te d'Ivoire"), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), 
('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'),
('Federated States of Micronesia', 'Federated States of Micronesia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Georgia', 'Georgia'), ('Germany', 'Germany'),
('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), 
('Hungary', 'Hungary'), ('Iceland', 'Iceland'),
('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel', 'Israel'), 
('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), 
('Kenya', 'Kenya'), ('Kingdom of the Netherlands', 'Kingdom of the Netherlands'), ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), 
('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), 
('Luxembourg', 'Luxembourg'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'),
('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), 
('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('New Zealand', 'New Zealand'),
('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Korea', 'North Korea'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'),
('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ("People's Republic of China", "People's Republic of China"), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), 
('Republic of Ireland', 'Republic of Ireland'), ('Republic of the Congo', 'Republic of the Congo'), 
('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), 
('Saint Lucia', 'Saint Lucia'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), 
('San Marino', 'San Marino'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), 
('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), 
('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), 
('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'),
('Switzerland', 'Switzerland'), ('Syria', 'Syria'),('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'),
('The Gambia', 'The Gambia'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'),
('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'),
('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')]


proofs=[
   ('Aadhar Card','Aadhar Card'),
   ('Indian Passport','Indian Passport'),
   ('Overseas Passport',"Overseas Passport"),
   ('Voter Id',"Voter id"),
   ('Pan Card','Pan Card'),
   ('Driving Licence','Driving Licence'),
   ('Ration Card','Ration Card') 
]
class BookingForm1(forms.Form):
    CheckInDate=forms.DateField(required=True)
    CheckOutDate=forms.DateField(required=True)
    CheckInTime=forms.TimeField(required=True)
    CheckOutTime=forms.TimeField(required=True)
    RoomCount=forms.IntegerField(required=True,max_value=999,min_value=0)
    GuestCount=forms.IntegerField(required=True,max_value=999,min_value=0)
    AdultCount=forms.IntegerField(required=True,max_value=999,min_value=0)
    ChildCount=forms.IntegerField(required=True,max_value=999,min_value=0)
    Country=forms.ChoiceField(required=True,choices=country)
    FirstName=forms.CharField(max_length=50,required=True)
    LastName=forms.CharField(max_length=50,required=True)
    Phonenumber=forms.IntegerField(required=True)
    City=forms.CharField(max_length=255,required=True)
    Gender=forms.ChoiceField(required=True,choices=[('Male','Male'),('Female','Female'),('Others','Others')])
    Email=forms.EmailField(required=True)
    IdentificationProof=forms.ChoiceField(required=True,choices=proofs)


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['CheckInDate'].label=""
        self.fields['CheckOutDate'].label=""
        self.fields['CheckOutTime'].label=""
        self.fields['CheckInTime'].label=""
        self.fields['RoomCount'].label=""
        self.fields['GuestCount'].label=""
        self.fields['AdultCount'].label=""
        self.fields['ChildCount'].label=""
        self.fields['Country'].label=""
        self.fields['FirstName'].label=""
        self.fields['LastName'].label=""
        self.fields['Phonenumber'].label=""
        self.fields['City'].label=""
        self.fields['Gender'].label=""
        self.fields['Email'].label=""
        self.fields['IdentificationProof'].label=""
        self.fields['CheckInDate'].widget=forms.widgets.DateInput(attrs={"type":"date","required":True,"class":"in-out","placeholder":"Date"})
        self.fields['CheckOutDate'].widget=forms.widgets.DateInput(attrs={"type":"date","required":True,"class":"in-out","placeholder":"Date"})
        self.fields['CheckInTime'].widget=forms.widgets.DateInput(attrs={"type":"time","required":True,"class":"in-out","placeholder":"Time"})
        self.fields['CheckOutTime'].widget=forms.widgets.DateInput(attrs={"type":"time","required":True,"class":"in-out","placeholder":"Time"})
        self.fields['RoomCount'].widget=forms.widgets.NumberInput(attrs={"type":"Number","required":True,"class":"error","placeholder":"00","id":"number-rooms"})
        self.fields['GuestCount'].widget=forms.widgets.NumberInput(attrs={"type":"Number","required":True,"class":"error","placeholder":"00","id":"number-guests"})
        self.fields['AdultCount'].widget=forms.widgets.NumberInput(attrs={"type":"Number","required":True,"class":"error","placeholder":"00","id":"number-adults"})
        self.fields['ChildCount'].widget=forms.widgets.NumberInput(attrs={"type":"Number","required":True,"class":"error","placeholder":"00","id":"number-children"})
        self.fields['FirstName'].widget=forms.widgets.TextInput(attrs={"type":"Text","required":True,"class":"first-name error-class","placeholder":"First Name","id":"first-name"})
        self.fields['LastName'].widget=forms.widgets.TextInput(attrs={"type":"Text","required":True,"class":"last-name error-class","placeholder":"Last Name","id":"last-name"})
        self.fields['Phonenumber'].widget=forms.widgets.NumberInput(attrs={"type":"Number","required":True,"class":"last-name error-class","placeholder":"PhoneNumber","id":"phone-number"})
        self.fields['City'].widget=forms.widgets.TextInput(attrs={"type":"Text","required":True,"class":"error-class","placeholder":"City","id":"town"})
        self.fields['City'].widget=forms.widgets.TextInput(attrs={"type":"Text","required":True,"class":"error-class","placeholder":"City","id":"town"})
        self.fields['Email'].widget=forms.widgets.EmailInput(attrs={"type":"email","required":True,"class":"error-class","placeholder":"email","id":"email-address"})

    def clean_CheckInDate(self):
        CheckInDate=self.cleaned_data['CheckInDate']
        if(CheckInDate):
            if(datetime.date.today()>CheckInDate):
                raise forms.ValidationError("Please Enter Valid Check In Date !")
        return CheckInDate
    
    def clean_CheckOutDate(self):
        CheckOutDate=self.cleaned_data['CheckOutDate']
        if(CheckOutDate):
            if(datetime.date.today()>CheckOutDate):
                raise forms.ValidationError("Please Enter Valid Check Out Date !")
        return CheckOutDate

    def clean_RoomCount(self):
        RoomCount=self.cleaned_data['RoomCount']
        if RoomCount:
            if(RoomCount<1 or RoomCount>99):
                raise forms.ValidationError("Please Enter Valid Number of Rooms !")
        return RoomCount
    
    def clean_GuestCount(self):
        GuestCount=self.cleaned_data['GuestCount']
        if GuestCount:
            if(GuestCount<0 or GuestCount>99):
                raise forms.ValidationError("Please Enter Valid Number of Guests !")
        return GuestCount
    
    def clean_AdultCount(self):
        AdultCount=self.cleaned_data['AdultCount']
        if AdultCount:
            if(AdultCount<0 or AdultCount>99):
                raise forms.ValidationError("Please Enter Valid Number of Adults !")
        return AdultCount
    
    def clean_ChildCount(self):
        ChildCount=self.cleaned_data['ChildCount']
        if ChildCount:
            if(ChildCount<0 or ChildCount>99):
                raise forms.ValidationError("Please Enter Valid Number of Children !")
        return ChildCount
    
    def clean_FirstName(self):
        FirstName=self.cleaned_data['FirstName']
        if(FirstName):
            if(len(FirstName)<3 or (not FirstName.isalpha())):
                raise forms.ValidationError("Please Provide Valid FirstName !")
        return FirstName
    
    def clean_LastName(self):
        LastName=self.cleaned_data['LastName']
        if(LastName):
            if(len(LastName)<3 or (not LastName.isalpha())):
                raise forms.ValidationError("Please Provide Valid LastName !")
        return LastName
    
    def clean_Phonenumber(self):
        PhoneNumber=self.cleaned_data['Phonenumber']
        if PhoneNumber:
            if(not str(PhoneNumber).isnumeric() or len(str(PhoneNumber))!=10):
                raise forms.ValidationError("Please Provide Valid Phonenumber !")
        return PhoneNumber
    
    def clean_City(self):
        City=self.cleaned_data['City']
        if City:
            if(len(City)<3):
                raise forms.ValidationError("Please Enter valid City !")
        return City
    

    def clean(self):
        cleaned_data=super().clean()
        checkin=datetime.datetime.combine(cleaned_data['CheckInDate'],cleaned_data['CheckInTime'])
        checkout=datetime.datetime.combine(cleaned_data['CheckOutDate'],cleaned_data['CheckOutTime'])
        if((checkout-checkin).days<1):
            raise forms.ValidationError("Please Book The Room for atleast One Day.Please change the CheckIn And CheckOut Timings.!!")
        if(cleaned_data['GuestCount']!=cleaned_data['AdultCount']+cleaned_data['ChildCount']):
            raise forms.ValidationError("Number Of Guests Not Matched with the Number Of Adults And Children")
        
    

    


