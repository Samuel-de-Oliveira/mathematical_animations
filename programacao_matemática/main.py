from manim import *


class Introducao(Scene):
    def construct(self):
        codigo1 = Code(
            code_file=r'codes/intro.c', language='c', background='window'
        )
        codigo2 = Code(
            code_file=r'codes/exp.c', language='c', background='window'
        )
        titulo = Tex(f'Linguagem de programação')
        titulo.scale(2)
        titulo.shift(UP * 2)
        codigo1.scale(1.4)

        self.wait(1.1)
        self.play(FadeIn(codigo1))
        self.wait(1.1)
        self.play(codigo1.animate.scale(5 / 7))
        self.play(codigo1.animate.shift(DOWN * 2))
        self.play(Write(titulo))
        self.wait(1.1)
        self.play(FadeOut(titulo))
        self.play(ReplacementTransform(codigo1, codigo2))
        self.wait(1.1)
