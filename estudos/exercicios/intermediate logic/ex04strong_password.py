def is_passwd_strong(passwd: str) -> bool:
    if len(passwd) < 8:
        return False
    
    special_chars = '!@#$%&'
    has_upper, has_lower, has_number, has_special = False, False, False, False

    for ch in passwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_number = True
        elif ch in special_chars:
            has_special = True
    
    return has_upper and has_lower and has_number and has_special

print(is_passwd_strong("Teste"))
print(is_passwd_strong("Testando"))
print(is_passwd_strong("Testando123"))
print(is_passwd_strong("Testando123!"))
print(is_passwd_strong("TESTANDO123!"))