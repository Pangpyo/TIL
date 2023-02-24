import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static String[] str;
    static String vowel = "aeiou";
    static int L, C;

    static void combination(int n, int cnt, int vcnt, String p) {
        if (cnt == L) {
            if (vcnt > 0)
                System.out.println(p);
            return;
        }
        int temp;
        for (int i = n; i < C; i++) {
            if (vowel.contains(str[i])) {
                temp = 1;
            } else {
                temp = 0;
            }
            if (vcnt + temp <= L - 2) {
                combination(i + 1, cnt + 1, vcnt + temp, p + str[i]);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        str = br.readLine().split(" ");
        Arrays.sort(str);
        combination(0, 0, 0, "");

    }
}