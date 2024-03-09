import math

from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.clock import Clock

from kivymd.uix.carousel.arrangement import Arrangement


class CarouselStrategy:
    small_size_min = dp(40) + dp(8)  # dp(8) -> spacing
    small_size_max = dp(56) + dp(8)

    _container = None
    item_len = 0
    arrangement = None 

    def __init__(self, item_len, _container):
        self.item_len = item_len
        self._container = _container

    def arrange(
        self,
        alignment: str,
        available_space: int,
        measured_child_size: int,
        item_len: int,
    ) -> Arrangement:
        """Build arrangement based on size"""

    def set_init_size(self, *arg) -> None:
        """Set size of visible widgets initially"""

    def tranform_widgets(
        self,
        touch_distance,
        scroll,
    ) -> None:
        """Shift sizes as per scroll and touch distance"""

    @staticmethod
    def double_counts(count: list):
        doubled_count = []
        for i in count:
            doubled_count.append(i * 2)
        return doubled_count

    @staticmethod
    def clamp(value, min_val=0, max_val=0):
        return min(max(value, min_val), max_val)


class MultiBrowseCarouselStrategy(CarouselStrategy):
    small_counts = [1]
    medium_counts = [1, 0]

    def arrange(
        self,
        alignment: str,
        available_space: int,
        measured_child_size: int,
    ) -> Arrangement:
        # append default padding
        measured_child_size += dp(8)
        
        small_child_size_min = self.small_size_min
        small_child_size_max = max(self.small_size_max, small_child_size_min)
        target_large_child_size = min(measured_child_size, available_space)
        target_small_child_size = self.clamp(
            measured_child_size / 3, small_child_size_min, small_child_size_max
        )
        target_medium_child_size = (
            target_large_child_size + target_small_child_size
        ) / 2
        small_counts = self.small_counts
        if available_space < small_child_size_min * 2:
            small_counts = [0]
        medium_counts = self.medium_counts

        if alignment == "center":
            small_counts = self.double_counts(small_counts)
            medium_counts = self.double_counts(medium_counts)

        min_available_large_space = (
            available_space
            - (target_medium_child_size * max(medium_counts))
            - (small_child_size_max * max(small_counts))
        )
        large_count_min = max(1, min_available_large_space // target_large_child_size)
        large_count_max = math.ceil(available_space / target_large_child_size)
        large_counts = [
            large_count_max - i
            for i in range(int(large_count_max - large_count_min + 1))
        ]
        self.arrangement = Arrangement.find_lowest_cost_arrangement(
            available_space,
            target_small_child_size,
            small_child_size_min,
            small_child_size_max,
            small_counts,
            target_medium_child_size,
            medium_counts,
            target_large_child_size,
            large_counts,
        )

    def set_init_size(self, *arg):
        if len(self._container.children) < (
            self.arrangement.small_count
            + self.arrangement.medium_count
            + self.arrangement.large_count
        ):
            # Reset the size and then retry
            for widget in self._container.children:
                widget.width = self.arrangement.large_size - dp(30)
            Clock.schedule_once(self.set_init_size)
            return

        item_index = 0
        for type_item in ["large", "medium", "small"]:
            for _ in range(getattr(self.arrangement, "{}_count".format(type_item))):
                widget = self._container.children[::-1][item_index]
                widget.width = getattr(
                    self.arrangement, "{}_size".format(type_item)
                ) - dp(8)
                item_index += 1

    def tranform_widgets(
        self,
        touch_distance,
        scroll,
    ):
        print(touch_distance, scroll * self._container.width)
        touch_distance = touch_distance/10
        children = self._container.children[::-1]
        

class AvaliableStrategies:
    avaliable = ["MultiBrowseCarouselStrategy"]

    @staticmethod
    def get(strategy_name, item_len, container):
        return {
            "MultiBrowseCarouselStrategy": MultiBrowseCarouselStrategy,
        }[strategy_name](item_len, container)
