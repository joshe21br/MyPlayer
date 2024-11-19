import flet as ft
import pygame
import json
import os

pygame.mixer.init()

def main(page: ft.Page):
    page.title = "Joshe Player"
    page.bgcolor = "#121212"
    page.horizontal_alignment = "center"
    page.scroll = ft.ScrollMode.AUTO
    page.window.width = 600
    page.window.height = 550

    playlist = []
    current_track_index = -1

    # Funções para carregar, salvar, tocar e excluir a playlist
    def load_playlist():
        try:
            with open("playlist.json", "r") as f:
                data = json.load(f)
                playlist.clear()
                playlist.extend(data)
                update_playlist_view()
        except FileNotFoundError:
            pass

    def save_playlist():
        with open("playlist.json", "w") as f:
            json.dump(playlist, f)
        print("Playlist salva.")

    def play_music(track):
        try:
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Erro ao carregar a música: {e}")

    def pause_music():
        pygame.mixer.music.pause()

    def unpause_music():
        pygame.mixer.music.unpause()

    def stop_music():
        pygame.mixer.music.stop()

    def add_to_playlist(files):
        if files:
            for file in files:
                playlist.append(file.path)
            update_playlist_view()

    def update_playlist_view():
        playlist_view.controls.clear()
        for index, track in enumerate(playlist):
            color = "yellow" if index == current_track_index else "white"
            playlist_view.controls.append(
                ft.Row(
                    [
                        ft.Text(
                            f"{index + 1}. {os.path.basename(track)}",
                            color=color,
                            size=14,
                        ),
                        ft.IconButton(
                            icon=ft.icons.PLAY_ARROW,
                            icon_color="white",
                            on_click=lambda e, i=index: select_track(i),
                        ),
                    ],
                    alignment="spaceBetween",
                )
            )
        page.update()

    def select_track(index):
        nonlocal current_track_index
        current_track_index = index
        play_music(playlist[current_track_index])
        update_playlist_view()

    def prev_track():
        nonlocal current_track_index
        if current_track_index > 0:
            current_track_index -= 1
            play_music(playlist[current_track_index])
            update_playlist_view()

    def next_track():
        nonlocal current_track_index
        if current_track_index < len(playlist) - 1:
            current_track_index += 1
            play_music(playlist[current_track_index])
            update_playlist_view()

    def clear_playlist():
        nonlocal current_track_index
        playlist.clear()
        current_track_index = -1
        update_playlist_view()

    def play_playlist():
        if playlist:
            play_music(playlist[0])

    def load_music():
        file_picker.pick_files(allow_multiple=True)

    file_picker = ft.FilePicker(on_result=lambda e: add_to_playlist(e.files))
    page.overlay.append(file_picker)

    playlist_view = ft.Column(
        spacing=10,
        controls=[],
        alignment="start",
        scroll=ft.ScrollMode.AUTO,
    )

    playlist_view_container = ft.Container(
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text("Playlist", size=20, weight="bold", color="white"),
                ft.Container(
                    content=playlist_view,
                    height=200,
                    width=550,
                    bgcolor="#444444",
                    border_radius=8,
                    padding=ft.padding.all(8),
                ),
            ],
            alignment="start",
        ),
        bgcolor="#333333",
        padding=ft.padding.all(10),
    )

    volume_slider = ft.Slider(
        min=0,
        max=1,
        divisions=10,
        value=1.0,
        label="{value}",
        on_change=lambda e: pygame.mixer.music.set_volume(e.control.value),
        width=300,
        height=25,
    )

    def play_selected_track():
        if current_track_index >= 0:
            play_music(playlist[current_track_index])
        elif playlist:
            play_music(playlist[0])

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Image(src="/home/joshe/pyflat/app-01/img/joshe.jpg", width=150, height=150),
                    ],
                    alignment="center",
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Joshe Player",
                            size=32,
                            weight="bold",
                            color="white",
                            text_align="center",
                        ),
                        playlist_view_container,
                        ft.Row(  # Botões de controle do player em uma linha
                            [
                                ft.IconButton(
                                    icon=ft.icons.PLAY_ARROW,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: play_selected_track(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.PAUSE,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: pause_music(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.STOP,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: stop_music(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: prev_track(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ARROW_FORWARD,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: next_track(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CLEAR_ALL,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: clear_playlist(),
                                ),
                            ],
                            alignment="center",  # Alinha os botões no centro
                            spacing=10,  # Espaçamento entre os botões
                        ),
                        volume_slider,
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.SAVE,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: save_playlist(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.PLAYLIST_PLAY,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: play_playlist(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_FOREVER,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: clear_playlist(),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.FOLDER,
                                    icon_color="white",
                                    bgcolor="#6c63ff",
                                    on_click=lambda e: load_music(),  # Botão de carregar músicas
                                ),
                            ],
                            alignment="center",
                            spacing=10,  # Espaçamento entre os botões
                        ),
                    ],
                    spacing=20,
                    alignment="center",
                ),
            ],
            alignment="center",
            spacing=20,
        ),
    )

    footer = ft.Container(
        content=ft.Text(
            "Versão: 1.0 | Desenvolvedor: Joshe | Email: joshuasotero@protonmail.com | Telefone: (85) 98978-0215",
            color="white",
            size=12,
            text_align="center",
        ),
        bgcolor="#333333",
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
    )
    page.add(footer)

    # Carrega playlist ao iniciar
    load_playlist()

ft.app(target=main)

