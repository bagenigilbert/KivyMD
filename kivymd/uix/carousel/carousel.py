import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    StringProperty,
    OptionProperty,
    NumericProperty,
    ListProperty,
)
from kivy.uix.image import AsyncImage
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
    StencilBehavior,
)
from kivymd.uix.carousel.carousel_strategy import AvaliableStrategies

with open(
    os.path.join(uix_path, "carousel", "carousel.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDCarouselImageItem(AsyncImage, StencilBehavior):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fit_mode = "cover"
        self.radius = [30] * 4


class MDCarouselContainer(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RecycleBoxLayout,
    MDAdaptiveWidget,
):
    pass


class MDCarousel(RecycleView):
    strategy = OptionProperty(
        "MultiBrowseCarouselStrategy", options=[AvaliableStrategies.avaliable]
    )
    is_horizontal = BooleanProperty(True)
    alignment = StringProperty("default")
    desired_item_size = NumericProperty(140)

    _strategy = None
    _variable_item_size = dp(50)

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.bind(data=self.update_strategy)
        self.bind(size=self.update_strategy)
        self.bind(strategy=self.update_strategy)

    def update_strategy(self, *args):
        if self._strategy.__class__.__name__ != self.strategy:
            self._strategy = AvaliableStrategies.get(
                self.strategy, len(self.data), self.ids._container
            )
        self._strategy.arrange(self.alignment, self.width, self.desired_item_size)
        Clock.schedule_once(self._strategy.set_init_size)
        return self._strategy

    _last_touch_point = [0, 0]

    def on_touch_down(self, touch):
        self._last_touch_point = list(touch.pos)
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        self._strategy.tranform_widgets(
            touch.pos[0] - self._last_touch_point[0], self.scroll_x
        )
