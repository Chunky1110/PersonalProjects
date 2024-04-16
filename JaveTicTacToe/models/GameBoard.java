//Carson Crockett
package cpsc2150.extendedTicTacToe.models;

/**
 * This class creates a Board to play tic toe to allow users to view and interact with the board
 *
 * @author Carson Crockett
 * @version 1.0
 *
 * @correspondances: self = board[MAX_ROW][MAX_COL] AND [board is a 2D array of characters] and [there are MAX_ROW
 * number of rows] AND [there are MAX_COL number of columns] AND [there are rows # of rows] AND [there are columns # of
 * columns] AND [it takes markers # of markers in a row to win]
 *
 * @invariants: MAX_ROW = 100 AND MAX_COL = 100 AND MINIMUM_ROWS = 3 AND MINIMUM_COLS = 3 AND MINIMUM_NUM = 3 AND
 * MAXIMUM_NUM = 25
 *
 * @parameteres: r = [number of rows for the board] AND c = [number of columns for the board] AND m = [number of markers
 * in a row required to win]
 */
public class GameBoard extends AbsGameBoard implements IGameBoard {
    private final int rows;
    private final int columns;
    private final int markers;
    private char marks[];
    private char board[][] = new char[MAXIMUM_ROWS][MAXIMUM_COLS];

    /**
     * Constructor for GameBoard that fills board 5 x 8 with blank spaces
     * @pre r <= MAXIMUM_ROWS AND r >= MINIMUM_ROWs AND c <= MAXIMUM_COLS AND c >= MINIMUM_COLS AND markers <=
     * MAXIMUM_NOW AND markers >= MINIMUM_NUM
     *
     * @post board = [A 2D array of characters with every space containing a blank space character] AND rows = r AND
     * columns = c AND markers = M
     *
     * @param r the number of rows selected to be in the board
     * @param c the number of columns selected to be in the board
     * @param m the number of markers in a row selected to be required to win
     */
    public GameBoard(int r, int c, int m)
    {
        rows = r;
        columns = c;
        markers = m;
        for(int i = 0; i < rows; i++)
            for(int j = 0; j < columns; j++)
            {
                board[i][j] = emptySpace;
            }
    }


    public char whatsAtPos(BoardPosition pos)
    {
        return board[pos.getRow()][pos.getColumn()];
    }

    public void placeMarker(BoardPosition marker, char player)
    {
        board[marker.getRow()][marker.getColumn()] = player;
    }

    public int getNumRows()
    {
        return rows;
    }

    public int getNumColumns()
    {
        return columns;
    }

    public int getNumToWin()
    {
        return markers;
    }
}