import random
from faker import Faker
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from apps.patient.models import Paciente, TipoTelefono, Domicilio, Referente, Parroquia, Telefono, TratamientoMedico, PacienteTratamientoMedico, Medicacion

class Command(BaseCommand):
    help = 'Genera datos aleatorios para tus modelos en Django'

    def handle(self, *args, **kwargs):
        fake = Faker(['es_ES'])

        # Crear tipos de teléfono ficticios
        tipos_telefono = [fake.unique.word() for _ in range(5)]
        for tipo in tipos_telefono:
            TipoTelefono.objects.create(descripcion=tipo)

        # Crear datos aleatorios para Parroquias
        for _ in range(20):  # Ajusta el número según tus necesidades
            parroquia = Parroquia(
                nombre=fake.unique.word(),
            )
            parroquia.save()

            # Asignar domicilio aleatorio
            domicilio = Domicilio(
                calle=fake.street_name(),
                numero=fake.building_number(),
                piso=fake.secondary_address(),
                entre_calles=fake.secondary_address(),
                codigo_postal=fake.random_element(elements=('1406', '2000', '5000')),
                localidad=fake.city(),
            )
            domicilio.save()
            parroquia.domicilio = domicilio

            parroquia.save()

        # Crear datos aleatorios para Pacientes
        for _ in range(100):  # Ajusta el número según tus necesidades
            paciente = Paciente(
                dni=fake.unique.random_int(min=10000000, max=99999999),
                apellidos=fake.last_name(),
                nombres=fake.first_name(),
                fecha_de_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=90),
                casilla_de_mail=fake.email(),
                condicion_de_solicitud=random.choice(['ACTIVO', 'INACTIVO']),
                estado_de_monotributo=random.choice(['ALTA', 'EN_TRAMITE']),
                dni_foto_frente='dni/foto_frente.jpg',
                dni_foto_dorso='dni/foto_dorso.jpg',
                certificado_de_matrimonio='certificados/certificado_matrimonio.pdf',
                certificado_de_convivencia='certificados/certificado_convivencia.pdf',
                certificado_de_tutela='certificados/certificado_tutela.pdf',
                credencial=fake.unique.random_int(min=100000, max=999999),
                credencial_entregada=fake.boolean(chance_of_getting_true=50),
                observaciones=fake.text(),
            )
            paciente.save()

            # Asignar domicilio aleatorio
            domicilio = Domicilio(
                calle=fake.street_name(),
                numero=fake.building_number(),
                piso=fake.secondary_address(),
                entre_calles=fake.secondary_address(),
                codigo_postal=fake.random_element(elements=('1406', '2000', '5000')),
                localidad=fake.city(),
            )
            domicilio.save()
            paciente.domicilio = domicilio

            # Asignar referente aleatorio
            if random.choice([True, False]):
                referente = Referente(
                    apellidos=fake.last_name(),
                    nombres=fake.first_name(),
                    fecha_de_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=90),
                )
                referente.save()
                paciente.referente_parroquial = referente

            # Asignar teléfonos aleatorios
            for _ in range(random.randint(1, 3)):
                tipo_telefono = random.choice(TipoTelefono.objects.all())
                telefono = Telefono(
                    paciente=paciente,
                    tipo=tipo_telefono,
                    numero_de_telefono=fake.phone_number(),
                )
                telefono.save()

            paciente.save()

            # Asignar tratamientos médicos aleatorios
            for _ in range(random.randint(1, 3)):
                descripcion = fake.unique.word()
                while TratamientoMedico.objects.filter(descripcion=descripcion).exists():
                    descripcion = fake.unique.word()
                
                tratamiento = TratamientoMedico(
                    descripcion=descripcion,
                )
                tratamiento.save()
                fecha_desde = fake.date_of_birth(minimum_age=18, maximum_age=90)
                fecha_hasta = fecha_desde + timedelta(days=random.randint(30, 180))
                observaciones = fake.text()
                paciente_tratamiento = PacienteTratamientoMedico(
                    paciente=paciente,
                    tratamiento_medico=tratamiento,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta,
                    observaciones=observaciones,
                )
                paciente_tratamiento.save()

            # Asignar medicaciones aleatorias
            for _ in range(random.randint(1, 3)):
                medicacion = Medicacion(
                    medicamento=fake.word(),
                    dosis=fake.word(),
                    fecha_desde=fake.date_of_birth(minimum_age=18, maximum_age=90),
                    fecha_hasta=fake.date_of_birth(minimum_age=18, maximum_age=90),
                )
                medicacion.save()

        self.stdout.write(self.style.SUCCESS('Datos aleatorios creados con éxito.'))
