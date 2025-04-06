from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}, 
        help_text="Password must be at least 8 characters long."
    )
    confirm_password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}, 
        help_text="Confirm the password."
    )
    first_name = serializers.CharField(
        required=True,
        help_text="Your name is required."
    )
    email = serializers.EmailField(
        required = True,
        style = {'input_type' : 'email'},
        help_text = 'Email is required'
    )
    
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'username',
            'email',
            'password',
            'confirm_password',
            'last_name',
            'role',
            'phone_number',
            'newsletter_subscription',
        ]

    def validate_phone_number(self, value):
        """Validate phone number format. """
        if value and not value.isdigit():
            raise serializers.ValidationError('Phone number must contain only digits')
        return value
    
    def validate(self, data):
        """Validate passwords match and enforce additional rules."""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if len(data['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})
        return data

    def create(self, validated_data):
        """Remove confirm_password and create the user with hashed password."""
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.setdefault('role', 'member'),
            phone_number=validated_data.get('phone_number', ''),
            newsletter_subscription=validated_data.get('newsletter_subscription', False),
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'profile_picture',
            'newsletter_subscription',
            'role'
        ]
        read_only_fields = ['username', 'email', 'role']
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    