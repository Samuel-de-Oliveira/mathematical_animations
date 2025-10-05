from manim import *

class Carpet(Scene):
    def construct(self) -> None:
        Quadrado = Square()
        titulo = Tex(f'Tapete de Sierpinski')
        titulo.scale(1.75)

        self.play(Create(titulo))
        self.wait(1)
        self.play(titulo.animate.shift(UP * 6))
