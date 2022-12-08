from ejemplo.models import Familiar, Mascota, Vehiculo

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()

Mascota(apodo= "pipi", raza= 'Caniche Toy', edad=2).save()
Mascota(apodo= "lala", raza= 'Dalmata', edad=1).save()
Mascota(apodo= "toto", raza= 'Labrador', edad=3).save()
Mascota(apodo= "chiche", raza= 'Caniche', edad=5).save()

Vehiculo(marca= "Toyota", modelo= 'Etios', patente="AC 555 PC").save()
Vehiculo(marca= "Toyota", modelo= 'Hilux', patente="CC 675 VC").save()
Vehiculo(marca= "Chevrolet", modelo= 'Meriva', patente="AP 856 PP").save()

print("Se cargo con éxito")