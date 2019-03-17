
/**
 * Superclass that creates a Game object
 */
abstract public class Game {

    /**
     * The name of the game
     */
    private String name;

    /**
     * The maximum number of players
     */
    private int max;

    /**
     * The minimum number of players
     */
    private int min;

    public Game(String name, int max, int min) {
        this.name = name;
        this.max = max;
        this.min = min;
    }

    /**
     * The getName method returns the name of the game
     *
     * @return The name of the game
     */
    public String getName() {
        return name;
    }

    /**
     * The getMax method returns the maximum numbers of players
     *
     * @return The maximum number of players
     */
    public int getMax() {
        return max;
    }

    /**
     * The getMin method returns the minimum number of players
     *
     * @return The minimum number of players
     */
    public int getMin() {
        return min;
    }

    /**
     * The setName method sets the name of the game
     *
     * @param name Name of the game
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * The setMax method sets the maximum number of players
     *
     * @param max Maximum number of players
     */
    public void setMax(int max) {
        this.max = max;
    }

    /**
     * The setMin method sets the minimum number of players
     *
     * @param min Minimum number of players
     */
    public void setMin(int min) {
        this.min = min;
    }

    /**
     * Overridden toString method that displays the name of the game, maximum
     * number of players and the minimum number of players.
     *
     * @return Name of game / Minimum number of players /Maximum number of
     * players.
     */
    @Override
    public String toString() {
        return "Name of the game: " + name + "\nMinimum number of players: "
                + min + "\nMaximum number of players: " + max;
    }
}
