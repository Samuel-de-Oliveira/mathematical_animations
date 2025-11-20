from manim import *


class Enunciado(Scene):
    def construct(self):
        # Titulo
        titulo = Tex(f'OAM (2025)')
        titulo.scale(1.5)

        # Enunciado
        enun = Tex(
            f'Quantos são os pares $(m, n)$ \\\\ que satifazem a equação $7n - 3mn = 3$?'
        )

        self.play(Write(titulo))
        self.wait(1)
        self.play(titulo.animate.shift(UP * 3))
        self.play(Write(enun))
        self.wait(1)
        self.play(FadeOut(titulo))
        self.play(FadeOut(enun))


class Resolucao(Scene):
    def construct(self):
        # Equação
        equacao1 = Tex(f'$7n - 3mn = 3$')
        equacao1.scale(2)
        equacao2 = Tex(f'$n(7 - 3m) = 3$')
        equacao2.scale(2)

        # Sistema1
        sis1_1 = VGroup(Tex(f'n = 1'), Tex(f'7 - 3m = 3')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis1_1.scale(2)
        sis1_2 = VGroup(Tex(f'n = 1'), MathTex('m = \\frac{4}{3}')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis1_2.scale(2)
        # Sistema2
        sis2_1 = VGroup(Tex(f'n = 3'), Tex(f'7 - 3m = 1')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis2_1.scale(2)
        sis2_2 = VGroup(Tex(f'n = 3'), MathTex('m = 2')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis2_2.scale(2)
        # Sistema3
        sis3_1 = VGroup(Tex(f'n = -1'), Tex(f'7 - 3m = -3')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis3_1.scale(2)
        sis3_2 = VGroup(Tex(f'n = -1'), MathTex('m = \\frac{10}{3}')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis3_2.scale(2)
        # Sistema4
        sis4_1 = VGroup(Tex(f'n = -3'), Tex(f'7 - 3m = -1')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis4_1.scale(2)
        sis4_2 = VGroup(Tex(f'n = -3'), MathTex('m = \\frac{8}{3}')).arrange(
            DOWN, aligned_edge=LEFT
        )
        sis4_2.scale(2)

        # Solução
        solu = MathTex('S = \{(3, 2)\}')
        solu.scale(2)

        self.play(Write(equacao1))
        self.wait(1)
        self.play(ReplacementTransform(equacao1, equacao2))
        self.wait(1)
        self.play(ReplacementTransform(equacao2, sis1_1))
        self.wait(1)
        self.play(ReplacementTransform(sis1_1, sis1_2))
        self.wait(1)
        self.play(FadeOut(sis1_2))
        self.wait(0.5)
        self.play(Write(sis2_1))
        self.wait(1)
        self.play(ReplacementTransform(sis2_1, sis2_2))
        self.wait(1)
        self.play(FadeOut(sis2_2))
        self.wait(0.5)
        self.play(Write(sis3_1))
        self.wait(1)
        self.play(ReplacementTransform(sis3_1, sis3_2))
        self.wait(1)
        self.play(FadeOut(sis3_2))
        self.wait(0.5)
        self.play(Write(sis4_1))
        self.wait(1)
        self.play(ReplacementTransform(sis4_1, sis4_2))
        self.wait(1)
        self.play(FadeOut(sis4_2))
        self.wait(1.1)
        self.play(Write(solu))
        self.wait(1)
