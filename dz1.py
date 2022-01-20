import re


email = 'dima_protasevich@mail.ru'
def email_parse(email):
    patern = re.compile(r'(?P<username>\w+)@(?P<domain>[a-zA-Z_]+?\.[a-zA-Z]{2,6})')
    result = re.search(patern, email)
    return result.groupdict()


print(email_parse('kochirishka@list.ru'))
print(email_parse('someone@geekbrains.ru'))
