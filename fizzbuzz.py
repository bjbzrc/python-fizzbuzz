# Final code for the IT 4320 FizzBuzz challenge
# By Brandon Buttlar

def main():
    for i in range(1,101):
        fizz = 'Fizz' if i % 3 == 0 else ''
        buzz = 'Buzz' if i % 5 == 0 else ''
        
        print(f'{fizz}{buzz}' or i)
        
        
main()
