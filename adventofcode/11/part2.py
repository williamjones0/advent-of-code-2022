# Read input file to list
with open("input.txt", "r") as f:
    lines = f.readlines()

monkeys = [{
    "items": [],
    "operation": "",
    "test": -1,
    "true": -1,
    "false": -1,
    "inspected": 0
} for i in range(8)]

for i in range(len(lines)):
    line = lines[i].split()
    if len(line) == 0:
        continue
    elif line[0] == "Monkey":
        items = lines[i+1].split()
        for item in items:
            if item not in ["Starting", "items:"]:
                monkeys[i // 7]["items"].append(int(item.strip(",")))

        operation = lines[i+2].split()
        monkeys[i // 7]["operation"] = operation[4] + operation[5]

        test = lines[i+3].split()
        monkeys[i // 7]["test"] = int(test[3])

        true = lines[i+4].split()
        monkeys[i // 7]["true"] = int(true[5])

        false = lines[i+5].split()
        monkeys[i // 7]["false"] = int(false[5])

mod = 1
for monkey in monkeys:
    mod *= monkey["test"]

for _ in range(10000):
    for monkey in monkeys:
        # Monkey inspects item
        removed = []
        for item in monkey["items"]:
            monkey["inspected"] += 1
            original = item
            operation = monkey["operation"]
            if operation[0] == "+":
                if operation[1:] == "old":
                    item += item
                else:
                    item += int(operation[1:])
            elif operation[0] == "-":
                if operation[1:] == "old":
                    item -= item
                else:
                    item -= int(operation[1:])
            elif operation[0] == "*":
                if operation[1:] == "old":
                    item *= item
                else:
                    item *= int(operation[1:])
            elif operation[0] == "/":
                if operation[1:] == "old":
                    item /= item
                else:
                    item /= int(operation[1:])

            item %= mod
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)

            removed.append(original)

        for item in removed:
            monkey["items"].remove(item)


top = []
for monkey in monkeys:
    top.append(monkey["inspected"])

top.sort(reverse=True)
top = top[:2]

print(top[0] * top[1])
