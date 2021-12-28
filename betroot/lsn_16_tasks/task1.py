class Validator:
    def __init__(self, mail: str):

        self.validate(mail)

    @staticmethod
    def validate(arg):
        allowed_mails = ['mail.ru', 'gmail.com', 'ukr.net']
        notallowed = ['.', ',', '?', ']', '[', '{', '}', '-', '=', '+', '/']
        absolutely_not = '#'
        ban = ''
        email = arg.split('@')
        if len(email) != 2:
            raise ValueError('wrong format')
        if email[1] not in allowed_mails:
            raise ValueError('wrong format')
        if email[0][1] in notallowed or email[0][-1] in notallowed:
            raise ValueError('wrong format')
        if absolutely_not in email[0]:
            raise ValueError('wrong format')

        for char in email[0]:
            if char in notallowed:
                if ban == char:
                    raise ValueError('wrong format')
                ban = char

        print(arg.split('@'))
