def get_field_value(field):
    """
    Returns a method that fetches the value of the specified field from the user's profile.

    Args:
        field (str): The name of the field to retrieve from the user's profile.

    Returns:
        callable: A method that takes a user instance and returns the value of the
        specified field from their profile. If the value is None, it returns 'Not provided'.
    """

    def method(self, user):
        value = getattr(user.profile, field)
        return value if value else "Not provided"

    return method
