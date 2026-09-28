from abc import ABC, abstractmethod


class Renderizador(ABC):

    @abstractmethod
    def desenhar_circulo(self, x: float, y: float, raio: float) -> None:
        ...

    @abstractmethod
    def desenhar_retangulo(self, x: float, y: float,
            largura: float, altura: float) -> None:
        ...


class RenderizadorVetorial(Renderizador):

    def desenhar_circulo(self, x, y, raio):
        print(f"[Vetorial] círculo: centro=({x}, {y}), raio={raio}")

    def desenhar_retangulo(self, x, y, largura, altura):
        print(f"[Vetorial] retângulo: canto=({x}, {y}), "
            f"{largura}x{altura}")


class RenderizadorRaster(Renderizador):

    def desenhar_circulo(self, x, y, raio):
        print(f"[Raster] pintando pixels de um círculo em ({x}, {y}) "
            f"com raio {raio}px")

    def desenhar_retangulo(self, x, y, largura, altura):
        print(f"[Raster] pintando {largura * altura} pixels de um "
            f"retângulo em ({x}, {y})")


class Forma(ABC):

    def __init__(self, renderizador: Renderizador):
        self._renderizador = renderizador 

    @abstractmethod
    def desenhar(self) -> None:
        ...

    @abstractmethod
    def redimensionar(self, fator: float) -> None:
        ...


class Circulo(Forma):
    def __init__(self, x, y, raio, renderizador: Renderizador):
        super().__init__(renderizador)
        self.x, self.y, self.raio = x, y, raio

    def desenhar(self):
        self._renderizador.desenhar_circulo(self.x, self.y, self.raio)

    def redimensionar(self, fator):
        self.raio *= fator


class Retangulo(Forma):
    def __init__(self, x, y, largura, altura, renderizador: Renderizador):
        super().__init__(renderizador)
        self.x, self.y = x, y
        self.largura, self.altura = largura, altura

    def desenhar(self):
        self._renderizador.desenhar_retangulo(
            self.x, self.y, self.largura, self.altura)

    def redimensionar(self, fator):
        self.largura *= fator
        self.altura *= fator



if __name__ == "__main__":
    vetorial = RenderizadorVetorial()
    raster = RenderizadorRaster()

    formas = [
        Circulo(10, 10, 5, vetorial),
        Circulo(10, 10, 5, raster),
        Retangulo(0, 0, 4, 3, vetorial),
        Retangulo(0, 0, 4, 3, raster),
    ]

    for forma in formas:
        forma.desenhar()

    print("\n--- Redimensionando o primeiro círculo (x2) ---")
    formas[0].redimensionar(2)
    formas[0].desenhar()
