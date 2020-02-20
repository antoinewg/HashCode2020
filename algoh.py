def handle(lines):
    maximum_slice, num_pizzas = list(map(int, lines[0].split()))

    slices = list(map(int, lines[1].split()))

    pizzas_to_order = []
    total_slices = 0

    for pizza_number, num_slices in enumerate(slices):
        total_slices += num_slices
        if total_slices > maximum_slice:
            break
        else:
            pizzas_to_order.append(pizza_number)

    return [
        str(len(pizzas_to_order)),
        " ".join(list(map(str, pizzas_to_order)))
    ]