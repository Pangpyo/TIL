public class Bj10159 {
    public static void main(String[] args) throws  Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int u, v;
        int[][] pre = new int[N+1][N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            pre[u][v] = 1;
        }

        for (int k=1; k<=N; k++) {
            for (int i=1; i<=N; i++) {
                for (int j=1; j<=N; j++) {
                    if (i==j) continue;
                    if (pre[i][k] == 1 && pre[k][j] ==1) pre[i][j] = 1;
                }
            }
        }
        int temp;
        for (int i = 1; i <= N; i++) {
            temp = 0;
            for (int j = 1; j <= N; j++) {
                temp += pre[i][j] + pre[j][i];
            }
            sb.append(N-temp-1).append("\n");
        }
        System.out.println(sb);
    }
}