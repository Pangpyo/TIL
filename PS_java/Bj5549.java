// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N, M, K;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());
        char[][] map = new char[N][];

        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
        }

        int[][][] cntMap = new int[N+1][M+1][3];

        Map<Character, Integer> check = new HashMap<>();
        check.put('J', 0);
        check.put('O', 1);
        check.put('I', 2);

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                cntMap[i][j][check.get(map[i-1][j-1])] += 1;
                for (int k = 0; k < 3; k++) {
                    cntMap[i][j][k] += cntMap[i-1][j][k] + cntMap[i][j-1][k] - cntMap[i-1][j-1][k];
                }
            }
        }

        int sx, sy, ex, ey, temp;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            sx = Integer.parseInt(st.nextToken());
            sy = Integer.parseInt(st.nextToken());
            ex = Integer.parseInt(st.nextToken());
            ey = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 3; j++) {
                temp = cntMap[ex][ey][j] - cntMap[ex][sy-1][j] - cntMap[sx-1][ey][j] + cntMap[sx-1][sy-1][j];
                sb.append(temp).append(" ");
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}