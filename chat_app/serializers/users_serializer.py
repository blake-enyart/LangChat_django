from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password', 'password_confirmation')
        }
        data['password'] = validated_data['password']
        return self.Meta.model.objects.create_user(**data)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'password', 'password_confirmation',
            'first_name', 'last_name', 'country_of_origin', "is_active",
            "email"
        )
        read_only_fields = ('id',)
