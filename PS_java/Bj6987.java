import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Bj6987 {

    static int ans;
    static int[][] res;

    static void bt(int a, int b) {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 3; j++) {
                if (res[i][j] < 0) {
                    return;
                }
            }
        }

        if (b == 6) {
            a++;
            b = a + 1;
        }
        if (a == 5) {
            ans = 1;
            return;
        }

        for (int i = b; i < 6; i++) {
            res[a][0] -= 1;
            res[i][2] -= 1;
            bt(a, b + 1);
            res[a][0] += 1;
            res[i][2] += 1;

            res[a][1] -= 1;
            res[i][1] -= 1;
            bt(a, b + 1);
            res[a][1] += 1;
            res[i][1] += 1;

            res[a][2] -= 1;
            res[i][0] -= 1;
            bt(a, b + 1);
            res[a][2] += 1;
            res[i][0] += 1;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int t = 0; t < 4; t++) {
            st = new StringTokenizer(br.readLine());
            res = new int[6][3];
            boolean flag = true;
            int sum;
            ans = 0;
            for (int i = 0; i < 6; i++) {
                sum = 0;
                for (int j = 0; j < 3; j++) {
                    res[i][j] = Integer.parseInt(st.nextToken());
                    sum += res[i][j];
                }
                if (sum != 5)
                    flag = false;
            }
            if (flag) {
                bt(0, 1);
            }
            System.out.print(ans + " ");
        }
    }
}