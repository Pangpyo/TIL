import java.util.Arrays;

public class Socar2 {

    int solution(int n, int k, int[][] grid) {

        int answer = 0;

        int[][][] D = new int[n+1][n+1][11];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                for (int c = 1; c <= 10; c++) {
                    D[i][j][c] += D[i-1][j][c] + D[i][j-1][c] - D[i-1][j-1][c];
                }
                D[i][j][grid[i-1][j-1]] += 1;
            }
        }

        for (int i = 0; i <= n; i++) {
            System.out.println(Arrays.deepToString(D[i]));
        }
        boolean flag;
        int[] temp;
        int cnt, maxCnt, diff;
        for (int w = 0; w < n; w++) {
            flag = false;
            for (int i = 1+w; i <= n; i++) {
                for (int j = 1+w; j <= n; j++) {
                    temp = new int[11];
                    cnt = 0;
                    maxCnt = 0;
                    for (int c = 1; c <= 10; c++) {
                        temp[c] += D[i][j][c] - D[i-w-1][j][c] - D[i][j-w-1][c] + D[i-w-1][j-w-1][c];
                    }
                    for (int c = 1; c <= 10; c++) {
                        cnt += temp[c];
                        maxCnt = Math.max(maxCnt, temp[c]);
                    }
                    diff = cnt - maxCnt;
                    if (diff <= k) {
                        answer = w+1;
                        flag = true;
                    }
                }
            }
            if (!flag) break;
        }

        return answer;

    }

    public static void main(String[] args) {

        Socar2 socar2 = new Socar2();
        System.out.println(socar2.solution(3, 2, new int[][] {{1, 2, 2, 2}, {1, 2, 1, 1}, {1, 2, 2, 1}, {3, 2, 1, 1}}));
    }
}
