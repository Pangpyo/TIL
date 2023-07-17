import java.util.Scanner;

public class Main {

    static int N;
    static boolean flag = false;

    static int check(int n) {
        int rst = 0;
        int temp;
        while (true) {
            temp = n % 10;
            if ((rst & (1<<temp)) > 0) return -1;
            rst |= (1<<temp);
            n /= 10;
            if (n == 0) break;
        }
        return rst;
    }
    static void bt(int A, int AUsed) {
        if (flag || A >= N) return;
        int B = N-A;
        int BUsed = check(B);
        if (AUsed > 0 && BUsed > 0 && ((AUsed&BUsed) == 0 )) {
            System.out.println(A + " + " + B);
            flag = true;
            return;
        }
        for (int i=0; i<10; i++) {
            if ((AUsed & 1<<i) != 0) continue;
            bt(A*10+i, AUsed|(1<<i));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for (int i = 1; i < 10; i++) {
            bt(i, 1<<i);
        }

        if (!flag) System.out.println(-1);
    }
}