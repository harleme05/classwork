

def convert_height(cm):
    """
    Converts height from centimeters to feet and inches.

    Args:
        cm (int/float): The height in centimeters.

    Returns:
        tuple: A tuple containing the height in (feet, inches).
    """
    total_inches = cm / 2.54
    feet = float(total_inches // 12) 
    inches = float(round(total_inches % 12,0)) 

    return (feet, inches)
    