package cpsc2150.extendedTicTacToe.models;

import java.util.HashMap;
import java.util.*;

/**
 * This class creates a Board to play tic toe to allow users to view and interact with the board
 *
 * @author Carson Crockett
 * @version 1.0
 *
 * @correspondances: self = Map<Character, List<BoardPosition>> AND [board map containting and List of positions occupied
 * by each player ]and [there are MAX_ROW number of rows] AND [there are MAX_COL number of columns] and [There are markers
 * number of markers needed in a row to win] and [there are rows # of rows and columns # of columns]
 *
 * @invariants: MAX_ROW = 100 AND MAX_COL = 100 AND MINIMUM_ROWS = 3 AND MINIMUM_COLS = 3 AND MINIMUM_NUM = 3 AND
 * MAXIMUM_NUM = 25
 */
public class GameBoardMem extends AbsGameBoard implements IGameBoard
{
    private final int rows;
    private final int columns;
    private final int markers;
    private Map<Character, List<BoardPosition>> board;

    /**Constructor for GameBoardMem that initializes board as a HashMap
     * and stores the user selected number of rows, columns, and markers required to win
     *
     * @pre r <= MAXIMUM_ROWS AND r >= MINIMUM_ROWs AND c <= MAXIMUM_COLS AND c >= MINIMUM_COLS AND markers <=
     * MAXIMUM_NOW AND markers >= MINIMUM_NUM
     *
     * @post board = [An empty map] AND rows = r AND columns = c AND markers = M
     *
     * @param r the number of rows selected to be in the board
     * @param c the number of columns selected to be in the board
     * @param m the number of markers in a row selected to be required to win
     */
    public GameBoardMem(int r, int c, int m) {
        rows = r;
        columns = c;
        markers = m;
        board = new HashMap<>();
    }

    public char whatsAtPos(BoardPosition pos) {
        char c = emptySpace;
        for(Map.Entry<Character, List<BoardPosition>> m : board.entrySet()) {
            List<BoardPosition> temp = m.getValue();
            if(temp.contains(pos))
                c = m.getKey();
        }
        return c;
    }

    @Override
    public boolean isPlayerAtPos(BoardPosition pos, char player) {
        List<BoardPosition> temp;
        if(!board.containsKey(player))
            return false;
        else {
            temp = board.get(player);
            return temp.contains(pos);
        }
    }

    public void placeMarker(BoardPosition marker, char player) {
        List<BoardPosition> temp = new ArrayList<>();
        if(!board.containsKey(player))
        {
            temp.add(marker);
            board.put(player,temp);
        }
        else
            board.get(player).add(marker);
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
