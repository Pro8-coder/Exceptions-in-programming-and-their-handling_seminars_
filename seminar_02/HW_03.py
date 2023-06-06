"""
Дан следующий код, исправьте его там, где требуется
public static void main(String[] args) throws Exception {
   try {
       int a = 90;
       int b = 3;
       System.out.println(a / b);
       printSum(23, 234);
       int[] abc = { 1, 2 };
       abc[3] = 9;
   } catch (Throwable ex) {
       System.out.println("Что-то пошло не так...");
   } catch (NullPointerException ex) {
       System.out.println("Указатель не может указывать на null!");
   } catch (IndexOutOfBoundsException ex) {
       System.out.println("Массив выходит за пределы своего размера!");
   }
}
public static void printSum(Integer a, Integer b) throws FileNotFoundException {
   System.out.println(a + b);
}
"""

# Java
"""

public static void main(String[] args) {
   try {
       int a = 90;
       int b = 3;
       System.out.println(a / b);
       printSum(23, 234);
       int[] abc = { 1, 2 };
       abc[2] = 9;
   } catch (ArithmeticException ex) {
       System.out.println("Попытка деления на ноль!");
   } catch (FileNotFoundException ex) {
       System.out.println("Файл не найден!");
   } catch (ArrayIndexOutOfBoundsException ex) {
       System.out.println("Массив выходит за пределы своего размера!");
   } catch (Exception ex) {
       System.out.println("Что-то пошло не так...");
   }
}

public static void printSum(Integer a, Integer b) {
   System.out.println(a + b);
}
"""


# Python
def main():
    try:
        a = 90
        b = 3
        print(a / b)
        print_sum(23, 234)
        abc = [1, 2]
        abc[2] = 9
    except ZeroDivisionError:
        print("Попытка деления на ноль!")
    except FileNotFoundError:
        print("Файл не найден!")
    except IndexError:
        print("Массив выходит за пределы своего размера!")
    except Exception:
        print("Что-то пошло не так...")


def print_sum(a, b):
    print(a + b)


if __name__ == "__main__":
    main()
