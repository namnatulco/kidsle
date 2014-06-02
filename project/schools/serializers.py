from rest_framework import serializers

from .models import School

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'post_code', 'street', 'town', 'school_type', 'latitude', 'longitude')