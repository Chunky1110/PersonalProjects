//Carson Crockett
package cpsc2150.extendedTicTacToe.models;

/**
 * IGameBoard is a 2D array of characters serving as a board for a game of tic-tac-toe
 * Initialization ensures:
 *      The board is an empty 2D array of size between MINIMUM_ROWS by MINIMUM_COLS and MAXIUMUM_ROWS by MAXIMUM_COLS
 *      AND must be empty
 * Defines:
 *      The board will have a 2D array that stores what markers have been placed
 *      at every position on the board or if they are empty.
 *      num_rows: X
 *      num_cols: Y
 *      num_to_win: Z
 * Constraints:
 *      num_rows <= MINIMUM_ROWS AND num_rows <= MAXIMUM_ROWS AND num_cols >= MINIMUM_COLS AND num_cols <= MAXIMUM_COLS
 *      AND num_to_win <= MINIMUM_NUM AND num_to_win >= MIMINUM_NUM
 */
public interface IGameBoard {
    public static final int MAXIMUM_ROWS = 100;
    public static final int MAXIMUM_COLS = 100;
    public static final int MINIMUM_ROWS = 3;
    public static final int MINIMUM_COLS = 3;
    public static final int MINIMUM_NUM = 3;
    public static final int MAXIMUM_NUM = 25;
    public static final char emptySpace = ' ';

    /**
     * This method checks if the last move made resulted in a win
     *
     * @param lastPos An object of BoardPosition where the last marker was placed
     * @return Is true if the game is won and false otherwise
     *
     * @pre 0 <= lastPos.getRow() < MAXIMUM_ROW AND 0 <= lastPos.getCol() < MAXIMUM_COL AND
     * [lastPos is the place on the board where the latest play was made]
     * @post board = #board AND return true if [lastPos is the last in five consecutive markers vertically
     * horizontally or diagonally]
     */
    default public boolean checkForWinner(BoardPosition lastPos)
    {
        //Check if playerOne won the game
        char c = whatsAtPos(lastPos);
        if(checkVerticalWin(lastPos, c) || checkHorizontalWin(lastPos, c) || checkDiagonalWin(lastPos, c))
            return true;
        else
            return false;
    }

    /**
     * This method checks if the game has ended in a draw
     *
     * @return Is true if a draw is achieved, false otherwise
     *
     * @pre checkForWinner == false
     * @post board = #board AND returns true if [every position is occupied]
     */
    default public boolean checkForDraw()
    {
        //Boolean to store if a draw is achieved
        boolean draw = true;

        //Increment through every position on the board and check if it's empty
        //If any are not then a draw is not achieved
        for(int r = 0; r < getNumRows(); r++)
        {
            for(int c = 0; c < getNumColumns(); c++)
            {
                BoardPosition temp = new BoardPosition(r,c);
                if(checkSpace(temp))
                {
                    draw = false;
                }
            }
        }
        return draw;
    }

    /**
     * This method checks if the last move resulted in a horizontal win condition
     *
     * @param lastPos An object of BoardPosition where the last marker was placed
     * @param player The marker of the player whose move was last
     *
     * @return Is true if a horizontal win was achieved and false otherwise
     *
     * @pre 0 <=lastPos.getRow() < MAXIMUM_ROW AND 0 <= lastPos.getCol() < MAXIMUM_COL
     * @post Will return true if lastPos has 4 of the correct markers to the left and 0 to the right OR
     * 3 to the right and 1 to the left OR 2 to the left and 2 to the right OR 3 to the left and 1 to the
     * right OR 4 to the left AND board = #board
     */
    default public boolean checkHorizontalWin(BoardPosition lastPos, char player)
    {
        //Variable to store the current row to check
        int r = lastPos.getRow();
        //Variable to store number of consecutive markers
        int count = 0;
        //Counter variable to store which column we are currently checking
        int c = lastPos.getColumn();
        //Temporary BoardPosition object to store characters in to compare to player
        BoardPosition temp = new BoardPosition(r,c);

        while(isPlayerAtPos(temp,player)) {
            count++;
            if(c == (this.getNumColumns() - 1))
                break;
            else {
                c++;
                temp = new BoardPosition(r, c);
            }
        }

        count--;
        r = lastPos.getRow();
        c = lastPos.getColumn() ;
        temp = new BoardPosition(r,c);
        while(isPlayerAtPos(temp,player) && c >= 0) {
            count++;
            if(c == 0)
                break;
            else {
                c--;
                temp = new BoardPosition(r, c);
            }
        }

        return count >= this.getNumToWin();
    }

    /**
     * This method checks if the last move resulted in a vertical win condition
     *
     * @param lastPos An object of BoardPosition where the last marker was placed
     * @param player The marker of the player whose move was last
     *
     * @return Is true if a vertical win was achieved and false otherwise
     *
     * @pre 0 <=lastPos.getRow() < MAXIMUM_ROW AND 0 <= lastPos.getCol() < MAXIMUM_COL
     * @post Will return true if lastPos has 4 of the correct markers above and 0 below OR 3 above and 1
     * below OR 2 above and 2 below OR  3 below and 1 above OR 4 below and 0 above AND board = #board
     */
    default public boolean checkVerticalWin(BoardPosition lastPos, char player)
    {
        //Variable to store the current column to check
        int c = lastPos.getColumn();
        //Variable to store number of consecutive markers
        int count = 0;
        //Counter variable to store which row we are currently checking
        int r = lastPos.getRow();
        //Temporary BoardPosition object to store characters in to compare to player
        BoardPosition temp = new BoardPosition(r,c);

        while(isPlayerAtPos(temp,player)) {
            count++;
            if(r == (this.getNumRows() - 1))
                break;
            else {
                r++;
                temp = new BoardPosition(r, c);
            }
        }

        count--;
        r = lastPos.getRow();
        c = lastPos.getColumn();
        temp = new BoardPosition(r,c);
        while(isPlayerAtPos(temp,player)) {
            count++;
            if (r == 0)
                break;
            else {
                r--;
                temp = new BoardPosition(r, c);
            }
        }

        return count >= this.getNumToWin();
    }

    /**
     * This method checks if the last move resulted in a diagonal win condition
     *
     * @param lastPos An object of BoardPosition where the last marker was placed
     * @param player The marker of the player whose move was last
     *
     * @return Is true if a diagonal win was achieved and false otherwise
     *
     * @pre 0 <=lastPos.getRow() < MAXIMUM_ROW AND 0 <= lastPos.getCol() < MAXIMUM_COL
     * @post Will return true if lastPos has 4 of the correct markers above to the right and 0 below and to the left OR
     * 3 above and to the right and 1 below and to the left OR 2 above and to the right and 2 below and to the left OR
     * 1 above to the right and 3 below and left OR 0 above and right and 4 below and left OR
     * lastPos has 4 of the correct markers above to the left and 0 below and to the right OR
     * 3 above and to the left and 1 below and to the right OR 2 above and to the left and 2 below and to the right OR
     * 1 above to the left and 4 below and right Or 0 above and right and 4 below and right
     */
    default public boolean checkDiagonalWin(BoardPosition lastPos, char player) {
        //Declare integers to store the row and column of lastPos
        int r = lastPos.getRow();
        int c = lastPos.getColumn();
        //Variable to count the number of consecutive player markers
        int count = 0;
        //Boolean to store whether a win is achieved
        boolean win = false;

        //Count the number of markers in the North East direction
        BoardPosition pos = new BoardPosition(r, c);
        while (isPlayerAtPos(pos, player)) {
            count++;
            r--;
            c++;
            pos = new BoardPosition(r, c);
            //End the loop if we get to the end of the board
            if (r < 0 || r >= getNumRows())
                break;
            if (c < 0 || c >= getNumColumns())
                break;
        }
        //Reset the position to one place South West and start counting in that direction
        count--;
        r = lastPos.getRow() ;
        c = lastPos.getColumn();
        pos = new BoardPosition(r, c);
        while (isPlayerAtPos(pos, player)) {
            count++;
            r++;
            c--;
            pos = new BoardPosition(r, c);
            //End the loop if we get to the end of the board
            if (r < 0 || r >= getNumRows())
                break;
            if (c < 0 || c >= getNumColumns())
                break;
        }
        //A win is achieved if the count is >= the number in a row required to win
        if(count >= getNumToWin()) {
            win = true;
        }

        //Reset the count in preparation to check the NW/SE diagonal
        count = 0;
        //Reset the position to lastPos
        r = lastPos.getRow();
        c = lastPos.getColumn();
        pos = new BoardPosition(r,c);
        //Count the number of markers in the North West direction
        while (isPlayerAtPos(pos, player)) {
            count++;
            r--;
            c--;
            pos = new BoardPosition(r, c);
            //End the loop if we get to the end of the board
            if (r < 0 || r >= getNumRows())
                break;
            if (c < 0 || c >= getNumColumns())
                break;
        }
        //Reset the position to one place South East and start counting in that direction
        count--;
        r = lastPos.getRow();
        c = lastPos.getColumn() ;
        pos = new BoardPosition(r,c);
        while(isPlayerAtPos(pos,player))
        {
            count++;
            r++;
            c++;
            pos = new BoardPosition(r,c);
            //End the loop if we get to the end of the board
            if(r < 0 || r >= getNumRows())
                break;
            if(c < 0 || c >= getNumColumns())
                break;
        }
        //A win is achieved if the count is >= the number in a row required to win
        if(count >= getNumToWin()) {
            win = true;
        }

        return win;
    }

    /**
     * This method checks if a player occupies a position on the board
     *
     * @param pos An object of BoardPosition with the location to be checked
     * @param player The marker of the player to compare to the one stored at pos
     *
     * @return Is true if player occupies the space at pos and is false otherwise
     *
     * @pre 0 <= pos.getRow() < MAXIMUM_ROW AND 0 <= pos.getCol() < MAXIMUM_COL
     * @post board = #board AND return true if whatAtPos(pos) == player
     */
    public default boolean isPlayerAtPos(BoardPosition pos, char player) {
        return whatsAtPos(pos) == player;
    }

    /**
     * This method checks if a space is available for a player to put
     * a marker in or if it already has one stored in it
     *
     * @param pos An object of BoardPosition to be checked
     *
     * @return Is true if the space is empty and false if space is occupied or out of bounds
     *
     * @pre 0 <= pos.getRow() < MAXIMUM_ROW AND 0 <= pos.getCol() < MAXIMUM_COL AND [whatAtPos returns an empty spot]
     * @post board = #board AND [returns true if space is empty and false if it is occupied]
     */
    default public boolean checkSpace(BoardPosition pos)
    {
        return (whatsAtPos(pos) == emptySpace);
    }

    /**
     * This method places a players marker in a passed space on the board
     *
     * @param marker An object of BoardPosition to indicate where the market should be placed
     * @param player A marker of the player whose turn was last
     *
     * @pre checkSpace(marker) == true
     * @post board[marker.getRow()][marker.getCol()] = char AND [self - marker = #self - marker]
     */
    public void placeMarker(BoardPosition marker, char player);

    /**
     * This method tells the user which player has claimed a space or if it is unclaimed
     *
     * @param pos An object of BoardPosition to be checked
     *
     * @return The marker stored in pos
     *              Either an 'X', 'O', or ' '
     *
     * @pre 0 <= pos.getRow() < MAXIMUM_ROW AND 0 <= pos.getCol() < MAXIMUM_COL
     * @post board = #board AND [the returned value will be one of the two players markers]
     */
    public char whatsAtPos(BoardPosition pos);

    /**This method returns the number of rows on the board
     *
     * @return the number of rows on the bard
     *
     * @post getRows = MAXIMUM_ROWS board = #board
     */
    public int getNumRows();

    /**This method returns the number of columns on the board
     *
     * @return the number of columns on the board
     *
     * @post getRows = MAXIMUM_COLS AND board = #board
     */
    public int getNumColumns();

    /**This method returns the number of markers in a row required to win the game
     *
     * @return the number of markers in a row required to win
     *
     * @post getNumToWin = numToWin AND board = #board
     */
    public int getNumToWin();
}
