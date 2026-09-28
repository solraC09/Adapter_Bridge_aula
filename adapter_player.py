from abc import ABC, abstractmethod


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


class MP4Adapter(PlayerDeMusica):
    def __init__(self, player_mp4: MP4Player):
        self._player_mp4 = player_mp4

    def tocar(self, arquivo: str) -> None:
        self._player_mp4.reproduzir_mp4(arquivo)


class VLCAdapter(PlayerDeMusica):
    def __init__(self, player_vlc: VLCPlayer):
        self._player_vlc = player_vlc

    def tocar(self, arquivo: str) -> None:
        self._player_vlc.abrir_vlc(arquivo)


class SistemaDeMusica:
    def __init__(self, player: PlayerDeMusica):
        self._player = player

    def reproduzir(self, arquivo: str) -> None:
        self._player.tocar(arquivo)


class Principal:
    @staticmethod
    def main() -> None:
        sistema_mp3 = SistemaDeMusica(MP3Player())
        sistema_mp4 = SistemaDeMusica(MP4Adapter(MP4Player()))
        sistema_vlc = SistemaDeMusica(VLCAdapter(VLCPlayer()))

        sistema_mp3.reproduzir("musica.mp3")
        sistema_mp4.reproduzir("clipe.mp4")
        sistema_vlc.reproduzir("show.vlc")


if __name__ == "__main__":
    Principal.main()
