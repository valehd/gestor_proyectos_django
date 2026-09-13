# Gestor de Proyectos y Tareas - Django

## Descripción

Aplicación web desarrollada con Django para gestionar proyectos y tareas de manera organizada.

El sistema permite a los usuarios registrarse, iniciar sesión y administrar sus propios proyectos y las tareas asociadas a cada uno. Además, incorpora autenticación, autorización, validación de formularios, panel de administración de Django y pruebas unitarias.

El proyecto aplica conceptos fundamentales del framework Django, incluyendo modelos, vistas basadas en clases, formularios, templates, relaciones entre modelos, autenticación y pruebas automatizadas.

## Funcionalidades

### Gestión de usuarios

* Registro de nuevos usuarios.
* Inicio de sesión.
* Cierre de sesión.
* Redirección después del inicio y cierre de sesión.
* Restricción de acceso a usuarios no autenticados.
* Protección de los datos de cada usuario.

### Gestión de proyectos

Los usuarios autenticados pueden:

* Crear proyectos.
* Visualizar sus proyectos.
* Consultar el detalle de un proyecto.
* Editar proyectos.
* Eliminar proyectos.

Cada proyecto pertenece a un usuario específico.

### Gestión de tareas

Cada proyecto puede contener múltiples tareas.

Los usuarios pueden:

* Crear tareas.
* Visualizar tareas asociadas a un proyecto.
* Editar tareas.
* Eliminar tareas.
* Cambiar el estado de una tarea.

Estados disponibles:

* Pendiente
* En proceso
* Finalizada

## Tecnologías utilizadas

* Python
* Django 6.1.1
* SQLite
* HTML5
* CSS3
* Django Templates
* Django ORM
* Django Authentication
* Django Admin
* Django Test Framework

## Estructura del proyecto

```text
gestor_proyectos_django/
│
├── manage.py
├── README.md
├── .gitignore
│
├── gestor_tareas/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tareas/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   └── templates/
│       ├── base.html
│       │
│       ├── registration/
│       │   ├── login.html
│       │   └── registro.html
│       │
│       └── tareas/
│           ├── proyecto_list.html
│           ├── proyecto_detail.html
│           ├── proyecto_form.html
│           ├── proyecto_confirm_delete.html
│           ├── tarea_form.html
│           └── tarea_confirm_delete.html
│
└── static/
    └── css/
        └── styles.css
```

## Modelos

### Proyecto

El modelo `Proyecto` representa un proyecto perteneciente a un usuario.

Sus principales campos son:

* `usuario`: usuario propietario del proyecto.
* `nombre`: nombre del proyecto.
* `descripcion`: descripción del proyecto.
* `fecha_creacion`: fecha de creación.

Un usuario puede tener múltiples proyectos.

### Tarea

El modelo `Tarea` representa una tarea asociada a un proyecto.

Sus principales campos son:

* `proyecto`: proyecto al que pertenece.
* `titulo`: título de la tarea.
* `descripcion`: descripción.
* `estado`: estado actual de la tarea.
* `fecha_creacion`: fecha de creación.

Un proyecto puede tener múltiples tareas.

## Formularios

La aplicación utiliza formularios de Django para validar y procesar los datos ingresados por los usuarios.

Se utilizan:

* `UserCreationForm` para el registro de usuarios.
* `ModelForm` para la creación y edición de proyectos.
* `ModelForm` para la creación y edición de tareas.

Los formularios realizan validaciones antes de guardar información en la base de datos.

## Seguridad y autenticación

La aplicación utiliza el sistema de autenticación incorporado en Django.

Se implementan:

* `django.contrib.auth`
* `LoginRequiredMixin`
* Middleware de autenticación.
* Protección CSRF mediante `{% csrf_token %}`.
* Restricción de acceso a proyectos pertenecientes a otros usuarios.
* Validación de formularios antes de guardar información.

Los usuarios solamente pueden administrar sus propios proyectos y las tareas asociadas a ellos.

## Panel de administración

Django Admin se encuentra habilitado para facilitar la administración de la información.

Los modelos `Proyecto` y `Tarea` se encuentran registrados en el administrador.

Además, se incorporaron configuraciones para facilitar la gestión mediante:

* Visualización de campos relevantes.
* Búsqueda de proyectos y tareas.
* Filtros por estado de las tareas.
* Gestión de tareas directamente desde un proyecto mediante `TabularInline`.

El panel administrativo se encuentra disponible en:

```text
/admin/
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/valehd/gestor_proyectos_django.git
```

Ingresar al proyecto:

```bash
cd gestor_proyectos_django
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

En macOS o Linux:

```bash
source .venv/bin/activate
```

### 4. Instalar Django

```bash
pip install django
```

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

## Uso de la aplicación

### Registro

Los nuevos usuarios pueden registrarse desde:

```text
/registro/
```

### Inicio de sesión

El inicio de sesión se encuentra disponible en:

```text
/accounts/login/
```

### Gestión de proyectos

Después de iniciar sesión, el usuario puede acceder a sus proyectos desde la página principal.

Desde allí puede:

* Crear un proyecto.
* Ver el detalle.
* Editar.
* Eliminar.
* Agregar tareas.

### Cierre de sesión

El usuario puede cerrar sesión desde la opción **Salir** disponible en la navegación.

## Pruebas

El proyecto incluye pruebas unitarias para comprobar el funcionamiento de los modelos y las vistas principales.

Para ejecutar las pruebas:

```bash
python manage.py test
```

Actualmente se incluyen **10 pruebas automatizadas**.

Las pruebas verifican, entre otros aspectos:

* Creación de proyectos.
* Creación de tareas.
* Relaciones entre usuarios, proyectos y tareas.
* Acceso restringido a usuarios autenticados.
* Visualización de proyectos propios.
* Creación de proyectos.
* Creación de tareas.
* Restricción de acceso a proyectos pertenecientes a otros usuarios.

Resultado actual:

```text
Ran 10 tests in 22.270s

OK
```

## Arquitectura general

El proyecto utiliza la arquitectura basada en el patrón **MVT (Model-View-Template)** de Django.

### Model

Los modelos `Proyecto` y `Tarea` representan la información almacenada en la base de datos.

### View

Las vistas basadas en clases gestionan las solicitudes HTTP y las operaciones CRUD.

Se utilizan vistas genéricas de Django como:

* `ListView`
* `DetailView`
* `CreateView`
* `UpdateView`
* `DeleteView`

### Template

Los templates HTML presentan la información al usuario.

Se utiliza herencia de templates mediante:

```text
base.html
```

Esto permite reutilizar la estructura común de navegación y contenido de la aplicación.

## CRUD implementado

| Recurso  | Crear | Consultar | Editar | Eliminar |
| -------- | :---: | :-------: | :----: | :------: |
| Proyecto |   ✅   |     ✅     |    ✅   |     ✅    |
| Tarea    |   ✅   |     ✅     |    ✅   |     ✅    |

## Base de datos

El proyecto utiliza **SQLite** como base de datos durante el desarrollo.

La configuración se encuentra en:

```text
gestor_tareas/settings.py
```

Las migraciones de Django permiten crear y actualizar la estructura de la base de datos.

Para generar nuevas migraciones:

```bash
python manage.py makemigrations
```

Para aplicarlas:

```bash
python manage.py migrate
```

## Comandos principales

Activar entorno virtual:

```bash
source .venv/bin/activate
```

Ejecutar servidor:

```bash
python manage.py runserver
```

Verificar configuración:

```bash
python manage.py check
```

Ejecutar pruebas:

```bash
python manage.py test
```

Crear migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear usuario administrador:

```bash
python manage.py createsuperuser
```

## Autor

Proyecto desarrollado como parte del aprendizaje y evaluación de desarrollo web utilizando el framework Django.
