import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    StringProperty,
    OptionProperty,
    NumericProperty,
    ListProperty
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
    _container = None
    _variable_item_size =  dp(50)
    _scroll_distance = ListProperty([0,0])
    
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.bind(data=self.update_strategy)
        self.bind(size=self.update_strategy)
        self.bind(ids=self.set_container)

    def set_container(self, *args):
        self._container = self.ids._container

    def set_init_size(self, *arg):
        if len(self._container.children) < (
            self._strategy.small_count
            + self._strategy.medium_count
            + self._strategy.large_count
        ):
            # Reset the size and then retry
            for widget in self._container.children:
                widget.width = self.desired_item_size - dp(30)
            Clock.schedule_once(self.set_init_size)
            return
        item_index = 0
        for type_item in ["large", "medium", "small"]:
            for _ in range(
                getattr(self._strategy, "{}_count".format(type_item))
            ):
                widget = self._container.children[::-1][item_index]
                widget.width = getattr(
                    self._strategy, "{}_size".format(type_item)
                ) - dp(8) # dp(8) -> spacing
                item_index += 1
        self._old_children = self._container.children
    
    @staticmethod
    def clamp(value, min_val=0, max_val=0):
        return min(max(value, min_val), max_val)

    def on__scroll_distance(self, instance, distance_coord):
        if instance != self:
            return
        distance = distance_coord[0] - self._last_touch_point[0]
        for child in self._container.children[::-1]:
            print(distance)
            child.width = self.clamp(
                child.width + (distance/2),
                self._strategy.small_size,
                self._strategy.large_size,
            )
            return
        return

    def update_strategy(self, *args):
        self._strategy = AvaliableStrategies.get(self.strategy).arrange(
            self.alignment, self.width, self.desired_item_size, len(self.data)
        )
        Clock.schedule_once(self.set_init_size)
        return self._strategy

    _last_touch_point = [0, 0]

    def on_touch_down(self, touch):
        self._last_touch_point = list(touch.pos)
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        self._scroll_distance = list(touch.pos)
