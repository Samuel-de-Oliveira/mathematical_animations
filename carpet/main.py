from manim import *

class SierpinskiCarpetSlow(Scene):
    def generate_level(self, level, side_length=4):
        """
        Gera o tapete de Sierpinski até um nível específico.
        Retorna um VGroup contendo todos os quadrados visíveis.
        """
        carpet = VGroup()
        size = side_length / (3 ** level)

        for i in range(3**level):
            for j in range(3**level):
                # Remover quadrados centrais nos níveis anteriores
                x, y = i, j
                keep = True

                for k in range(level):
                    if (x % 3 == 1) and (y % 3 == 1):
                        keep = False
                        break
                    x //= 3
                    y //= 3

                if keep:
                    sq = Square(side_length=size)
                    sq.set_fill(YELLOW, opacity=1)
                    sq.set_stroke(BLACK, width=1)
                    sq.move_to(
                        LEFT * side_length/2 + RIGHT * (j + 0.5) * size +
                        UP * side_length/2 - DOWN * (i + 0.5) * size
                    )
                    carpet.add(sq)

        return carpet

    def construct(self):
        title = Text("Tapete de Sierpinski", font_size=44)

        self.play(FadeIn(title))
        self.play(title.animate.scale(1.5))
        self.play(title.animate.shift(UP * 4))

        # Etapa 0 — quadrado único
        level0 = self.generate_level(0)
        level0.shift(DOWN * 5) # Coloca o quadrado em baixo
        self.play(FadeIn(level0))
        # Descrição 0
        desc0 = Text(
                "Wacław F. Sierpiński Foi um matemático polonês\n"
                "que contribuiu bastante para os estudos da teoria\n"
                "dos conjuntos.", font_size=36)
        desc0.shift(DOWN * 6)
        self.play(Write(desc0))

        self.wait(1)

        # Etapa 1 — buraco central
        level1 = self.generate_level(1)
        level1.shift(DOWN * 5) # Coloca o quadrado em baixo
        self.play(ReplacementTransform(level0, level1, run_time=3))
        # Descrição 1
        desc1 = Text(
                "Mas, durante um tempo, o mesmo se interessou por\n"
                "fractais. Tal qual desenvolveu o conhecido Tapete\n"
                "de sierpinski. que lembra um formato de uma \"esponja\"", font_size=36)
        desc1.shift(DOWN * 6)
        self.play(ReplacementTransform(desc0, desc1))

        self.wait(1)

        # Etapa 2 — mais detalhes
        level2 = self.generate_level(2)
        level2.shift(DOWN * 5) # Coloca o quadrado em baixo
        self.play(ReplacementTransform(level1, level2, run_time=3))
        # Descrição 2
        desc2 = Text(
                "Mas, durante um tempo, o mesmo se interessou por\n"
                "fractais. Tal qual desenvolveu o conhecido Tapete\n"
                "de sierpinski. que lembra um formato de uma \"esponja\"", font_size=36)
        desc2.shift(DOWN * 6)
        self.play(ReplacementTransform(desc1, desc2))

        self.wait(1)

        # Etapa 3 — mais refinado (opcional)
        # se quiser mais curto, comente estas 3 linhas
        level3 = self.generate_level(3)
        level3.shift(DOWN * 5) # Coloca o quadrado em baixo
        self.play(ReplacementTransform(level2, level3, run_time=3))
        desc3 = Text(
                "Para construi-lo basta que pegamos um quadrado e\n"
                "divida-mos ele em 9 partes. Logo após tirar sua\n"
                "parte central. Fazendo isso infinitas vezes", font_size=36)
        desc3.shift(DOWN * 6)
        self.play(ReplacementTransform(desc2, desc3))

        self.wait(4)
        self.play(FadeOut(title), FadeOut(level3), FadeOut(desc3))
