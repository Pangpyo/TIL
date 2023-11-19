import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static class XY implements Comparable<XY>{
        int X;
        int Y;

        public XY(int x, int y) {
            this.X = x;
            this.Y = y;
        }
        @Override
        public String toString() {
            return this.X + " " + this.Y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            XY xy = (XY) o;
            return X == xy.X && Y == xy.Y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(X, Y);
        }

        @Override
        public int compareTo(XY o) {
            return this.X != o.X ? this.X - o.X : this.Y - o.Y;
        }
    }

    static XY plus (XY s1, XY s2) {
        return new XY(s1.X + s2.X, s1.Y + s2.Y);
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int M = Integer.parseInt(br.readLine());

        XY[] starSet = new XY[M];
        XY xy;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            xy = new XY(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            starSet[i] = xy;
        }
        int N = Integer.parseInt(br.readLine());
        Set<XY> stars = new HashSet<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            xy = new XY(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            stars.add(xy);
        }
        int sx = starSet[0].X;
        int sy = starSet[0].Y;
        XY nStar, diff;
        boolean flag;
        for (XY star : stars) {
            flag = true;
            diff = new XY(star.X - sx, star.Y-sy);
            for (XY s : starSet) {
                nStar = plus(diff, s);
                if (!stars.contains(nStar)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                System.out.println(diff);
                break;
            }
        }
    }
}