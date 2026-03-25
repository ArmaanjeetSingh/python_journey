fizzbuzz = ["fizzbuzz" if x % 15 == 0 else 
            "fizz" if x % 3 == 0 else
            "buzz" if x % 5 == 0 else
            str(x) for x in range(1,10)
        ]

print(fizzbuzz)

fizzbuzz_gen = ("fizzbuzz" if x % 15 == 0 else 
            "fizz" if x % 3 == 0 else
            "buzz" if x % 5 == 0 else
            str(x) for x in range(1,10)
)
for fb in fizzbuzz:
    print(fb.center(12,'*'))