from abc import ABC, abstractmethod
from typing import Callable

class PlayerDeMusica(ABC):
    @abstractmethod
    def tocar(self, arquivo: str) -> None:
        ...

class MP3Player(PlayerDeMusica):
    def tocar(self, arquivo: str) -> None:
        print(f"[MP3] Tocando: {arquivo}")

class MP4Player:
    def reproduzir_mp4(self, arquivo: str) -> None:
        print(f"[MP4] Reproduzindo vídeo/áudio: {arquivo}")

class VLCPlayer:
    def abrir_vlc(self, arquivo: str) -> None:
        print(f"[VLC] Abrindo no VLC: {arquivo}")

class PlayerAdapter(PlayerDeMusica):
    def __init__(self, metodo_adaptado: Callable[[str], None]):
        self._metodo_adaptado = metodo_adaptado

    def tocar(self, arquivo: str) -> None:
        self._metodo_adaptado(arquivo)

class SistemaDeMusica:
    def __init__(self, player: PlayerDeMusica):
        self._player = player

    def reproduzir(self, arquivo: str) -> None:
        self._player.tocar(arquivo)

class Principal:
    @staticmethod
    def main() -> None:
        mp4 = MP4Player()
        vlc = VLCPlayer()

        sistema_mp3 = SistemaDeMusica(MP3Player())
        sistema_mp4 = SistemaDeMusica(PlayerAdapter(mp4.reproduzir_mp4))
        sistema_vlc = SistemaDeMusica(PlayerAdapter(vlc.abrir_vlc))

        sistema_mp3.reproduzir("musica.mp3")
        sistema_mp4.reproduzir("clipe.mp4")
        sistema_vlc.reproduzir("show.vlc")


if __name__ == "__main__":
    Principal.main()