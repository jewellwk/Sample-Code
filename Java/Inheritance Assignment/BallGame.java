
/**
 * The BallGame class creates a child object of Game
 */
public class BallGame extends Game {

    /**
     * The number of balls used
     */
    private int numBalls;

    /**
     * Constructor
     *
     * @param name The name of the game
     * @param max The maximum number of players
     * @param min The minimum number of players
     */
    public BallGame(String name, int max, int min, int numBalls) {
        super(name, max, min);
        this.numBalls = numBalls;
    }

    /**
     * The getNumBalls method returns the number of balls used
     *
     * @return The number of balls used
     */
    public int getNumBalls() {
        return numBalls;
    }

    /**
     * The setNumballs method sets the number of balls used
     *
     * @param NumBalls Number of balls used
     */
    public void setNumBalls(int NumBalls) {
        this.numBalls = NumBalls;
    }

    /**
     * Overridden toString that displays method in parent class and the number
     * of balls used.
     *
     * @return The name of the game, the minimum and maximum number of players
     * and the type of ball used
     */
    @Override
    public String toString() {
        return "Name of the game: " + getName()
                + "\nMinimum number of players: " + getMin()
                + "\nMaximum number of players: " + getMax()
                + "\nThe number of balls used: " + getNumBalls();
    }
}
