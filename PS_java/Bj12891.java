import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    static int S, P, A, C, G, T, cnt;

    static String dna;

    static HashMap<Character, Integer> ACGT = new HashMap<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());

        dna = br.readLine();

        ACGT.put('A', 0);
        ACGT.put('C', 0);
        ACGT.put('G', 0);
        ACGT.put('T', 0);

        st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        cnt = 0;
        for (int i = 0; i < S; i++) {
            ACGT.put(dna.charAt(i), ACGT.get(dna.charAt(i)) + 1);
            if (i >= P - 1) {

                if (ACGT.get('A') >= A &&
                        ACGT.get('C') >= C &&
                        ACGT.get('G') >= G &&
                        ACGT.get('T') >= T) {
                    cnt++;
                }
                ACGT.put(dna.charAt(i - P + 1), ACGT.get(dna.charAt(i - P + 1)) - 1);
            }
        }
        System.out.println(cnt);
    }
}