
def loop_five_turns():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break

    print(y)

# loop_five_turns()