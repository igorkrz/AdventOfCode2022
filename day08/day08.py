from utils.utils import Utils, GridCreator, Day


class Day8(Utils):
    def __init__(self):
        super().__init__()

    def part_one(self):
        grid_creator = GridCreator(self.input)
        result = 0

        for points in grid_creator.grid:
            for point in points:
                if point.has_left() and point.has_right() and point.has_top() and point.has_bottom():
                    is_visible = self.__check_top(point, Day.part_one)
                    if not is_visible:
                        is_visible = self.__check_right(point, Day.part_one)
                        if not is_visible:
                            is_visible = self.__check_bottom(point, Day.part_one)
                            if not is_visible:
                                is_visible = self.__check_left(point, Day.part_one)

                    if is_visible:
                        result += 1
                else:
                    result += 1

        return result

    def part_two(self):
        grid_creator = GridCreator(self.input)
        max_result = 0

        for points in grid_creator.grid:
            for point in points:
                if point.has_left() and point.has_right() and point.has_top() and point.has_bottom():
                    result = self.__check_top(point, Day.part_two) * \
                             self.__check_right(point, Day.part_two) * \
                             self.__check_bottom(point, Day.part_two) * \
                             self.__check_left(point, Day.part_two)

                    if result > max_result:
                        max_result = result

        return max_result

    def __check_top(self, point, part, is_visible=True):
        value = point.value
        current_point = point
        result = 0

        while current_point.has_top():
            result += 1
            if not value > current_point.top.value:
                is_visible = False
                break

            current_point = current_point.top

        match part:
            case Day.part_one:
                return is_visible
            case Day.part_two:
                return result

    def __check_right(self, point, part, is_visible=True):
        value = point.value
        current_point = point
        result = 0

        while current_point.has_right():
            result += 1
            if not value > current_point.right.value:
                is_visible = False
                break

            current_point = current_point.right

        match part:
            case Day.part_one:
                return is_visible
            case Day.part_two:
                return result

    def __check_bottom(self, point, part, is_visible=True):
        value = point.value
        current_point = point
        result = 0

        while current_point.has_bottom():
            result += 1
            if not value > current_point.bottom.value:
                is_visible = False
                break

            current_point = current_point.bottom

        match part:
            case Day.part_one:
                return is_visible
            case Day.part_two:
                return result

    def __check_left(self, point, part, is_visible=True):
        value = point.value
        current_point = point
        result = 0

        while current_point.has_left():
            result += 1
            if not value > current_point.left.value:
                is_visible = False
                break

            current_point = current_point.left

        match part:
            case Day.part_one:
                return is_visible
            case Day.part_two:
                return result
