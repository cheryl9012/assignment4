def main():
    number = float(input("\033[1;3m Enter a number:\033[0m "))  # Styled input prompt
    square = number ** 2
    print(f"The square of {number} is {square}")

if __name__ == "__main__":
    main()
