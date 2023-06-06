"""
Если необходимо, исправьте данный код
try {
   int d = 0;
   double catchedRes1 = intArray[8] / d;
   System.out.println("catchedRes1 = " + catchedRes1);
} catch (ArithmeticException e) {
   System.out.println("Catching exception: " + e);
}
"""



# Java
"""
public class Main {
    public static void main(String[] args) {
        int[] intArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        try {
            int d = 0;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
        }
    }
}
"""

# Python
# try:
#     d = 2

intArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    d = 2
    catchedRes1 = intArray[8] / d
    print("catchedRes1 = ", catchedRes1)
except ArithmeticError as e:
    print("Catching exception: ", e)

"""
В исходном коде не объявлен intArray, а так же d = 0 что приводит 
к "Catching exception:  division by zero" и еще я бы переименовал переменные, 
но сие не критично
"""
