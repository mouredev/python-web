import reflex as rx

import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.newsletter import newsletter
from link_bio.components.title import title
from link_bio.styles.styles import Color, Spacing


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Bash/Shell desde cero",
            "Curso de terminal, línea de comandos y scripting",
            "/icons/terminal.svg",
            const.BASH_COURSE_URL,
        ),
        link_button(
            "Java y POO desde cero",
            "Curso de +8h, 75 lecciones y 150 ejercicios",
            "/icons/java.svg",
            const.JAVA_COURSE_URL,
        ),
        link_button(
            "Python desde cero",
            "Curso de +44h: Fundamentos, frontend, backend, testing...",
            "/icons/python.svg",
            const.PYTHON_COURSE_URL,
        ),
        link_button(
            "JavaScript desde cero",
            "Curso de +14h, 120 lecciones y 220 ejercicios",
            "/icons/js.svg",
            const.JS_COURSE_URL,
        ),
        link_button(
            "Git y GitHub",
            "Curso de 5h para aprender Git y GitHub desde cero",
            "/icons/git.svg",
            const.GIT_COURSE_URL,
        ),
        link_button(
            "SQL y Bases de Datos",
            "Curso de 7h desde cero para aprender los fundamentos de SQL",
            "/icons/sql.svg",
            const.SQL_COURSE_URL,
        ),
        link_button(
            "Retos de programación",
            "Practica lógica con ejercicios y proyectos reales",
            "/icons/challenges.png",
            const.CODE_CHALLENGES_URL,
        ),
        link_button(
            "Un día, un lenguaje",
            "Primeros pasos en los 11 lenguajes de programación más usados",
            "/icons/code.svg",
            const.LANGUAGES_COURSE_URL,
        ),
        title("Mucho más en"),
        link_button(
            "mouredev pro",
            "Estudia programación de manera diferente",
            "/icons/pro.svg",
            const.PRO_URL,
            True,
            Color.ORANGE.value,
        ),
        link_button(
            "Guías de programación",
            "Mi listado de guías gratis en PDF para aprender desarrollo",
            "/icons/book.svg",
            const.RESOURCES_URL,
            True,
            Color.GREEN.value,
        ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "/icons/discord.svg",
            const.DISCORD_URL,
        ),
        link_button(
            "YouTube",
            "Cursos y tutoriales sobre desarrollo de software",
            "/icons/youtube.svg",
            const.YOUTUBE_URL,
        ),
        newsletter(),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )
