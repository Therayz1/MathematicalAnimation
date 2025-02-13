from manim import *

class SquareProofFinal(Scene):
    def construct(self):
        # Başlık
        title = Tex("Kare - Özellikler ve İspat").scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Kareyi merkeze al ve biraz yukarı kaydır
        square = Square(side_length=3, color=BLUE, stroke_width=2).shift(UP * 0.5)
        vertices = square.get_vertices()
        
        # Kenarları oluştur
        sides = VGroup(
            Line(vertices[0], vertices[1], color=BLUE, stroke_width=2),  # AB
            Line(vertices[1], vertices[2], color=BLUE, stroke_width=2),  # BC
            Line(vertices[2], vertices[3], color=BLUE, stroke_width=2),  # CD
            Line(vertices[3], vertices[0], color=BLUE, stroke_width=2)   # DA
        )
        
        # Köşe etiketleri
        labels = VGroup(
            Tex("A").next_to(vertices[0], DL, buff=0.1),
            Tex("B").next_to(vertices[1], DR, buff=0.1),
            Tex("C").next_to(vertices[2], UR, buff=0.1),
            Tex("D").next_to(vertices[3], UL, buff=0.1)
        )
        
        self.play(Create(sides), run_time=2)
        self.play(Write(labels))
        self.wait()
        
        # Özellik metinleri için sabit pozisyon (karenin altında)
        text_position = DOWN * 2
        
        # Özellik 1: Eş kenarlar
        prop1 = Tex("1. Tüm kenarlar eşit uzunlukta", font_size=36).move_to(text_position)
        self.play(Write(prop1))
        
        for side in sides:
            self.play(
                side.animate.set_color(YELLOW),
                rate_func=there_and_back,
                run_time=0.5
            )
        self.wait()
        
        # Özellik 2: Dik açılar (içeride)
        prop2 = Tex("2. Tüm iç açılar 90°", font_size=36).move_to(text_position)
        
        # Dik açı sembolleri içeride ve daha küçük
        angles = VGroup()
        for i in range(4):
            angle = RightAngle(
                sides[i], 
                sides[(i+1)%4], 
                length=0.2,  # Daha küçük boyut
                color=WHITE,
                quadrant=(1,1) if i == 0 else (-1,1) if i == 1 else (-1,-1) if i == 2 else (1,-1)
            )
            angles.add(angle)
        
        self.play(ReplacementTransform(prop1, prop2))
        self.play(LaggedStart(*[Create(angle) for angle in angles], lag_ratio=0.3))
        self.wait()
        
        # Özellik 3: Köşegenler
        prop3 = Tex("3. Köşegenler eşit, dik ve birbirini ortalar", font_size=36).move_to(text_position)
        
        diagonal1 = Line(vertices[0], vertices[2], color=GREEN, stroke_width=2)
        diagonal2 = Line(vertices[1], vertices[3], color=ORANGE, stroke_width=2)
        center_dot = Dot(diagonal1.get_center(), color=PURPLE, radius=0.05)
        
        self.play(ReplacementTransform(prop2, prop3))
        self.play(Create(diagonal1), Create(diagonal2), run_time=1.5)
        self.play(GrowFromCenter(center_dot))
        
        # Köşegenlerin kesişimindeki dik açı (daha küçük)
        center_right_angle = RightAngle(diagonal1, diagonal2, length=0.2, color=RED)
        self.play(Create(center_right_angle))
        self.wait()
        
        # Özellik 4: Simetri eksenleri
        prop4 = Tex("4. Dört simetri ekseni", font_size=36).move_to(text_position)
        
        symmetry_axes = VGroup(
            DashedLine(vertices[0], vertices[2], dash_length=0.1),
            DashedLine(vertices[1], vertices[3], dash_length=0.1),
            DashedLine(square.get_top(), square.get_bottom(), dash_length=0.1),
            DashedLine(square.get_left(), square.get_right(), dash_length=0.1)
        ).set_color(YELLOW)
        
        self.play(ReplacementTransform(prop3, prop4))
        self.play(Create(symmetry_axes), run_time=2)
        self.wait()
        
        # Özet
        summary = VGroup(
            Tex("Özet:", color=YELLOW, font_size=40),
            Tex("• 4 eş kenar", font_size=36),
            Tex("• 4 dik açı", font_size=36),
            Tex("• 4 simetri ekseni", font_size=36),
            Tex("• Eşit ve dik köşegenler", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        summary.next_to(square, RIGHT, buff=1.5)
        
        self.play(
            FadeOut(VGroup(prop4, symmetry_axes)),
            Write(summary),
            run_time=2
        )
        self.wait(2)
