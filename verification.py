def Name_verication(name):
    return name.replace(" ", "").isalpha()


def Document_type_verification(document_type):
    return document_type in ('Passport', 'Identity Card')


def Document_verification(doc, document_type):
    if document_type == 'Passport':
        return doc.isalnum() and len(doc) == 8

    elif document_type == 'Identity Card':
        return doc.isalnum() and len(doc) == 14
    return False


def whitespace_verification(info):
    return bool(info.strip())


def alpha_verification(info):
    return info.replace(" ", "")
