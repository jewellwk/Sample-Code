/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author JewellWright
 */
import java.util.Arrays;
import java.util.Scanner;

public class Arr2Dtrue {

    static Scanner input = new Scanner(System.in);
    static int size;
    static boolean eval;
    static boolean table[][];

    public static void main(String[] args) {   
//    main method that called the methods to carry out actions
        boolean arr2dtrue[][] = createArr();
        printArr(arr2dtrue);
        andVals(arr2dtrue);
        orVals(arr2dtrue);
        diagonal(arr2dtrue);
        antidiagonal(arr2dtrue);
    }
//method that returns a boolean 2D array based on user input
    public static boolean[][] createArr() {
        System.out.println("Enter the size: ");
        if (input.hasNextInt()) {
            size = input.nextInt();
        } else {
            System.out.println("Invalid Input. Start over.");
        }
        table = new boolean[size][size];
        for (int countrows = 0; countrows < size; countrows++) {
            for (int count = 0; count < size; count++) {
                System.out.println("Enter true or false:");
                if(input.hasNextBoolean()){
                table[countrows][count] = input.nextBoolean();
                } else {
                   break;
                }
            }
        }
        return table;
    }
    
    public static void printArr(boolean[][] compare) {
//it's not required that the array gets printed
//method that i used to print the array in order to check the code
        System.out.println(Arrays.deepToString(compare));
        System.out.println("\n");
    }

    public static void andVals(boolean[][] array) {
//The result of ANDing the values in each row
//I couldn't have the method returning eval because then it doesn't print
        for (int rows = 0; rows < size; rows++) {
            int nextVal = 1;
             while ( nextVal < size) {
                for (int count = 0; count < size; count++){ 
                    eval = array[rows][0] && array[rows][nextVal];
                }
                 if (eval == false){
                        break;
                 }
                nextVal++;
            }           
            System.out.println(eval);
        }
        System.out.println("");
    }

    public static void orVals(boolean[][] array) {
        int nextVal;
        //The result of ORing the values in each column
        for (int cols = 0; cols < size; cols++) {
                nextVal = 1;
             while ( nextVal < size) {
                for (int count = 0; count < size; count++){ 
                    eval = array[0][cols] || array[nextVal][cols];
                }
                 if (eval == true){
                        break;
                 }
                nextVal++;
            }           
            System.out.println(eval);
        }
        System.out.println("");
    }

    public static void diagonal(boolean[][] array) {
//      outputs the number of true values diagonally  
        int count = 0;
        int numTval = 0;
        while (count < size) {
            if (array[count][count] == true) {
                numTval++;
            }
            count++;
        }
        System.out.println("# of true values in the 1st diagonal: "+numTval);
    }

    public static void antidiagonal(boolean[][] array) {
//    outputs the number of true values antidiagonally
        int count = 0;
        int countbac = size - 1;
        int numTval = 0;
        while (count < size) {
            if (array[count][countbac] == true) {
                numTval++;
            }
            count++;
            countbac--;
        }
        System.out.println("# of true values in the 2nd diagonal: "+numTval);
    }
}
