from faker import Faker

fake = Faker('es.Es')
lUsuarios = []

for i in range(1, 16):
    lUsuarios.append({
        "codigo" : i,
        "nome" : fake.name(),
        "direccion" : fake.address(),
        "correo electronico" : fake.email(),
        "telefono" : fake.phone_number(),
    })

print("Los participantes son: ")
for usr in lUsuarios:
    print(usr)

