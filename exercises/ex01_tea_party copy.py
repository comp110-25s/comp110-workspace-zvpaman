"""
This code calculates the requirements and costs for hosting a cozy tea party.
It includes functions to determine the number of tea bags, treats, and the total cost.
"""

__author__: str = "730466088"


def tea_bags(people: int) -> int:
    """
    Calculates the number of tea bags needed for the given number of people.
    Each person requires two tea bags.
    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculates the number of treats needed for the given number of people.
    Each person is estimated to consume 1.5 treats.
    """
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculates the total cost of tea bags and treats.
    Tea bags cost $0.50 each, and treats cost $0.75 each.
    """
    return (tea_count * 0.5) + (treat_count * 0.75)


def main_planner(guests: int) -> None:
    """
    Plans a tea party by calculating the required tea bags, treats, and total cost,
    then prints a formatted summary.
    """
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests)):.2f}")


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
