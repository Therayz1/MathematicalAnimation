from manim import *

class RectangleProofFinal(Scene):
    def construct(self):
        # Başlık
        title = Tex("Dikdörtgen - Özellikler ve İspat").scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Dikdörtgeni oluştur (yatay olarak daha uzun)
        rectangle = Rectangle(
            width=4.0,
            height=2.5,
            color=BLUE,
            stroke_width=2
        ).shift(UP * 0.5)
        vertices = rectangle.get_vertices()
        
        # Kenarları oluştur
        sides = VGroup(
            Line(vertices[0], vertices[1], color=BLUE, stroke_width=2),  # AB
            Line(vertices[1], vertices[2], color=BLUE, stroke_width=2),  # BC
            Line(vertices[2], vertices[3], color=BLUE, stroke_width=2),  # CD
            Line(vertices[3], vertices[0], color=BLUE, stroke_width=2)   # DA
        )
        
        # Köşe etiketleri (dışarıda)
        labels = VGroup(
            Tex("A").next_to(vertices[0], DOWN + LEFT, buff=0.2),   # Sol alt
            Tex("B").next_to(vertices[1], DOWN + RIGHT, buff=0.2),  # Sağ alt
            Tex("C").next_to(vertices[2], UP + RIGHT, buff=0.2),    # Sağ üst
            Tex("D").next_to(vertices[3], UP + LEFT, buff=0.2)      # Sol üst
        )
        
        self.play(Create(sides), run_time=2)
        self.play(Write(labels))
        self.wait()
        
        # Her köşe için doğru yönlendirilmiş dik açı sembolleri
        angles = VGroup(
            RightAngle(  # A köşesi (sol alt)
                sides[3], sides[0],
                length=0.2,
                color=WHITE,
                quadrant=(1, 1)
            ),
            RightAngle(  # B köşesi (sağ alt)
                sides[0], sides[1],
                length=0.2,
                color=WHITE,
                quadrant=(-1, 1)
            ),
            RightAngle(  # C köşesi (sağ üst)
                sides[1], sides[2],
                length=0.2,
                color=WHITE,
                quadrant=(-1, -1)
            ),
            RightAngle(  # D köşesi (sol üst)
                sides[2], sides[3],
                length=0.2,
                color=WHITE,
                quadrant=(1, -1)
            )
        )
        
        # Metin için sabit pozisyon
        text_position = DOWN * 2
        
        # Özellik 1: Karşılıklı kenarlar eşit
        prop1 = Tex("1. Karşılıklı kenarlar eşit uzunlukta", font_size=36).move_to(text_position)
        self.play(Write(prop1))
        
        # Karşılıklı kenarları grupla ve sırayla göster
        parallel_pairs = [(sides[0], sides[2]), (sides[1], sides[3])]
        for pair in parallel_pairs:
            self.play(
                *[side.animate.set_color(YELLOW) for side in pair],
                rate_func=there_and_back,
                run_time=1
            )
        self.wait()
        
        # Özellik 2: Dik açılar
        prop2 = Tex("2. Tüm iç açılar 90°", font_size=36).move_to(text_position)
        self.play(ReplacementTransform(prop1, prop2))
        self.play(LaggedStart(*[Create(angle) for angle in angles], lag_ratio=0.3))
        self.wait()
        
        # Özellik 3: Köşegenler
        prop3 = Tex("3. Köşegenler eşit ve birbirini ortalar", font_size=36).move_to(text_position)
        
        diagonal1 = Line(vertices[0], vertices[2], color=GREEN, stroke_width=2)
        diagonal2 = Line(vertices[1], vertices[3], color=ORANGE, stroke_width=2)
        center_dot = Dot(diagonal1.get_center(), color=PURPLE, radius=0.05)
        
        self.play(ReplacementTransform(prop2, prop3))
        self.play(Create(diagonal1), Create(diagonal2), run_time=1.5)
        self.play(GrowFromCenter(center_dot))
        self.wait()
        
        # Özet
        summary = VGroup(
            Tex("Özet:", color=YELLOW, font_size=40),
            Tex("• Karşılıklı kenarlar eşit", font_size=36),
            Tex("• 4 dik açı", font_size=36),
            Tex("• Köşegenler eşit", font_size=36),
            Tex("• Köşegenler birbirini ortalar", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        summary.next_to(rectangle, RIGHT, buff=1.5)
        
        self.play(
            FadeOut(prop3),
            Write(summary),
            run_time=2
        )
        self.wait(2)
