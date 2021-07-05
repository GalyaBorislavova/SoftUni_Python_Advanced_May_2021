class EmailValidationError(Exception):
    pass


class NameTooShortError(EmailValidationError):
    pass


class MustContainAtSymbolError(EmailValidationError):
    pass


class InvalidDomainError(EmailValidationError):
    pass


class TooManyAtSymbolsError(EmailValidationError):
    pass
