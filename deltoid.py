from manim import *

class DeltoidProof(Scene):
    def construct(self):
        # Noktaları tanımla
        A = Dot(ORIGIN, color=BLUE)
        B = Dot([-1, 0.5, 0], color=RED)
        C = Dot([0, 2, 0], color=GREEN)
        D = Dot([1, 0.5, 0], color=RED)
        noktalar = VGroup(A, B, C, D)

        # Etiketler
        etiketler = VGroup(
            Tex("A").next_to(A, DOWN),
            Tex("B").next_to(B, LEFT),
            Tex("C").next_to(C, UP),
            Tex("D").next_to(D, RIGHT)
        )

        # Kenarları çiz
        AB = Line(A, B, color=YELLOW)
        BC = Line(B, C, color=YELLOW)
        CD = Line(C, D, color=YELLOW)
        DA = Line(D, A, color=YELLOW)
        kenarlar = VGroup(AB, BC, CD, DA)

        # Eşit kenarları işaretle
        AB_ticks = VGroup(
            Triangle().scale(0.1).rotate(PI/2).next_to(AB, LEFT, buff=0.1),
            Triangle().scale(0.1).rotate(PI/2).next_to(DA, RIGHT, buff=0.1)
        )
        
        BC_ticks = VGroup(
            Triangle().scale(0.1).rotate(-PI/2).next_to(BC, LEFT, buff=0.1),
            Triangle().scale(0.1).rotate(-PI/2).next_to(CD, RIGHT, buff=0.1)
        )

        # Köşegenler
        AC = Line(A, C, color=BLUE)
        BD = Line(B, D, color=RED)
        O = Dot([0, 0.5, 0], color=PURPLE)
        O_etiket = Tex("O", color=PURPLE).next_to(O, DOWN)

        # Dik açı göstergesi
        dik_aci = RightAngle(AC, BD, length=0.3, quadrant=(-1,1))

        # Metinler
        ozellikler = Tex(
            "Deltoid Özellikleri:\\\\",
            "1. İki komşu kenar çifti eşit\\\\",
            "2. Köşegenler dik kesişir\\\\",
            "3. Bir köşegen diğerini ortalar",
            font_size=30
        ).to_edge(DOWN)

        # Animasyon sırası
        self.play(LaggedStart(
            Create(A), Create(B), Create(C), Create(D),
            lag_ratio=0.5
        ))
        self.play(Write(etiketler))
        self.wait()
        
        self.play(LaggedStart(
            Create(AB), Create(BC), Create(CD), Create(DA),
            lag_ratio=0.5
        ))
        self.wait()
        
        self.play(Write(AB_ticks), Write(BC_ticks))
        self.wait()
        
        self.play(Create(AC), Create(BD))
        self.play(Create(O), Write(O_etiket))
        self.wait()
        
        self.play(Create(dik_aci))
        self.wait()
        
        self.play(Write(ozellikler))
        self.wait(3)
