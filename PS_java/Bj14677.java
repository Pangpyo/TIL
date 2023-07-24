import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        char[] arr = sc.next().toCharArray();
        boolean[][] visit = new boolean[N*3+1][N*3+1];
        Queue<int[]> que = new ArrayDeque<>();
        que.add(new int[] {0, 0});
        visit[0][0] = true;
        char[] BLD = {'B', 'L', 'D'};
        int[] xy;
        int x, y, size;
        int time = 0;
        int ans = -1;
        while (!que.isEmpty()) {
            size = que.size();
            for (int i = 0; i < size; i++) {
                xy = que.poll();
                x = xy[0];
                y = xy[1];
                if (x + y < 3*N) {
                    if (arr[x] == BLD[time] && !visit[x+1][y]) {
                        que.add(new int[] {x+1, y});
                        visit[x+1][y] = true;
                    }
                    if (arr[3*N-1-y] == BLD[time] && !visit[x][y+1]) {
                        que.add(new int[] {x, y+1});
                        visit[x][y+1] = true;
                    }
                }
            }
            ans++;
            time = (time+1)%3;


        }
        System.out.println(ans);
    }
}