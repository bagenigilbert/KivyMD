import math
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivymd.uix.carousel.arrangement import Arrangement


class CarouselStrategy:
    small_size_min = dp(40)
    small_size_max = dp(56)

    def on_first_child_measured_with_margins(carousel: Widget, child: Widget):
        pass

    def get_child_mask_percentage(
        masked_size: float, unmasked_size: float, child_margins: float
    ):
        return 1 - ((masked_size - child_margins) / (unmasked_size - child_margins))

    @staticmethod
    def double_counts(count: list):
        doubled_count = list()
        for i in range(len(count)):
            doubled_count[i] = count[i] * 2
        return doubled_count

    @staticmethod
    def clamp(value, min_val=0, max_val=0):
        return min(max(value, min_val), max_val)

    def is_contained(self):
        return True

    def should_refresh_key_line_state(self, carousel: Widget, old_item_count: int):
        return False

    def set_small_item_size_min(self, min_small_item_size: float):
        self.small_size_min = min_small_item_size

    def set_small_item_size_max(self, max_small_item_size: float):
        self.small_size_max = max_small_item_size


class MultiBrowseCarouselStrategy(CarouselStrategy):
    SMALL_COUNTS = [1]
    MEDIUM_COUNTS = [1, 0]

    def on_first_child_measured_with_margins(self, carousel: Widget, child: Widget):
        available_space = carousel.height if carousel.is_horizontal else carousel.width
        measured_child_size = child.height if carousel.is_horizontal else child.width
        small_child_size_min = self.small_size_min
        small_child_size_max = max(self.small_size_max, small_child_size_min)
        target_large_child_size = min(measured_child_size, available_space)
        target_small_child_size = self.clamp(
            measured_child_size / 3, small_child_size_min, small_child_size_max
        )
        target_medium_child_size = (
            target_large_child_size + target_small_child_size
        ) / 2
        small_counts = self.SMALL_COUNTS
        if available_space < small_child_size_min * 2:
            small_counts = [0]
        medium_counts = self.MEDIUM_COUNTS

        if carousel.alignment == "center":
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
            large_count_max - i for i in range(large_count_max - large_count_min + 1)
        ] 
        arrangement = Arrangement.find_lowest_cost_arrangement(
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

        keyline_count = arrangement.get_item_count()
        print( len(carousel.children) )
        if self.ensure_arrangement_fits_item_count(arrangement, len(carousel.children)):
            arrangement = Arrangement.find_lowest_cost_arrangement(
                available_space,
                target_small_child_size,
                small_child_size_min,
                small_child_size_max,
                [arrangement.small_count],
                target_medium_child_size,
                [arrangement.medium_count],
                target_large_child_size,
                [arrangement.large_count],
            )

        return arrangement

    def ensure_arrangement_fits_item_count(
        self, arrangement: Arrangement, carousel_item_count: int
    ):
        keyline_surplus = arrangement.get_item_count() - carousel_item_count
        changed = keyline_surplus > 0 and (
            arrangement.small_count > 0 or arrangement.medium_count > 1
        )
        while keyline_surplus > 0:
            if arrangement.small_count > 0:
                arrangement.small_count -= 1
            elif arrangement.medium_count > 1:
                arrangement.medium_count -= 1
            keyline_surplus -= 1
        return changed

    def should_refresh_keyline_state(carousel: Widget, old_item_count: int):
        return (
            old_item_count < keyline_count
            and carousel.get_item_count() >= keyline_count
        ) or (
            old_item_count >= keyline_count
            and carousel.get_item_count() < keyline_count
        )
