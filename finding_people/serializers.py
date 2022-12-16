from rest_framework import serializers
from .models import User, LoggedInData, AadharData, FIRData, TrainigImagesData, CascadeAndTrainerData, TrainedDataSet, TrackingUserData, AllUsersTrackingData
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','password','mobile','aadhar_number','email_otp','email_verification','mobile_otp','mobile_verification','aadhar_verification','verified_user','verified_user_id_proof']
    
    # validations
    def validate_password(self,value):
        special_char='[@_!$%^&*()<>?/\|}{~:]#'
        
        isNum = any(i.isdigit() for i in value)
        isUpper = any(i.isupper() for i in value)
        isLower = any(i.islower() for i in value)
        isSpecial = any(special_char[i] in value for i in range(len(special_char)))

        if not isNum or not isUpper or not isLower or len(value)<10 or not isSpecial:
            raise serializers.ValidationError('Please Maintain Password Criteria')
        value = make_password(value)
        return value
        
    

class LoggedInDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggedInData
        fields = ['id','username','session']
        
    def validate_password(self,value):
        special_char='[@_!$%^&*()<>?/\|}{~:]#'
        
        isNum = any(i.isdigit() for i in value)
        isUpper = any(i.isupper() for i in value)
        isLower = any(i.islower() for i in value)
        isSpecial = any(special_char[i] in value for i in range(len(special_char)))

        if not isNum or not isUpper or not isLower or len(value)<10 or not isSpecial:
            raise serializers.ValidationError('Please Maintain Password Criteria')
        return value
    
    
class AadharDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AadharData
        fields = ['id','serial','card_number','VID','profile','name','DOB', 'gender','address']
        
class FIRDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIRData
        fields = ['id','serial','fir_id','profile','name','father_name','address','phone_number','fir_type']
        
class TrainigImagesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainigImagesData
        fields = ['id','image','serial','from_database']
        
class CascadeAndTrainerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CascadeAndTrainerData
        fields = ['id','name','file_name']
        
class TrainedDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainedDataSet
        fields = ['id','serial','name','aadhar_number']
        

class TrackingUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingUserData
        fields = ['id','username','profile','name','police_station_droped','time_at_droped','date_at_droped','tracking_progress']
        

class AllUsersTrackingData(serializers.ModelSerializer):
    class Meta:
        model = AllUsersTrackingData
        fields = ['id','uid','from_database','database_serial']