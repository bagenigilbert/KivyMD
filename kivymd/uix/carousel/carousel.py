import os

from kivy.properties import ColorProperty, ListProperty, BooleanProperty
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.carousel.carousel_strategy import MultiBrowseCarouselStrategy

with open(
    os.path.join(uix_path, "carousel", "carousel.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDCarouselImageItem(AsyncImage, StencilBehavior):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fit_mode = "cover"
        self.radius = [10] * 4


class MDCarousel(MDScrollView):
    images = ListProperty([])
    is_horizontal = BooleanProperty(True)
    alignment = "none"
    # Axis
    axis = "x"

    _child_layout = None
    _item_widgets = []

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.do_scroll_x = True
        self.do_scroll_y = False
        self.bar_color = [0, 0, 0, 0]
        self.bar_inactive_color = [0, 0, 0, 0]

        # Container
        self._child_layout = MDBoxLayout()
        self._child_layout.size_hint = [None, None]
        self._child_layout.size = self.size
        self._child_layout.spacing = dp(8)
        self._child_layout.padding = [dp(16), dp(8)]
        self._child_layout.is_horizontal = self.is_horizontal
        self._child_layout.alignment = self.alignment
        self.add_widget(self._child_layout)

    def init_images(self, images, start_from=0):
        for image in images:
            self._child_layout.add_widget( MDCarouselImageItem(size_hint_x=None, width=dp(100), source = image["source"]) )

        clas = MultiBrowseCarouselStrategy().on_first_child_measured_with_margins(
            self._child_layout, MDCarouselImageItem(size_hint_x=None, width=dp(100))
        )
        print(clas)

    def on_images(self, instance, images):
        self.init_images(images)

    def on_size(self, instance, size):
        self._child_layout.size = self.size
        self.init_images(self.images)

    _last_touch_pos = []

    def on_touch_down(self, touch):
        self._last_touch_pos = list(touch.pos)
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
