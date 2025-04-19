from .utils.input_utils import Input_Utils

# Process: Define a function named 'test' that takes a list 'sides' representing the side lengths of a triangle
def test(sides):
    # Order the side lengths in ascending order and assign them to variables a, b, and c
    a, b, c = sorted(sides)
    
    # compute the semi-perimeter of the triangle
    s = sum(sides) / 2
    
    # Use Heron's formula to compute the area of the triangle
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    # compute the height of the triangle
    y = 2 * area / a
    
    # compute the x-coordinate of the third vertex using the Pythagorean theorem
    x = (c ** 2 - y ** 2) ** 0.5
    
    # Yield the coordinates of the vertices of the triangle as a list of lists
    return [[0.0, 0.0], [a, 0.0], [x, y]]

# initialize target list of side lengths 'sides' to the variable
sides = InputUtilities.get_number_list_interactively({"confirmText":"Sides of the triangle:"})

# Output a message indicating the operation to be performed
print("Coordinates of a triangle with the said side lengths:")

# Output the result of the test function applied to the 'sides' list
print(test(sides))