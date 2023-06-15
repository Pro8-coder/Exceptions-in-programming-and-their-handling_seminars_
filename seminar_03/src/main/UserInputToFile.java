import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class UserInputToFile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter data: ");
        String data = scanner.nextLine();
        scanner.close();

        String[] dataArray = data.split(" ");
        if (dataArray.length != 6) {
            System.out.println("Error: Invalid number of data elements.");
            return;
        }

        String surname = dataArray[0];
        String name = dataArray[1];
        String patronymic = dataArray[2];
        String birthdateStr = dataArray[3];
        String phoneStr = dataArray[4];
        String genderStr = dataArray[5];

        LocalDate birthdate;
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy");
            birthdate = LocalDate.parse(birthdateStr, formatter);
        } catch (Exception e) {
            System.out.println("Error: Invalid date format.");
            return;
        }

        long phone;
        try {
            phone = Long.parseLong(phoneStr);
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid phone number format.");
            return;
        }

        if (!genderStr.equals("f") && !genderStr.equals("m")) {
            System.out.println("Error: Invalid gender.");
            return;
        }

        String fileName = surname + ".txt";
        String fileContent = surname + name + patronymic + birthdateStr + " " + phoneStr + genderStr;

        try {
            FileWriter writer = new FileWriter(fileName, true);
            writer.write(fileContent + "\n");
            writer.close();
            System.out.println("Data has been written to file.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
