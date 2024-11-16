from datetime import datetime
def first_n_fibonacci(n):
    if n == 0 :
        return []
    if n == 1:
        return [1]
    liz = [1,1]
    y= 1
    if n < 3:
        for x in range(1,10-1):
            y += liz[x-1]
            liz.append(y)
    return liz


def first_n_even_integers(n):
   temp = []
   m = 0
   while(len(temp) < n):
        m+= 2
        temp.append(m)
   return temp

def current_year_workshop():
    return datetime.now().year

def main():
    print(f"Welcome to the {current_year_workshop()} git workshop!")
    print(f"The first 10 even integers are: {first_n_even_integers(10)}")
    print(f"The first 10 even fibonacci are: {first_n_fibonacci(10)}")
    pass

if __name__ == "__main__":
    main()
