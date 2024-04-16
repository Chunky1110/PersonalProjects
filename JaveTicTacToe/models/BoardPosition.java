//Carson Crockett
package cpsc2150.extendedTicTacToe.models;

/**
 * This Class is used to store positions within the 5 x 8 game board
 *
 * @invariant MAX_ROW = 5 AND MAX_COL = 8
 */

public class BoardPosition {
    private int row;
    private int col;
    public static final int MAX_ROW = 5;
    public static final int MAX_COL = 8;

    /**
     * Constructor for Board position to create a position at row {@code r} and column {@code c}
     *
     * @param r Vertical component of the position
     * @param c Horizontal component of the position
     *
     * @pre 0 <= r < MAXIMUM_ROW AND 0 <= c < MAXIMUM_COL
     * @post row = r AND col = c
     */
    public BoardPosition(int r, int c)
    {
        row = r;
        col = c;
    }

    /**
     * Return the value of the row {@code row}
     *
     * @return returns the value of the row {@code row}
     *
     * @post row = #row AND col = #col
     */
    public int getRow()
    {
        return row;
    }

    /**
     * Returns the value of the column {@code col}
     *
     * @return returns the vale of the column {@code row}
     *
     * @post row = #row AND col = #col
     */
    public int getColumn()
    {
        return col;
    }

    /**
     * Overrides the equals function of Java
     *
     * @return returns true if the objects are equal and false if they are not
     *
     * @pre obj instanceof BoardPosition
     * @post row = #row AND col = #col AND return true if [obj is the same object as self]
     */
    @Override
    public boolean equals(Object obj)
    {
        if(!(obj instanceof BoardPosition))
            return false;
        BoardPosition bp  = (BoardPosition) obj;

        return (this.row == bp.row) && (this.col == bp.col);
    }

    /**
     * Overrides the toString function of Java
     *
     * @return returns a String representation of the object
     *
     * @post row = #row AND col = #col AND a string will be made in the format "row,column"
     */
    @Override
    public String toString()
    {
        String output= "";
        output += getRow();
        output += ",";
        output += getColumn();
        return output;
    }
}
