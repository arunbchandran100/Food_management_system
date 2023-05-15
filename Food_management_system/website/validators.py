import re
#from django.core.exceptions import ValidationError

"""
def validate_mobile_number(value):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    if not pattern.match(value):
        raise ValidationError("Invalid mobile number format")
    

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must contain at least one special character.")
    def get_help_text(self):
        return "Password must be at least 6 characters long, contain at least one number, and one special character."

def validate_password(password):
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must contain at least one special character.")
def get_help_text(self):
        return "Password must be at least 6 characters long, contain at least one number, and one special character."
#test"""  
"""
class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 special character: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
"""   