import os

from kivy.properties import ColorProperty, ListProperty
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.scrollview import MDScrollView

with open(
    os.path.join(uix_path, "carousel", "carousel.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())

class MDCarouselImageItem(AsyncImage, StencilBehavior):
    
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fit_mode = "cover"
        self.radius = [10] *4

class MDCarousel(
        MDScrollView
    ):
    
    images = ListProperty([])
    md_bg_color = ColorProperty([0,0,0,0])

    _child_layout = None
    _image_widgets = {}
    
    def __init__(self, *arg, **kwargs):
        self.do_scroll_x = True
        self.do_scroll_y = False
        super().__init__(*arg, **kwargs)
        self.init_child()

    def init_child(self):
        self._child_layout = MDBoxLayout()
        self._child_layout.adaptive_width = True
        self._child_layout.spacing = dp(10)
        self._child_layout.padding = [dp(10)] * 4
        self._child_layout.md_bg_color = self.md_bg_color
        self.add_widget(self._child_layout)

    def on_images(self, instance, images):
        for image in images:
            self._child_layout.add_widget(MDCarouselImageItem(source=image["source"])) 
