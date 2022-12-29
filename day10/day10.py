from utils.utils import Utils


class Day10(Utils):
    result: int
    cycle: int
    crt_row: str

    def __init__(self):
        super().__init__()

    def part_one(self):
        x = 1
        self.cycle = 1
        self.result = 0

        for line in self.input:
            operation = line.split()
            self.cycle += 1
            self.__add_result(x)

            if len(operation) > 1:
                x += int(operation[1])
                self.cycle += 1
                self.__add_result(x)

        return self.result

    def part_two(self):
        x = 1
        sprite_counter = 0
        crt_counter = 0
        self.crt_row = ''

        for line in self.input:
            operation = line.split()

            if len(operation) > 1:
                for _ in range(0, 2):
                    self.__append_pixel(crt_counter, sprite_counter)
                    crt_counter += 1
                    crt_counter = self.__append_new_line(crt_counter)

                x += int(operation[1])
                sprite_counter = x
            else:
                self.__append_pixel(crt_counter, sprite_counter)
                crt_counter += 1
                crt_counter = self.__append_new_line(crt_counter)

        print(self.crt_row)
        return self.crt_row

    def __add_result(self, x):
        match self.cycle:
            case 20 | 60 | 100 | 140 | 180 | 220:
                self.result += x * self.cycle

    def __append_pixel(self, crt_counter, sprite_counter):
        if crt_counter in range(sprite_counter - 1, sprite_counter + 2):
            self.crt_row += '#'
        else:
            self.crt_row += '.'

    def __append_new_line(self, crt_counter):
        if crt_counter == 40:
            self.crt_row += '\n'
            return 0

        return crt_counter


