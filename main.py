def area(side):
    """Calculates the area of a square.

  Args:
      side: The length of a side of the square.

  Returns:
      The area of the square.
  """

    return side ** 2


side = float(input("Enter the side of the square: "))
area = area(side)
print("The area of the square is", area)