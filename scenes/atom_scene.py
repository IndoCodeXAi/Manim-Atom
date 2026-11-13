"""
Animasi 3D Atom - Manim
Menampilkan inti atom dan elektron yang mengorbit, cocok untuk konten
edukasi fisika (dunia kuantum / atom) di YouTube/TikTok.

Render lokal (kalau punya Termux/PC):
    manim -qm scenes/atom_scene.py AtomScene

Atau biarkan GitHub Actions yang render (lihat workflow render.yml).
"""

from manim import *


class AtomScene(ThreeDScene):
    def construct(self):
        # Atur sudut kamera 3D
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # Judul pembuka
        title = Text("Dunia Atom", font_size=48)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Inti atom
        nucleus = Sphere(radius=0.5, resolution=(20, 20)).set_color(RED)
        nucleus_label = Text("Inti Atom", font_size=24)
        nucleus_label.to_corner(DL)

        self.play(FadeIn(nucleus))
        self.add_fixed_in_frame_mobjects(nucleus_label)
        self.play(Write(nucleus_label))
        self.wait(1)

        # Orbit dan elektron
        orbit_radii = [2, 3, 4]
        orbits = VGroup()
        electrons = VGroup()

        for r in orbit_radii:
            orbit = Circle(radius=r, color=BLUE_D).rotate(PI / 2, axis=RIGHT)
            orbits.add(orbit)

            electron = Sphere(radius=0.15, resolution=(10, 10)).set_color(YELLOW)
            electron.move_to(orbit.point_from_proportion(0))
            electrons.add(electron)

        self.play(Create(orbits), run_time=2)
        self.play(FadeIn(electrons))
        self.wait(0.5)

        # Putar kamera otomatis supaya terlihat 3D-nya
        self.begin_ambient_camera_rotation(rate=0.15)

        # Elektron berputar di orbit masing-masing dengan kecepatan beda
        rotations = []
        for electron, speed in zip(electrons, [2, 1.5, 1]):
            rotations.append(
                Rotate(
                    electron,
                    angle=2 * PI * speed,
                    about_point=ORIGIN,
                    axis=RIGHT,
                    run_time=6,
                    rate_func=linear,
                )
            )
        self.play(*rotations)
        self.stop_ambient_camera_rotation()
        self.wait(1)

        # Penjelasan penutup
        explanation = Text(
            "Elektron sebenarnya bukan bergerak\ndi jalur pasti seperti ini,\n"
            "melainkan berupa 'awan probabilitas'",
            font_size=28,
            line_spacing=1.2,
        )
        explanation.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(3)
