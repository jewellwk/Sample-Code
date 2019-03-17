
/**
 * The CardGame class creates a child object of Game
 */
public class CardGame extends Game {

    /**
     * The number of decks of cards used
     */
    private int cards;

    /**
     * Constructor
     *
     * @param name The name of the game
     * @param max The maximum number of players
     * @param min The minimum number of players
     */
    public CardGame(String name, int max, int min, int cards) {
        super(name, max, min);
        this.cards = cards;
    }

    /**
     * The getCards method returns the number of decks of cards used
     *
     * @return The number of decks of cards used
     */
    public int getCards() {
        return cards;
    }

    /**
     * The setCards method sets the number of decks of cards used
     *
     * @param cards The number of decks of cards used
     */
    public void setCards(int cards) {
        this.cards = cards;
    }

    /**
     * Overridden toString that displays method in parent class and the type of
     * ball used.
     *
     * @return The name of the game, minimum number of players, maximum number
     * of players and the number of decks used
     */
    @Override
    public String toString() {
        return "Name of the game: " + getName()
                + "\nMinimum number of players: " + getMin()
                + "\nMaximum number of players: " + getMax()
                + "\nThe number of decks used: " + getCards();
    }
}
