"""Calculate the powers of two, with iteration, from minimum to maximum values."""


def calculate_powers_of_two_for_loop(minimum: int, maximum: int):
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    # Leveraging your notes, the course slides, and your notes,
    # please provide a complete implementation of this function that passes
    # the test suite and produces the correct output
    for i in range(minimum, maximum):
        number = 2**i
        powers_list.append(number)
    # Make sure that this function performs the computation with a for loop
    return powers_list


def calculate_powers_of_two_while_loop(minimum: int, maximum: int):
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    i = minimum
    while i < maximum:
        number = 2**i
        powers_list.append(number)
        i += 1
    # Leveraging your notes, and the course slides,
    # please provide a complete implementation of this function that passes
    # the test suite and produces the correct output
    # Make sure that this function performs the computation with a while loop
    return powers_list
