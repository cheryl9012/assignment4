def main():

    Fahrenheit = float(input(" \033[1;3m Enter temperature in Fahrenheit:\ 033[0m "))
    
    Celsius = (Fahrenheit - 32) * 5 / 9

    print(f"temperature : {Fahrenheit}F = {Celsius}C")

if __name__ == "__main__":
    main()