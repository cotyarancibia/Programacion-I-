# Programacion-I-
Sistema de Adopción de mascotas 

Este proyecto consiste en el desarrollo de una API para la gestión de adopción de mascotas. 
Los usuarios pueden publicar mascotas en adopción y otros usuarios pueden solicitar adoptarlas. 

El sistema está compuesto por las siguientes entidades: 
- Usuario
- Mascota
- Solicitud

Relaciones: 
- Un usuario puede publicar múltiples mascotas (1:N)
- Un usuario puede realizar múltiples solicitudes de adopción (1:N)
- Una mascota puede tener múltiples solicitudes (1:N)

Funcionalidades: 
- Crear usuarios
- Publicar mascotas 
- Solicitar adopción
- Listar solicitudes

Objetivo: 
El objetivo de este proyecto es desarrollar un backend utilizando Django que permita gestionar el proceso de adopción de mascotas. 
Se busca implentar una API que facilite la creación de usuarios, la publicación de mascotas en adopción y la gestión de solicitudes por parte de otros usuarios. 

Requisitos Previos: 
Para poder ejecutar este proyecto es necesario contar con: 
- Python instalado 
- Git instalado  

Instalación: 
1. Clonar el repositorio: 
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
2. Crear entorno virtual: 
python -m venv venv 
3. Activar entorno virtual: 
venv\Scripts\Activate.ps1
4. Instalar dependencias: 
pip install -r requirements.txt
5. Aplicar migraciones: 
python manage.py migrate 

Ejecutar el proyecto: 
Para iniciar el servidor de desarrollo ejecutar: 
python manage.py runserver
Acceso: 
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/
