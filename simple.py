import jinja2

model = 'Olá {{ nome }}, seja bem vindo. Seu email é {{email}} e seu estado {{estado}}'

emails = [
    ['fernando@mail.com', 'Fernando Santos', 'Rio Grande do Sul'],
    ['maria@mail.com', 'Maria Clara', 'São Paulo'],
    ['c.pinha@mail.com', 'Cezar Pinha', 'Rio de Janeiro']
]

template = jinja2.Template(model)

for email in emails:
    print(template.render(nome=email[1], email=email[0], estado=email[2]))