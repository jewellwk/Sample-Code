/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author JewellWright
 */

import java.util.Scanner;

public class ArrayData {

    private static Scanner input = new Scanner(System.in);
    private static int countInts = 0;
    private static String answer;
    private static int size;
    private static int[] fixData;
    private static int[] dataExt;
    private static int[] valData;
    private static int[] original;

    public static void main(String[] args) {
        System.out.println("This program stores whatever values you want"
                + " into an array."
                + "\nEnter 'a' to add a value or 'd' to delete a value."
                + "\nUse 'q' to quit at any time.");
        createArray();
        System.out.println("\nAre you done entering values: (Enter y/n)");
        answer = input.next().substring(0, 1).toUpperCase();
        if (answer.equals("N")) {
            while (answer.equals("N")) {
                arrayExt(original);
                System.out.println("Are you done entering values: (Enter y/n)\n");
                answer = input.next().substring(0, 1).toUpperCase();
            }
            printArray(original);
        } else {
            printArray(original);
        }
    }
//this is the method that returns the array based on user input
    public static int[] createArray() {
        size = 5;
        valData = new int[size];
        while (countInts < size) {
            System.out.println("What would you like to do?");
//the user will import a string and then the string will be broken down  
            String direct = input.next().toLowerCase();
//the if statement takes the lowercase and uppercase values and ensures the length
            if (direct.substring(0, 1).equals("a") && direct.length() > 1) {
 //this variable is the parsed Integer version of the string                
                valData[countInts] = Integer.parseInt(direct.substring(1));
//this is how I had to delete a value because Idk how to use the remove element method              
            } else if (direct.substring(0, 1).equals("d") && direct.length() > 1) {
                int delete = Integer.parseInt(direct.substring(1));
                for (int x = 0; x < countInts; x++) {
                    if (valData[x] == delete) {
                        fixData = new int[valData.length];
                        System.arraycopy(valData, 0, fixData, 0, x);
                        System.arraycopy(valData, x + 1, fixData, x, countInts - x);
                        valData = fixData;
                        countInts -= 2;
                    }
                }
            } else if (direct.substring(0, 1).equals("q")) {
                break;
            } else {
//i had to ensure that you could not break my code, although I'm sure you can               
                System.out.println("Invalid Input");
                break;
            }
            countInts++;
        }
//i needed to also keep a copy of the original array       
        original = valData;
        return valData;
    }

    public static int[] arrayExt(int[] ref) {
//this doubles the array when necessary        
        dataExt = new int[size *= 2];
//this copies the previous array into the new larger one        
        System.arraycopy(ref, 0, dataExt, 0, ref.length);
//this is the same exact code because i could not find a way to implement a method
//each time i called a method instead, the original array data was erased
        while (countInts < size) {
            System.out.println("What you you like to do?");
            String direct = input.next().toLowerCase();
            if (direct.substring(0, 1).equals("a") && direct.length() > 1) {
                dataExt[countInts] = Integer.parseInt(direct.substring(1));
            } else if (direct.substring(0, 1).equals("d") && direct.length() > 1) {
                int delete = Integer.parseInt(direct.substring(1));
                for (int x = 0; x < size; x++) {
                    if (dataExt[x] == delete) {
                        fixData = new int[dataExt.length];
                        System.arraycopy(dataExt, 0, fixData, 0, x);
                        System.arraycopy(dataExt, x + 1, fixData, x, countInts - x);
                        dataExt = fixData;
                        countInts -= 2;
                    }
                }
            } else if (direct.substring(0, 1).equals("q")) {
                break;
            } else {
                System.out.println("Invalid Input");
                break;
            }
            countInts++;
        }
//this updates the saved copy of the array        
        original = dataExt;
        return dataExt;
    }

    public static void printArray(int[] arr) {
//outputs the counter that keeps tracked of the entered values
//outputs the entered values except 0
        System.out.println("You entered " +countInts+ " value(s).");
        System.out.print("These are your value(s): ");
        for (int count = 0; count < countInts; count++) {
            System.out.print("(" +arr[count] + ")");          
        }
    }
}
