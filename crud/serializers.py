from rest_framework import serializers
from .models import User

# Custom Validators
def name_must_start_with_a(value):
  if value[0].lower() != 'a':
    raise serializers.ValidationError("Name must start with a")

class UserSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=70, validators=[name_must_start_with_a])
  class Meta:
    model = User
    fields = '__all__'
  
  # Field level validation
  def validate_name(self, value):
    if value == 'admin':
      raise serializers.ValidationError("Name can't be admin")
    return value

  # Field level validation
  def validate_roll(self, value):
    if value >= 200:
      raise serializers.ValidationError("Roll number can't be greater than 200")
    return value

  # Object level validation
  def validate(self, data):
    name = data.get('name')
    city = data.get('city')

    if city.lower() != 'lahore':
      raise serializers.ValidationError('City must be lahore')
    return data

