import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Main {
    static StringBuilder sb = new StringBuilder();

    static String[] movie;

    static void recursion(int r, int c, int size) {
        int sum = 0;
        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                sum += movie[i].charAt(j) - '0';
            }
        }

        if (sum == size * size)
            sb.append("1");
        else if (sum == 0)
            sb.append("0");
        else {
            int half = size / 2;
            sb.append("(");
            recursion(r, c, half);
            recursion(r, c + half, half);
            recursion(r + half, c, half);
            recursion(r + half, c + half, half);
            sb.append(")");
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        movie = new String[N];

        for (int i = 0; i < N; i++) {
            movie[i] = br.readLine();
        }

        recursion(0, 0, N);

        System.out.println(sb);
    }
}