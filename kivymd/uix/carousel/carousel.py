import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    StringProperty,
    OptionProperty,
    NumericProperty,
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
        self.radius = [10] * 4


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
    desired_item_size = NumericProperty(120)

    _strategy = None
    _container = None
    _distance_scroll = NumericProperty(0.0)
    _variable_item_size = dp(50) 

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.bind(data=self.update_strategy)
        self.bind(size=self.update_strategy)
        self.bind(ids=self.set_container)

    def set_container(self, *args):
        self._container = self.ids._container

    def fit_count(self, type_item, child_count):
        suitable_count = getattr(self._strategy, f"{type_item}_count")
        #if type_item == "large":
            #if (self.width-dp(32))/getattr(self._strategy, f"{type_item}_size") <= suitable_count:
            #    suitable_count -= self._strategy.small_count - self._strategy.medium_count -1 
        return range(suitable_count)

    def set_init_size(self, *arg):
        predicted_size = (self._strategy.large_count*self._strategy.large_size) + (self._strategy.medium_count*self._strategy.medium_size) + (self._strategy.small_count*self._strategy.small_size)
        
        print(predicted_size)
        print(self.size,self._strategy, len(self._container.children))

        child_count = len(self._container.children)
        if child_count < (
            self._strategy.small_count
            + self._strategy.medium_count
            + self._strategy.large_count
        ):
            return
        index = 0
        for type_item in ["large", "medium", "small"]:
            item_size = getattr(self._strategy, f"{type_item}_size")
            for widget_index in (
                self.fit_count(type_item, child_count)
            ):
                widget = self._container.children[::-1][index]
                widget.width = item_size
                index += 1
        
    def on__distance_scroll(self, instance, distance):
        pass

    def update_strategy(self, *args):
        self._strategy = AvaliableStrategies.get(self.strategy).arrange(
            self.width, self.desired_item_size, len(self.data)
        )
        Clock.schedule_once(self.set_init_size)
        return self._strategy

    _last_touch_point = [0, 0]

    def on_touch_down(self, touch):
        self._last_touch_point = list(touch.pos)
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        self._distance_scroll = touch.pos[0] - self._last_touch_point[0]
