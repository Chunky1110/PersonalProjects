package cpsc2150.extendedTicTacToe.controllers;

import cpsc2150.extendedTicTacToe.models.*;
import cpsc2150.extendedTicTacToe.views.*;

/**
 * <p>
 * The {@link TicTacToeController} class will handle communication between our {@link TicTacToeView}
 * and our model ({@link IGameBoard} and {@link BoardPosition})
 * </p>
 *
 * <p>
 * This is where you will write code
 * <p>
 *
 * You will need to include your {@link BoardPosition} class, the {@link IGameBoard} interface
 * and both of the {@link IGameBoard} implementations from Project 4.
 * If your code was correct you will not need to make any changes to your {@link IGameBoard} implementation class.
 *
 * @version 2.0
 */
public class TicTacToeController {

    /**
     * <p>
     * The current game that is being played
     * </p>
     */
    private IGameBoard curGame;

    /**
     * <p>
     * The screen that provides our view
     * </p>
     */
    private TicTacToeView screen;

    /**
     * <p>
     * Constant for the maximum number of players.
     * </p>
     */
    public static final int MAX_PLAYERS = 10;

    /**
     * <p>
     * The number of players for this game. Note that our player tokens are hard coded.
     * </p>
     */
    private int numPlayers;

    /**
     * <p>
     *     An array of characters to represent the players markers
     * </p>
     */
    private char[] players;

    /**
     * <p>
     *     A boolean to keep track of whether or not a tie has been made or a win is achieved
     * </p>
     */
     private boolean endGame;

    /**
     * <p>
     *     An integer counter to keep track of whose turn it is
     * </p>
     */
    private int turnCount;

    /**
     * <p>
     * This creates a controller for running the Extended TicTacToe game
     * </p>
     *
     * @param model
     *      The board implementation
     * @param view
     *      The screen that is shown
     * @param np
     *      The number of players for this game.
     *
     * @post [ the controller will respond to actions on the view using the model. ]
     */
    public TicTacToeController(IGameBoard model, TicTacToeView view, int np) {
        this.curGame = model;
        this.screen = view;
        this.numPlayers = np;
        this.endGame = false;
        this.players = new char[]{'X', 'O', 'C', 'J', 'D', 'L', 'G', 'A', 'S', 'P'};
        this.turnCount = 0;
    }

    /**
     * <p>
     * This processes a button click from the view.
     * </p>
     *
     * @param row
     *      The row of the activated button
     * @param col
     *      The column of the activated button
     *
     * @post [ will allow the player to place a marker in the position if it is a valid space, otherwise it will display an error
     * and allow them to pick again. Will check for a win as well. If a player wins it will allow for them to play another
     * game hitting any button ]
     */
    public void processButtonClick(int row, int col) {
        BoardPosition bp = new BoardPosition(row, col);
        //If the space is empty place the marker
        if(curGame.checkSpace(bp)){
            curGame.placeMarker(bp,players[turnCount]);
            screen.setMarker(row,col,players[turnCount]);
            //If this is the last player, reset the turnCount and print whose turn it is
            if(turnCount == numPlayers - 1) {
                turnCount = 0;
                screen.setMessage("It is " + players[turnCount] + "'s turn");
            }
            //If this is not the last player, increase the turnCount index and print whose turn it is
            else {
                turnCount++;
                screen.setMessage("It is " + players[turnCount] + "'s turn");
            }
        }
        //If the space is unavailable inform the user and wait for next input
        else {
            screen.setMessage("That space is unavailable");
            //If this action was the one after the game was won or tied, start a new one
            if(endGame)
                newGame();
        }
        //If a win is achieved, inform the user and set endGame to true
        if(curGame.checkForWinner(bp) && !endGame){
            if(turnCount == 0)
                screen.setMessage(players[numPlayers - 1] + " wins!");
            else
                screen.setMessage(players[turnCount - 1] + " wins!");
            this.endGame = true;
        }
        //If a tie is achieved, inform the user and set endGame to true
        else if(curGame.checkForDraw() && !endGame){
            screen.setMessage("Draw!");
            this.endGame = true;
        }
        //If a win or tie has been achieved, end the game, if this is not the same turn the condition was met
        else if(endGame)
            newGame();
    }

    /**
     * <p>
     * This method will start a new game by returning to the setup screen and controller
     * </p>
     *
     * @post [ a new game gets started ]
     */
    private void newGame() {
        //close the current screen
        screen.dispose();

        //start back at the set-up menu
        GameSetupScreen screen = new GameSetupScreen();
        GameSetupController controller = new GameSetupController(screen);
        screen.registerObserver(controller);
    }
}