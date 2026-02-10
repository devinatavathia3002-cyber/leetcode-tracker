// Last updated: 2/9/2026, 9:54:29 PM
class Solution {
    public int[][] transpose(int[][] matrix) {
        
        int rowLength = matrix.length;
        int colLength = matrix[0].length;
        
        int[][] newMatrix = new int[colLength][rowLength];
        
        for(int i = 0; i < colLength; i++){
            for(int j = 0; j < rowLength; j++){
                
                newMatrix[i][j] = matrix[j][i];
            }
        }
        
        return newMatrix;
    }
}