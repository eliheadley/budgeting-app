import java.util.Scanner;
import java.io.*;
public class Main {
    public static void save(Purchase purchase){
        PrintWriter pw = null;
        try{
            File myFile = new File("C:\\Users\\elihe\\OneDrive\\projects\\expense-tracker\\purchases\\monthly-purchsases.txt");
            pw = new PrintWriter(myFile);
            pw.println(purchase); pw.flush();
        }catch(IOException e){
            System.out.println(e.getMessage());
        }finally {
            if(pw != null){
                pw.close();
            }
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int userInput = 0;
        while(userInput != 3){
            System.out.print(
            "Choose one of the following options:\n"
            + "1) Enter a new expense.\n" 
            + "2) Edit old entry.\n"
            + "3) Quit.\n"
            + "Enter option number here: ");
            userInput = sc.nextInt();
            sc.nextLine();
            if(userInput == 1){
                double amount;
                String vendor;
                String date;
                System.out.print("\nWhat was the date of the purchase (mm/dd/yyyy): ");
                date = sc.nextLine();
                System.out.print("Where was the purchase made: ");
                vendor = sc.nextLine();
                System.out.print("How much was the purchase: ");
                amount = sc.nextDouble();
                sc.nextLine();
                Purchase purchase = new Purchase(date, vendor, amount);
                save(purchase);
            }
        }
    }    
}
