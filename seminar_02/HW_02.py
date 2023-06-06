"""
Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете
получить?
public static int sum2d(String[][] arr) {
    int sum = 0;
    for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < 5; j++) {
            int val = Integer.parseInt(arr[i][j]);
            sum += val;
        }
    }
    return sum;
}
"""

"""
1) NumberFormatException - возникает, если метод Integer.parseInt() не может 
преобразовать строку в число.

2) NullPointerException - возникает, если массив arr равен null или если один 
из его элементов равен null.

3) ArrayIndexOutOfBoundsException - возникает, если индекс элемента массива 
arr находится за пределами границ массива.

4) IndexOutOfBoundsException - возникает, если индекс элемента массива 
находится за пределами границ массива.

5) IllegalArgumentException - возникает, если в метод передан некорректный 
аргумент, который не может быть преобразован в нужный тип.
"""