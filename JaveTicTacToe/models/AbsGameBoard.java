//Carson Crockett
package cpsc2150.extendedTicTacToe.models;

public abstract class AbsGameBoard implements IGameBoard{

    /**Creates a string that contains the game board
     *
     * @return a string that contains the game board
     *
     * @post toString = [String representation of the game board] and self = #self
     */
    @Override
    public String toString()
    {
        //add indent to header row
        String output = "   ";

        //Print the header row containing the column indexes
        for(int i = 0; i < this.getNumColumns(); i++)
        {
            if(i < 10)
                output = output + " " + i + "|";
            else
                output = output + i + "|";
        }
        output = output + '\n';

        //Print header column containing the row indexes as well as each position on the board and it's contents
        for(int r = 0; r < this.getNumRows(); r++)
        {
            if(r < 10)
                output = output + " " + r;
            else
                output = output + r;
            for(int c = 0; c < this.getNumColumns(); c++)
            {
                BoardPosition pos = new BoardPosition(r,c);
                output = output + "|" + whatsAtPos(pos) + " ";
            }
            output += "|" + '\n';
        }

        return output;
    }
}
