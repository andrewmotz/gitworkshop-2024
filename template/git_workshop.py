# Edit this file

def first_n_even_integers(n):
    result = []
    for i in range(1,n*2+1):
        if i % 1 == 0:
            result.append(i)
    return result


def current_year():
    return 2023

def main():
    print(f"Welcome to the {current_year()} git workshop!")
    print(f"The first 10 even integers are: {first_n_even_integers(10)}")
    pass

if __name__ == "__main__":
    main()
