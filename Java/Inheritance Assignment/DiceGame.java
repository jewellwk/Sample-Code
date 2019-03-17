
/**
 * The DiceGame class creates a child object of Game
 */
public class DiceGame extends Game {

    /**
     * The number of dice used
     */
    private int dice;

    /**
     * Constructor
     *
     * @param name The name of the game
     * @param max The maximum number of players
     * @param min The minimum number of players
     */
    public DiceGame(String name, int max, int min, int dice) {
        super(name, max, min);
        this.dice = dice;
    }

    /**
     * The getDice method returns the number of dice used
     *
     * @return The number of dice used
     */
    public int getDice() {
        return dice;
    }

    /**
     * The setDice method sets the number of dice used
     *
     * @param dice The number of dice used
     */
    public void setDice(int dice) {
        this.dice = dice;
    }

    /**
     * Overridden toString that displays method in parent class and the type of
     * ball used.
     *
     * @return The name of the game, the minimum and maximum number of players
     * and the number of dice used
     */
    @Override
    public String toString() {
        return "Name of the game: " + getName()
                + "\nMinimum number of players: " + getMin()
                + "\nMaximum number of players: " + getMax()
                + "\nThe number of dice used: " + getDice();
    }
}
