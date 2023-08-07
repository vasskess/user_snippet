from django.contrib.auth import get_user_model

User = get_user_model()


def get_profile_model():
    """
    Returns the Profile model associated with the custom User model.

    This function dynamically retrieves the Profile model from the custom User model
    by inspecting the ForeignKey or OneToOneField named 'profile'. It helps avoid
    hard-coding the Profile model's name and promotes maintainability.

    Returns:
        Model: The Profile model associated with the custom User model.
    """
    return User._meta.get_field("profile").remote_field.model