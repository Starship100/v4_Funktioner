def pretty_print(pretty_list):

    if not pretty_list:
        print("Tom lista.")

    list_length = len(pretty_list)
    print("Antal element: " + str(list_length))

    for elements in pretty_list:
        print(f"* {elements}")



pretty_print(["a", "b", "c"])