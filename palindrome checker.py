print("Hello , welcome to the palindrome checker.")
stuff=input("what is your word / number ?")
stuff_reverse= stuff [::-1]
input=("Funfact= a palindrome is a word or number which appears the same from both sides , enter anything to continue ")

if stuff==stuff_reverse:
    print("Yes , your input is a palindrome.")
else:
    print("No , your input is not a palindrome.")

print("Thanks for using our tool")
input=("enter any key to exit ")