from Validators import *

ALLOWED_DOMAINS = [".com", ".bg", ".net", ".org"]


def valid_email(email):
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain, *rest = email.split("@")

    if rest:
        raise TooManyAtSymbolsError("Email must contain only one at symbol")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if f".{domain.split('.')[-1]}" not in ALLOWED_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")

    print("Email is valid")


def main():
    while True:
        email = input()
        try:
            valid_email(email)
        except EmailValidationError as e:
            print(e)


def test():
    try:
        valid_email("petergmail.com")
    except MustContainAtSymbolError:
        pass

    try:
        valid_email("abc@gmail.com")
    except NameTooShortError:
        pass

    try:
        valid_email("peter@gmail.hotmail")
    except InvalidDomainError:
        pass

    try:
        valid_email("one@two@gmail.com")
    except TooManyAtSymbolsError:
        pass

    valid_email("peter@gmail.com")


if __name__ == "__main__":
    # test()
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye")
