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
        self.radius = [10] * 4


class MDCarousel(MDScrollView):
    images = ListProperty([])

    # Android default sizes
    small_item_min = dp(40)
    small_item_max = dp(56)
    large_item = dp(120)

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
        self.add_widget(self._child_layout)

    def get_max_items(self):
        return max(2, 3 + round((self.width - self.small_item_min) / self.large_item))

    def init_images(self, images, start_from=0):
        """Add items to view and set there initial size"""
        max_items = self.get_max_items()
        size_hint = "size_hint_{}".format(self.axis)

        # clear previous ones
        self._child_layout.clear_widgets()

        # Add required widgets
        while len(self._item_widgets) < max_items:
            self._item_widgets.append(MDCarouselImageItem(**{size_hint: None}))
        # Remove excess if any
        while len(self._item_widgets) >= max_items:
            self._item_widgets.pop()

        distance_covered = 0
        w_h = "width" if self.axis == "x" else "height"
        _is_small = False
        for item, widget in zip(images[start_from:max_items], self._item_widgets):
            # set props
            widget.source = item["source"]
            if widget.parent:
                self._child_layout.remove_widget(widget)

            # set size
            distance_left = getattr(self, w_h) - distance_covered
            if distance_left > self.large_item * 2:
                setattr(widget, size_hint, None)
                setattr(widget, w_h, self.large_item)
                distance_covered += getattr(widget, w_h)
            elif not _is_small:
                setattr(widget, size_hint, 1)
                _is_small = True
            else:
                setattr(widget, size_hint, None)
                setattr(widget, w_h, self.small_item_min)

            self._child_layout.add_widget(widget)

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

        distance = touch.pos[0] - self._last_touch_pos[0]
        print(self.scroll_x * self._child_layout.width)
        for widget in self._child_layout.children[::-1]:
            if widget.width < self.small_item_max:
                if self.scroll_x * self._child_layout.width > self.small_item_min:
                    self._child_layout.remove_widget(widget)
                break
            widget.width += distance
            break
