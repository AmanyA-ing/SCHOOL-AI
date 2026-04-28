import flet as ft
import time

# On importe toutes les vues que nous avons créées dans le dossier /views
from views.config_view import config_view
from views.gestion_view import gestion_view
from views.historique_view import historique_view
from views.stats_view import stats_view
from views.aide_view import aide_view

def main(page: ft.Page):
    # --- 1. CONFIGURATION DE LA PAGE ---
    page.title = "SCHOOL AI - Système de Gestion Intégré"
    page.window_width = 1100
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- 2. ÉCRAN DE CHARGEMENT (SPLASH SCREEN) ---
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    logo = ft.Icon(name=ft.icons.SCHOOL_ROUNDED, size=120, color="blue_800")
    titre = ft.Text("SCHOOL AI", size=45, weight="bold", color="blue_900")
    sous_titre = ft.Text("Chargement du moteur d'intelligence...", italic=True)
    barre_chargement = ft.ProgressBar(width=400, color="blue_700", bgcolor="blue_100")
    
    page.add(logo, titre, sous_titre, barre_chargement)
    time.sleep(3) # On simule le chargement
    
    # --- 3. NETTOYAGE ET PRÉPARATION DU MENU ---
    page.controls.clear()
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    # Le conteneur central qui changera de contenu selon le menu choisi
    content_area = ft.Container(expand=True, padding=20)

    # Fonction pour changer de page
    def route_change(e):
        index = e.control.selected_index
        if index == 0:
            content_area.content = config_view(page)
        elif index == 1:
            content_area.content = gestion_view(page)
        elif index == 2:
            content_area.content = historique_view(page)
        elif index == 3:
            content_area.content = stats_view(page)
        elif index == 4:
            content_area.content = aide_view(page)
        page.update()

    # --- 4. BARRE DE NAVIGATION (RAIL) ---
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        bgcolor="blue_grey_50",
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Config"),
            ft.NavigationRailDestination(icon=ft.icons.ADD_SHOPPING_CART_OUTLINED, selected_icon=ft.icons.ADD_SHOPPING_CART, label="Gestion"),
            ft.NavigationRailDestination(icon=ft.icons.HISTORY_OUTLINED, selected_icon=ft.icons.HISTORY, label="Historique"),
            ft.NavigationRailDestination(icon=ft.icons.INSERT_CHART_OUTLINED, selected_icon=ft.icons.INSERT_CHART, label="Stats"),
            ft.NavigationRailDestination(icon=ft.icons.HELP_OUTLINE, selected_icon=ft.icons.HELP, label="Aide"),
        ],
        on_change=route_change,
    )

    # Initialisation sur la première page (Config)
    content_area.content = config_view(page)

    # --- 5. ASSEMBLAGE FINAL ---
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )
    page.update()

# Lancement de l'application
if __name__ == "__main__":
    ft.app(target=main)