'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import json

def my_function():
    x = {
        "name": "Milano Ramadely",
        "address": "Perum. Bumi Agung Permai Blok D No.18. Batu Aji, Batam",
        "is_married": False,
        "school": {"highSchool": "SMKN 1 Batam", "university": "-"},
        "hobbies": [
            "Coding",
            "Reading"
            ],
        "skills": [
            {"name": "Programming"},
            {"score": 85, "mpg": 23.8}
            ]
            
        }
    print(json.dumps(x))
    

my_function()


