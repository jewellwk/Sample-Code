
import java.util.Random;
import java.util.ArrayList;

/**
 * A class that exploits inheritance to create objects of the parent Game based
 * on each child within the Parent and then records each object into an
 * ArrayList
 */
public class GameTester {

    /**
     * The creation of an ArrayList of Game objects
     */
    private static ArrayList<Game> demo;

    /**
     * The creation of Game object
     */
    private static Game gameSelect;

    public static void main(String[] args) {
        runTest();
    }

    /**
     * The runTest method generates 5 random Game objects and then appends them
     * to an ArrayList. Last, it prints the ArrAyList.
     */
    public static void runTest() {
        demo = new ArrayList<>();
        // loop that selects 5 games
        for (int i = 0; i < 5; i++) {
            // adds game to ArrayList
            demo.add(createObj());
        }
        // gets ArrayList
        for (int i = 0; i < 5; i++) {
            System.out.println(demo.get(i) + "\n");
        }
    }

    /**
     * Method that creates a Game object based on a randomly generated number
     *
     * @return Game object
     */
    public static Game createObj() {
        // generates random number
        Random chooseGame = new Random();
        int GameChosen = chooseGame.nextInt(3);
        // generates random numbers for the parameters
        Random ranParam = new Random();
        int a = ranParam.nextInt(101);
        int b = ranParam.nextInt(101);
        int c = ranParam.nextInt(1001);  
        // initializes game based on the random number
        switch (GameChosen) {
            case 0: {
                gameSelect = new BallGame("GameOne", a, b, c);
                break;
            }
            case 1: {
                gameSelect = new DiceGame("GameTwo", a, b, c);
                break;
            }
            case 2: {
                gameSelect = new CardGame("GameThree", a, b, c);
                break;
            }
            default:
                break;
        }
        return gameSelect;
    }
}
