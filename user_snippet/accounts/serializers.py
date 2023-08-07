from rest_framework import serializers
from django.contrib.auth import get_user_model

from user_snippet.helpers.get_field_helper import get_field_value

User = get_user_model()


class AppUserSerializer(serializers.ModelSerializer):
    """
    Serializer for custom User model, including additional profile fields.

    This serializer is used to convert User model instances, along with their
    associated ProfileModel data, into JSON representations.

    Attributes:
        slug (serializers.SerializerMethodField): The method to retrieve the slug
            field value from the user's profile.
        first_name (serializers.SerializerMethodField): The method to retrieve the
            first_name field value from the user's profile.
        last_name (serializers.SerializerMethodField): The method to retrieve the
            last_name field value from the user's profile.
        date_joined (serializers.DateTimeField): The formatted date the user joined.

    Meta:
        model (User): The custom User model associated with this serializer.
        fields (list): The list of fields to include in the serialized representation.
    """

    slug = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = User
        fields = [
            "slug",
            "email",
            "first_name",
            "last_name",
            "date_joined",
        ]

    get_slug = get_field_value("slug")
    get_first_name = get_field_value("first_name")
    get_last_name = get_field_value("last_name")
