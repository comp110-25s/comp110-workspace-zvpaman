"""
This code calculates the requirements and costs for hosting a cozy tea party. It
includes functions to determine the number of tea bags, treats, and the total cost.
"""

__author__: str = "730466088"


def tea_bags(people: int) -> int:
    """
    Calculates the number of tea bags needed for the given number of people. This is
    based on each person requiring two tea bags.
    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculates the number of treats needed for the given number of people. Each person
    is estimated to consume 1.5 treats, which is calculated using the number of tea
    bags required.
    """
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculates the total cost of tea bags and treats. Tea bags cost $0.50 each, and
    treats cost $0.75 each. The total is the sum of these costs.
    """
    return (tea_count * 0.5) + (treat_count * 0.75)


def main_planner(guests: int) -> None:
    """
    Plans a tea party by calculating the required tea bags, treats, and the total cost.
    It then prints these details in a formatted summary.
    """
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)):.2f}"
    )


if __name__ == "__main__":
    """
    Executes the main block to prompt the user for the number of guests and then plans
    the tea party by calling the main_planner function.
    """
    guests = int(input("Enter the number of guests: "))
    main_planner(guests=guests)
