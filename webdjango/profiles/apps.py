from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
 characters = set(new_password1)

        lower = any(letter.islower() for letter in characters)
        upper = any(letter.isupper() for letter in characters)
        digit = any(letter.isdigit() for letter in characters)

        if not upper:
            raise forms.ValidationError('Your password must use of '
                                        'both uppercase and lowercase letters')

        if not lower:
            raise forms.ValidationError('Your password must use of '
                                        'both uppercase and lowercase letters')

        if not digit:
            raise forms.ValidationError('Your password must include '
                                        'of one or more numerical digits')

        special_characters = ["@", "#", "$"]
        check = False
        for character in special_characters:
            if character in new_password1:
                check = True

        if not check:
            raise forms.ValidationError('Your password must include of '
                                        'special characters, such as @, #, $')

        first_name = self.user.profile.first_name.lower()
        last_name = self.user.profile.last_name.lower()

        if first_name in new_password1.lower():
            raise forms.ValidationError('Your password cannot be too '
                                        'similar to your other personal '
                                        'information')

        if last_name in new_password1.lower():
            raise forms.ValidationError('Your password cannot be too '
                                        'similar to your other personal '
                                        'information')

        return new_password1
