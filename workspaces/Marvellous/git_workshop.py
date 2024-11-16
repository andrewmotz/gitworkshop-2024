# Edit this file

# should return [1,1,2,3,5... and so on
def first_n_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return [1, 1]

    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci
    return first_n_fibonacci(n - 1) + first_n_fibonacci(n - 1)

# if n=5, should return 2,4,6,8,10
def first_n_even_integers(n):
    return [num for num in range(n) if num%2==0]
#    pass

<<<<<<< HEAD
def current_year_workshop():
    return 2024
=======
def current_year():
     return 1970
>>>>>>> 69246f9 (Change year to correct year)

def main():
    print(f"Welcome to the {current_year_workshop()} git workshop!")
    print(f"The first 10 even integers are: {first_n_even_integers(10)}")
    print(f"The first 10 even fibonacci are: {first_n_fibonacci(10)}")
    pass

if __name__ == "__main__":
    main()
