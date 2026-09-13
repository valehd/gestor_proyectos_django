
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Proyecto, Tarea


class ProyectoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="valentina",
            password="Test1234!"
        )

    def test_crear_proyecto(self):
        proyecto = Proyecto.objects.create(
            usuario=self.usuario,
            nombre="Proyecto de prueba",
            descripcion="Descripción del proyecto"
        )

        self.assertEqual(proyecto.nombre, "Proyecto de prueba")
        self.assertEqual(proyecto.usuario, self.usuario)
        self.assertEqual(str(proyecto), "Proyecto de prueba")

    def test_usuario_puede_tener_varios_proyectos(self):
        Proyecto.objects.create(
            usuario=self.usuario,
            nombre="Proyecto 1"
        )
        Proyecto.objects.create(
            usuario=self.usuario,
            nombre="Proyecto 2"
        )

        self.assertEqual(self.usuario.proyectos.count(), 2)


class TareaModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="valentina",
            password="Test1234!"
        )

        self.proyecto = Proyecto.objects.create(
            usuario=self.usuario,
            nombre="Proyecto de prueba"
        )

    def test_crear_tarea(self):
        tarea = Tarea.objects.create(
            proyecto=self.proyecto,
            titulo="Tarea de prueba",
            descripcion="Descripción de la tarea"
        )

        self.assertEqual(tarea.titulo, "Tarea de prueba")
        self.assertEqual(tarea.proyecto, self.proyecto)
        self.assertEqual(tarea.estado, "pendiente")
        self.assertEqual(str(tarea), "Tarea de prueba")

    def test_proyecto_puede_tener_varias_tareas(self):
        Tarea.objects.create(
            proyecto=self.proyecto,
            titulo="Tarea 1"
        )
        Tarea.objects.create(
            proyecto=self.proyecto,
            titulo="Tarea 2"
        )

        self.assertEqual(self.proyecto.tareas.count(), 2)


class ProyectoViewsTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="valentina",
            password="Test1234!"
        )

        self.otro_usuario = User.objects.create_user(
            username="otro_usuario",
            password="Test1234!"
        )

        self.proyecto = Proyecto.objects.create(
            usuario=self.usuario,
            nombre="Mi proyecto"
        )

        self.otro_proyecto = Proyecto.objects.create(
            usuario=self.otro_usuario,
            nombre="Proyecto de otro usuario"
        )

    def test_usuario_no_autenticado_es_redirigido_al_login(self):
        response = self.client.get(reverse("proyecto_list"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('proyecto_list')}"
        )

    def test_usuario_autenticado_ve_solo_sus_proyectos(self):
        self.client.login(
            username="valentina",
            password="Test1234!"
        )

        response = self.client.get(reverse("proyecto_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mi proyecto")
        self.assertNotContains(response, "Proyecto de otro usuario")

    def test_usuario_puede_crear_un_proyecto(self):
        self.client.login(
            username="valentina",
            password="Test1234!"
        )

        response = self.client.post(
            reverse("proyecto_create"),
            {
                "nombre": "Nuevo proyecto",
                "descripcion": "Proyecto creado mediante test"
            }
        )

        self.assertEqual(response.status_code, 302)

        proyecto = Proyecto.objects.get(nombre="Nuevo proyecto")

        self.assertEqual(proyecto.usuario, self.usuario)

    def test_usuario_no_puede_acceder_al_proyecto_de_otro_usuario(self):
        self.client.login(
            username="valentina",
            password="Test1234!"
        )

        response = self.client.get(
            reverse(
                "proyecto_detail",
                kwargs={"pk": self.otro_proyecto.pk}
            )
        )

        self.assertEqual(response.status_code, 404)


class TareaViewsTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="valentina",
            password="Test1234!"
        )

        self.otro_usuario = User.objects.create_user(
            username="otro_usuario",
            password="Test1234!"
        )

        self.proyecto = Proyecto.objects.create(
            usuario=self.usuario,
            nombre="Mi proyecto"
        )

        self.otro_proyecto = Proyecto.objects.create(
            usuario=self.otro_usuario,
            nombre="Proyecto de otro usuario"
        )

    def test_usuario_puede_crear_una_tarea(self):
        self.client.login(
            username="valentina",
            password="Test1234!"
        )

        response = self.client.post(
            reverse(
                "tarea_create",
                kwargs={"proyecto_id": self.proyecto.pk}
            ),
            {
                "titulo": "Nueva tarea",
                "descripcion": "Tarea creada mediante test",
                "estado": "pendiente"
            }
        )

        self.assertEqual(response.status_code, 302)

        tarea = Tarea.objects.get(titulo="Nueva tarea")

        self.assertEqual(tarea.proyecto, self.proyecto)
        self.assertEqual(tarea.proyecto.usuario, self.usuario)

    def test_usuario_no_puede_crear_tarea_en_proyecto_ajeno(self):
        self.client.login(
            username="valentina",
            password="Test1234!"
        )

        response = self.client.post(
            reverse(
                "tarea_create",
                kwargs={"proyecto_id": self.otro_proyecto.pk}
            ),
            {
                "titulo": "Tarea no autorizada",
                "descripcion": "No debería crearse",
                "estado": "pendiente"
            }
        )

        self.assertEqual(response.status_code, 404)

        self.assertFalse(
            Tarea.objects.filter(
                titulo="Tarea no autorizada"
            ).exists()
        )