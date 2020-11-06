from django.test import TestCase
from django.contrib.auth.models import User
from mantenedor.models import regitro_cliente,nuevos_plan

class MantenedorTestCase(TestCase):
        def setUp(self):
            userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
            )

class registroClienteTestCase(TestCase):
    def setUp(self):
        regitro_cliente.objects.create(nombre='Felipe',apellidoP="Munoz")
        regitro_cliente.objects.create(nombre='Ivan',apellidoP="Figueroa")
     

    def test_campos_cliente_correctos(self):
        obj1 = regitro_cliente.objects.get(nombre='Felipe')
        obj2 = regitro_cliente.objects.get(nombre='Ivan')
        self.assertEqual(obj1.nombre,'Felipe')
        self.assertEqual(obj2.nombre,'Ivan')
        self.assertEqual(obj1.apellidoP,'Munoz')
        self.assertEqual(obj2.apellidoP,'Figueroa')

