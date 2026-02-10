// Last updated: 2/9/2026, 9:53:54 PM
class Solution {
    public char[][] rotateTheBox(char[][] box) {

        int row = box.length;
        int col = box[0].length;

        //first create a falling effect
        
        for (int i = 0; i < row; i++) {
            for (int j = col - 2; j >= 0; j--) {
                if (box[i][j] == '#' && box[i][j+1] == '.') {
                    int savedj = j;
                    j++;
                    while (j < col && box[i][j] == '.') j++;
                    j--;
                    box[i][savedj] = '.';
                    box[i][j] = '#';
                }
            }
        }
        
        //then turn grid by 90 degrees
        char[][] rotate = new char[col][row];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                rotate[j][i] = box[row - 1- i][j];
            }
        }

        return rotate;
    }
}