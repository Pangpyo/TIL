import java.util.Arrays;

public class Socar1 {
    public int solution(int n, int[] orders) {

        int[] bookStack = new int[n+1];
        Arrays.fill(bookStack, -1);
        int index = 1;
        bookStack[0] = 0;
        for (int i = 0; i < n*2; i++) {
            if (bookStack[orders[i]] == -1) {
                bookStack[orders[i]] = index++;
            }
        }
        tree = new int[n+1];
        for (int i = 1; i <= n; i++) {
            add(i, 2);
        }
        int answer = 0;
        int mod = 1000000000;
        for (int order : orders) {
            System.out.println(order);
            answer = (int) (answer + sum(bookStack[order]-1)) % mod;
            add(bookStack[order], -1);
        }

        return answer;
    }

    static int[] tree;

    long sum(int index) {
        long result = 0;
        while (index > 0) {
            result += tree[index];
            index &= (index-1);
        }
        return result;
    }

    void add(int index, int value) {
        while (index < tree.length) {
            tree[index] += value;
            index += (index & -index);
        }
    }

    public static void main(String[] args) {
        Socar1 socar1 = new Socar1();
        System.out.println("answer :" + socar1.solution(3, new int[] {1, 2, 1, 3, 3, 2}));



    }
}
