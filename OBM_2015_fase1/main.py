import math
from manim import *


class Problema(Scene):
    def construct(self) -> None:
        # Título
        titulo = Tex(f"OBM (2015)")
        titulo.scale(2)

        # Enunciado
        Enunciado = Tex(
            f"Qua é o valor da expressão:\\\\$2015^2 - 2015 \cdot 2014 - 2014^2 + 2014 \cdot 2015$"
        )
        Enunciado.scale(1.5)

        Parte1 = Tex(f"Qua é o valor da expressão:\\\\$a^2 - ab - b^2 + ab$")
        Parte1.scale(2)

        Parte2 = Tex(f"Qua é o valor da expressão:\\\\$a^2 - b^2$")
        Parte2.scale(2)

        Parte3 = Tex(f"Qua é o valor da expressão:\\\\$(a - b)(a + b)$")
        Parte3.scale(2)

        Parte4 = Tex(f"Qua é o valor da expressão:\\\\$(2015 - 2014)(2015 + 2014)$")
        Parte4.scale(2)

        Parte5 = Tex(f"Resultado:\\\\$4029$")
        Parte5.scale(2)

        # Animação
        self.play(Create(titulo))
        self.wait(1.1)
        self.play(titulo.animate.shift(UP * 6.5))
        self.play(Write(Enunciado))
        self.wait(1.1)
        self.play(ReplacementTransform(Enunciado, Parte1))
        self.wait(1.1)
        self.play(ReplacementTransform(Parte1, Parte2))
        self.wait(1.1)
        self.play(ReplacementTransform(Parte2, Parte3))
        self.wait(1.1)
        self.play(ReplacementTransform(Parte3, Parte4))
        self.wait(1.1)
        self.play(ReplacementTransform(Parte4, Parte5))
        self.wait(1.1)
        self.play(FadeOut(titulo))
        self.play(FadeOut(Parte5))


# Agradecimentos:
class Agradecimento(Scene):
    def construct(self) -> None:
        Ins = Tex(f"Inscreva-se para\\\\mais vídeos!")
        Ins.scale(2)

        self.play(Write(Ins))
        self.wait(1)
