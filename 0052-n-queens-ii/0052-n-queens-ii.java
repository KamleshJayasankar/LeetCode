class Solution {
    int count = 0;
    public int totalNQueens(int n) {
        char[][] board = new char[n][n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                board[i][j] = '.';
            }
        }

        place(board, 0);

        return count;
    }

    private void place(char[][] board, int row){
        if(row == board.length){
            count++;
            return;
        }

        for(int i = 0; i < board.length; i++){
            if(safe(board, row, i)){
                board[row][i] = 'Q';
                place(board, row + 1);
                board[row][i] = '.';
            }
        }
    }
    private boolean safe(char[][] board, int row, int col){
        for(int i = row - 1; i >= 0; i--){
            if(board[i][col] == 'Q'){
                return false;
            }
        }

        for(int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--){
            if(board[i][j] == 'Q'){
                return false;
            }
        }

        for(int i = row - 1, j = col + 1; i >= 0 && j < board.length; i--, j++){
            if(board[i][j] == 'Q'){
                return false;
            }
        }

        return true;
    }
}