
import java.util.Scanner;

public class NQUEENAPNACOLLEGE {
    static int solution = 0;

    public static boolean isSafe(char board[][], int row, int col) {
        // vertical up
        for (int i = row - 1; i >= 0; i--) {
            if (board[i][col] == 'Q') {
                return false;

            }
        }

        // left diagonal up
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;

            }

        }
        // right diagonal up
        for (int i = row - 1, j = col + 1; i >= 0 && j < board.length; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;

    }

    public static void NQueens(char board[][], int row) {
        if (row == board.length) {
            solution++;
            System.out.println("Solution " + solution + ":");
            printBoard(board);
            return;

        }
        // column loop

        for (int j = 0; j < board.length; j++) {
            if (isSafe(board, row, j)) {
                board[row][j] = 'Q';
                NQueens(board, row + 1);// function call
                board[row][j] = 'X';// backtracking step

            }

        }

    }

    public static void printBoard(char board[][]) {
        System.out.println("-------Chess board-------");

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();

        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter No of Queen: ");

        int n = sc.nextInt();

        char board[][] = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = 'X';

            }

        }
        NQueens(board, 0);
        if (solution == 0) {
            System.out.println("No solutions found.");

        } else {
            System.out.println("total solutions " + solution);

        }

        sc.close();

    }

}
