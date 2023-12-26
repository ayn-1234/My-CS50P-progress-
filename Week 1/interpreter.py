def main():
    expression = input("expression: ")
    print(math_interpreter(expression))

def math_interpreter(math):
   x,y,z = math.split(" ")
   x = float(x)
   z = float(z)

   if y == "+":
       return x + z

   elif y == "-":
       return x - z

   elif y == "*":
       return x * z

   elif y == "/" and z != 0:
       return x / z

   else:
       return "error"

main()

#completed assingment
#alhamdulliah
