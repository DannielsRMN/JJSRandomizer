# JJS Randomizer - Jujutsu Shenanigans

Un widget ligero desarrollado en Python para la selección aleatoria de personajes dentro de la experiencia "Jujutsu Shenanigans" en Roblox.

## 📋 Concepto del Proyecto
El proyecto implementa un sistema de recomendación aleatoria basado en el elenco de personajes de Jujutsu Shenanigans. Está diseñado para ser una herramienta rápida y visual que flote en el escritorio del jugador.

## 🎯 Finalidad
Proporcionar una herramienta útil para jugadores que necesiten una recomendación imparcial de personaje para:
* Diferentes dinámicas de juego (Ranked, Servidores Públicos/Privados).
* Torneos organizados.
* Retos de comunidad.

## ⚙️ Especificaciones Técnicas
* **Entrada:** Interacción mediante un clic que activa el evento de recomendación.
* **Proceso:** Algoritmo de selección aleatoria entre los 15 personajes actuales del juego.
* **Salida:** Interfaz gráfica que muestra el nombre del personaje y una imagen identificativa.

## 👥 Personajes Incluidos (Versión Feb 16, 2026)
La base de datos actual incluye:
* **Honored One** - Satoru Gojo
* **Vessel** - Yuji Itadori
* **Restless Gambler** - Kinji Hakari
* **Ten Shadows** - Megumi Fushiguro
* **Perfection** - Mahito
* **Blood Manipulator** - Choso
* **Switcher** - Aoi Todo
* **Defense Attorney** - Hiromi Higuruma
* **Cursed Partners** - Yuta Okkotsu
* **Puppet Master** - Kokichi Muta (Mechamaru)
* **Head of the Hei** - Naoya Zenin
* **Salaryman** - Kento Nanami
* **Locust Guy** - Locust Plague
* **Star Rage** - Yuki Tsukumo
* **Aspiring Mangaka** - Charles Bernard

## 🚀 Instalación y Uso
1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv .venv`.
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Ejecuta la aplicación: `python src/main.py`.

## 🛠️ Tecnologías
* Python 3.x
* Tkinter (Interfaz Gráfica)
* Pillow (Manejo de Imágenes)