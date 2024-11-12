# Edit this file

def first_ten_even_integers():
    result = []
    for i in range(1,50):
        if i % 2 == 0:
            result.append(i)
    return result


def current_year():
    return 2022

def main():
    print(f"Welcome to the {current_year()} git workshop!")
    print(f"The first 10 even integers are: {first_ten_even_integers()}")

if __name__ == "__main__":
    main()
