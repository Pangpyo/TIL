import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Bj11067 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        int N, M;
        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            List<Integer>[] cafe = new ArrayList[100001];
            Arrays.setAll(cafe, i -> new ArrayList<>());
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                cafe[Integer.parseInt(st.nextToken())].add(Integer.parseInt(st.nextToken()));
            }
            int preY = 0;
            List<int[]> answer = new ArrayList<>();
            int l;
            for (int i = 0; i < 100001; i++) {
                if (cafe[i].isEmpty()) continue;
                Collections.sort(cafe[i]);
                l = cafe[i].size();
                if (cafe[i].get(0) == preY) {
                    for (int j = 0; j < l; j++) {
                        answer.add(new int[] {i, cafe[i].get(j)});
                    }
                    preY = cafe[i].get(l-1);
                }else {
                    for (int j = l-1; j >= 0; j--) {
                        answer.add(new int[] {i, cafe[i].get(j)});
                    }
                    preY = cafe[i].get(0);
                }
            }

            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            int[] temp;
            for (int i = 0; i < M; i++) {
                temp = answer.get(Integer.parseInt(st.nextToken())-1);
                sb.append(temp[0]).append(" ").append(temp[1]).append("\n");

            }

        }
        System.out.println(sb);

    }
}
