def pack_and_bill(order: list, prices: dict):
    # small box can contain up to 100 balls and the large box can contain up to 500 balls.
    # order requires multiple boxes, the priority lies with having the smallest possible number of boxes.
    #  calculate how many large and small boxes are necessary to ship the order, as well as the total price of the order (rounded to two decimal places). It should then return these three numbers as a tuple.

    # all balls
    total_balls = sum(order)

    # quantities
    large = 500
    small = 100

    # prices:
    ball_price = prices["ball"]
    small_box_price = prices["smallbox"]
    large_box_price = prices["largebox"]

    # counts
    large_box_count = 0

    small_box_count = 1 if remaining_balls > 0 else 0

    if total_balls > 500:
        large_box_count += total_balls // large
        remaining_balls = large_box_count % large
    elif total_balls <= 100:
        

    # total price
    total_price = round(total_ball_price + total_box_price, 2)

    return (large_box_count, small_box_count, total_price)


prices = {
    "ball":     0.20,
    "smallbox": 4.50,
    "largebox": 7.50
}

print(pack_and_bill([1], prices))
# 0 large boxes, 1 small box, total price 4.50 + 0.20 * 1
# print(pack_and_bill([1], prices) == (0, 1, 4.70))
# 1 large box, 0 small boxes, total price 7.50 + 0.20 * 500
# print(pack_and_bill([500], prices) == (1, 0, 107.50))
# print(pack_and_bill([600], prices) == (1, 1, 132.00))
# print(pack_and_bill([601], prices) == (2, 0, 135.20))
# print(pack_and_bill([50, 500, 500], prices) == (2, 1, 229.50))
