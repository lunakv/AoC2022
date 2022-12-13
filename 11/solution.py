import re
import copy

items_re = re.compile(r"Starting items: ((?:\d+, )*\d+)")
operation_re = re.compile(r"new = (.*)")
test_re = re.compile(r"divisible by (\d+)")
throw_re = re.compile(r"throw to monkey (\d+)")


class Monkey:
    RELIEF_FACTOR = 3
    ALL_DIVISOR_PRODUCT = 1

    def __init__(self):
        self.items = []
        self.operation = lambda x, y: None
        self.args = (None, None)
        self.divisibility = 0
        self.throw_on_true = -1
        self.throw_on_false = -1

        self.inspections = 0

    def parse_operation(self, operation):
        operation = operation.split()
        operator = operation[1]
        if operator == "+":
            self.operation = lambda x, y: x + y
        elif operator == "-":
            self.operation = lambda x, y: x - y
        elif operator == "*":
            self.operation = lambda x, y: x * y
        elif operator == "/":
            self.operation = lambda x, y: x // y
        else:
            raise ValueError(f'Invalid operator "{operator}"')

        for i in [0, 2]:
            if operation[i] == "old":
                operation[i] = lambda x: x
            else:
                n = int(operation[i])
                operation[i] = lambda _: n
        self.args = (operation[0], operation[2])

    def __update_threat(self, threat):
        arg1, arg2 = [arg(threat) for arg in self.args]
        return (self.operation(arg1, arg2) // Monkey.RELIEF_FACTOR) % Monkey.ALL_DIVISOR_PRODUCT

    def __throw_item(self, item) -> (int, int):
        self.inspections += 1
        threat = self.__update_threat(item)
        if threat % self.divisibility == 0:
            return self.throw_on_true, threat
        else:
            return self.throw_on_false, threat

    def take_turn(self) -> list[(int, int)]:
        thrown = [self.__throw_item(item) for item in self.items]
        self.items = []
        return thrown


def load_monkeys():
    monkeys = []
    try:
        while True:
            input()  # "Monkey n:"
            monkey = Monkey()
            monkeys.append(monkey)
            items = items_re.search(input()).group(1)
            monkey.items = [int(num) for num in items.split(", ")]
            operation = operation_re.search(input()).group(1)
            monkey.parse_operation(operation)
            divis = test_re.search(input()).group(1)
            monkey.divisibility = int(divis)
            Monkey.ALL_DIVISOR_PRODUCT *= int(divis)
            on_true = throw_re.search(input()).group(1)
            monkey.throw_on_true = int(on_true)
            on_false = throw_re.search(input()).group(1)
            monkey.throw_on_false = int(on_false)
            input()  # empty line
    except EOFError:
        return monkeys


def run(monkeys: list[Monkey], rounds: int) -> list[Monkey]:
    for _ in range(rounds):
        for monkey in monkeys:
            for target, item in monkey.take_turn():
                monkeys[target].items.append(item)

    return monkeys


def two_highest_inspections(monkeys: list[Monkey]) -> (int, int):
    first, second = -1, -1
    for monkey in monkeys:
        i = monkey.inspections
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i
    return first, second


monkeys = load_monkeys()
part1 = run(copy.deepcopy(monkeys), 20)
a, b = two_highest_inspections(part1)
print(a * b)

Monkey.RELIEF_FACTOR = 1
part2 = run(monkeys, 10000)
a, b = two_highest_inspections(part2)
print(a * b)
