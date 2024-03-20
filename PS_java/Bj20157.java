import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int getGCD(int a, int b) {
        if (b == 0) {
            return 1;
        }
        if (a%b == 0) {
            return b;
        }
        return getGCD(b, a%b);
    }

    static class Drection {
        int x, y;

        public Drection(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Drection)) return false;
            Drection drection = (Drection) o;
            return x == drection.x && y == drection.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        Map<Drection, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int gcd = getGCD(Math.abs(x), Math.abs(y));
            Drection dr = new Drection(x/gcd, y/gcd);
            if (map.containsKey(dr)) {
                map.replace(dr, map.get(dr)+1);
            }else {
                map.put(dr, 1);
            }
        }
        int answer = 0;
        for (int cnt : map.values()) {
            answer = Math.max(cnt, answer);
        }
        System.out.println(answer);
    }
}