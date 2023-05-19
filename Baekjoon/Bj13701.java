// 13701 중복 제거
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.BitSet;
import java.util.StringTokenizer;
public class Bj13701 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BitSet set = new BitSet(33554432);
        StringBuilder sb = new StringBuilder();
        int num;
        while(st.hasMoreTokens()) {
            num = Integer.parseInt(st.nextToken());
            if(!set.get(num)) {
                set.set(num);
                sb.append(num).append(" ");
            }
        }
        System.out.println(sb.toString());
    }
}