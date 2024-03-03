from glob import glob
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp

from examples.common_app import CommonApp, KV

MAIN_KV = """
<Item>:
    size_hint_y:None
    height:dp(50)

MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    BoxLayout:
        orientation:"vertical"
        MDCarousel:
            id:carousel
            size_hint_y:None
            height:dp(200)
        Widget:
"""


class Item(BoxLayout):
    pass


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(MAIN_KV)

    def on_start(self):
        super().on_start()
        self.root.ids.carousel.images = [
            {"source":path} for path in glob("/home/tdynamos/Pictures/Screenshots/*")
        ] 

Example().run()
