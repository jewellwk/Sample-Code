
import java.util.ArrayList;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author JewellWright
 */
public class ArrayListData {
//so much easier than using an array. you're cruel for the first assignment
    static Scanner input = new Scanner(System.in);
    static ArrayList<String> data = new ArrayList<>();
    static int count = 5;
    static int countadj;
//instructions
    public static void main(String[] args) {
        System.out.println("This program stores whatever values you want"
                + " into an array list."
                + "\nEnter 'a' to add a value or 'd' to delete a value."
                + "\nEnter 'q' to quit at any time.\n");
        adjustList();
        extList();
    }
//method that extends your list
    public static void extList() {
        System.out.println("Do you need to make more changes? (y/n)");
        String answer = input.next().toUpperCase();
//as long as you input Yes the loop will call the adjustList method to accept inputs        
        while (answer.substring(0, 1).equals("Y")) {
//the count starts with 5 values then doubles as you need more            
            count *= 2;
            adjustList();
            System.out.println("Do you need to make more changes?");
            answer = input.next().toUpperCase();
        }
//outputs the values and number of values once the user is done making changes        
        System.out.println("You entered " + countadj + " values.");
        System.out.println("These are you values: " + data);
    }
//method that allows you to make adjustments to your data
    public static void adjustList() {
        for (countadj = 0; countadj < count; countadj++) {
            System.out.println("What would you like to do?");
            String task = input.next().toLowerCase();
            if (task.substring(0, 1).equals("a") && task.length() > 1) {
//adds a value               
                data.add(task.substring(1));
            } else if (task.substring(0, 1).equals("d") && task.length() > 1) {
//deletes a value and then adjusts the count                
                data.remove(task.substring(1));
                countadj -= 2;
            } else if (task.substring(0, 1).equals("q")) {
                break;
            } else {
//avoiding sabotage                
                System.out.println("Invalid request. Try again.");
                countadj--;
            }
        }
    }
}
