import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long[] D = new long[101];
        D[0] = 0;
        D[1] = 1;
        D[2] = 2;
        D[3] = 3;
        D[4] = 4;
        D[5] = 5;
        for (int i = 6; i <= N; i++) {
            for (int j=2; j<i-3; j++) {
                D[i] = Math.max(D[i-j-1]*j, D[i]);
            }
        }
        System.out.println(D[N]);
    }
}