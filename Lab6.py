# Lab6
# Author: James Railey cabrera


## add in functions from test.py's test statements here to make the pytest work

def calculate_rectangle_area(length:int, width:int)->float:
    return length * width

def calculate_hypotenuse(side_a:float,side_b:float)->float:
    return(side_a**2 + side_b**2)**0.5

def is_even(number:int)->bool:
    return number % 2 == 0

def find_maximum(number1:int,number2:int)->int:
    if number1 > number2:
        return number1
    else:
        return number2
    
def grade_calculator(score:int)->str:
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"
    
    
def main():
    pass

if __name__ == "__main__":
    main()
