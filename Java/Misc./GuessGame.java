/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.Scanner;
import java.util.Random;

/**
 *
 * @author JewellWright
 */
public class GuessGame {

    /**
     * @param args the command line arguments
     */
    static int count = 0;
    static Random num = new Random();

    public static void main(String[] args) {
        // the guessing game
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to the guessing game.\n"
                + "\nI will choose a number between 1 and 100 ... "
                + "and you try to guess it."
                + "\nWith each guess, "
                + "I will tell you whether you are too high or too low."
                + "\nThe objective is to find the number using as few guesses as"
                + " possible. \nYou only have six guesses."
                + "\nI'm thinkging of a number between 1 and 100.");

        int number = num.nextInt(101);
        game(number);

        System.out.println("\nDo you want to play again?: (y/n)");
        char answer;
        answer = input.next().charAt(0);

        if (answer == 'y' || answer == 'Y') {
            number = num.nextInt(101);
            count = 0;
            game(number);
        } else {
            System.out.println("Goodbye.");
            System.exit(0);
        }
    }

    public static void game(int number) {
        Scanner input = new Scanner(System.in);

        if (count == 6) {
            System.out.println("You lose. The number was: " +number );
            System.out.println("\nDo you want to play again?: (y/n)");
            char answer;
            answer = input.next().charAt(0);

            if (answer == 'y' || answer == 'Y') {
                number = num.nextInt(101);
                count = 0;
                game(number);
            } else {
                System.out.println("Goodbye.");
                System.exit(0);
            }
        } else {

            System.out.println("\nEnter guess (or -1 to quit):");

            int guess = 0;

            if (input.hasNextInt()) {
                guess = input.nextInt();

                if (guess < 0) {
                    System.out.println("Goodbye.");
                    System.exit(0);

                } else if (guess > number) {
                    System.out.println("Too High");
                    count++;
                    game(number);

                } else if (guess < number) {
                    System.out.println("Too low");
                    count++;
                    game(number);

                } else if (guess == number) {
                    System.out.println("You win. You got it in "+(count+1)+" guesses.");

                }

            } else {
                System.out.println("Invalid input");
                game(number);
            }
        }

    } 

}
