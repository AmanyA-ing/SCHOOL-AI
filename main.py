import flet as ft
from views.welcome_view import welcome_view
from views.gestion_view import gestion_view
from views.affichage_view import affichage_view
from views.stats_view import stats_view
from views.config_view import config_view
from views.aide_view import aide_view

def main(page: ft.Page):
    page.title = "SCHOOL AI - Gestion Scolaire"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 800

    # Conteneur principal qui va changer de contenu
    container_view = ft.Container(expand=True, padding=20)

    # Fonction pour basculer les vues
    def navigate(index):
        if index == 0: container_view.content = gestion_view(page)
        elif index == 1: container_view.content = affichage_view(page)
        elif index == 2: container_view.content = stats_view(page)
        elif index == 3: container_view.content = config_view(page)
        elif index == 4: container_view.content = aide_view(page)
        page.update()

    # Barre de navigation latérale
    nav_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME, label="Gestion"),
            ft.NavigationRailDestination(icon=ft.icons.LIST_ALT, label="Données"),
            ft.NavigationRailDestination(icon=ft.icons.INSERT_CHART, label="Stats"),
            ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="Config"),
            ft.NavigationRailDestination(icon=ft.icons.HELP, label="Aide"),
        ],
        on_change=lambda e: navigate(e.control.selected_index),
    )

    # Fonction appelée une fois le splash screen fini
    def start_app():
        page.clean()
        page.add(
            ft.Row(
                [
                    nav_rail,
                    ft.VerticalDivider(width=1),
                    container_view,
                ],
                expand=True,
            )
        )
        navigate(0) # Affiche la vue Gestion par défaut

    # Lancement avec la page d'accueil
    page.add(welcome_view(page, start_app))

# Lancement de l'app avec les assets
ft.app(target=main, assets_dir="assets")