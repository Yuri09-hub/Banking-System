def Name_verication(Name):
    if Name == '':
        return False
    elif not Name.isalpha():
        return False
    return True


def Document_type_verication(Document_type):
    if Document_type == 'Passport' or Document_type == 'Identity Card':
        return True
    else:
        return False
