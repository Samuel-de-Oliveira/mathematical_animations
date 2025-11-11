from manim import *


class Introducao(Scene):
    def construct(self):
        codigo = Code(
            code_file=r'codes/intro.c', language='c', background='window'
        )
        titulo = Tex(f'Linguagem de programação')
        titulo.scale(2)
        titulo.shift(UP * 2)
        codigo.scale(2)

        self.wait(0.25)
        self.play(FadeIn(codigo))
        self.wait(1)
        self.play(codigo.animate.scale(2/3))
        self.play(codigo.animate.shift(DOWN * 2))
        self.play(Write(titulo))
        self.wait(0.5)
