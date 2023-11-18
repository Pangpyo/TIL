import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    static int charToNum(char A) {
        if (A >= 'a') {
            return A - 'a' + 26;
        }
        return A -'A';
    }

    static char numToChar(int n) {
        if (n >= 26) {
            return (char) (n + 'a' - 26);
        }
        return (char) (n + 'A');
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        char A, B;
        String temp;

        int[][] D = new int[52][52];

        for (int i = 0; i < N; i++) {
            temp = br.readLine();
            A = temp.charAt(0);
            B = temp.charAt(5);
            if (A == B) continue;;
            D[charToNum(A)][charToNum(B)] = 1;
        }
        for (int k = 0; k < 52; k++) {
            for (int i = 0; i < 52; i++) {
                for (int j = 0; j < 52; j++) {
                    if (D[i][k] == 1 && D[k][j] == 1) {
                        D[i][j] = 1;
                    }
                }
            }
        }
        int l = 0;
        for (int i = 0; i < 52; i++) {
            char now = numToChar(i);
            for (int j = 0; j < 52; j++) {
                if (D[i][j] == 0 || i == j) continue;
                sb.append(now).append(" => ").append(numToChar(j)).append('\n');
                l += 1;
            }
        }
        System.out.println(l);
        System.out.println(sb.toString().trim());
    }
}