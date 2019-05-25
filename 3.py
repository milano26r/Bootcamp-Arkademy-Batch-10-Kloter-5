'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def count_vowels(a):
    b = 'aiueo'
    d = 0
    for c in b:
        s = a.count(c)
        d+=s
    print(d)
    
count_vowels('programmer')
count_vowels('hmm..')
