package olive;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class prob2 {
	public static void main(String[] args) {
		String[] kor = {"AAA", "BCD", "AAAAA", "ZY"};
		String[] usa = {"AB", "AA", "TTTT"};
		String[] incs = {"AB BCD AAA TTTT AAAAA", "BCD AAA", "AB AAA TTTT BCD", "AA AAAAA AB", "AAA AB BCD"};
		
		
		HashMap<String, HashMap<String, Integer>> korMap = new HashMap<>();
		for (String k : kor) {
			korMap.put(k, new HashMap<String, Integer>());
		}
		
		int answer = 0;
		int utemp, ktemp, k, u;
		int d = incs.length;
		String[] ups;
		ArrayList<String> upKor;
		ArrayList<String> upUsa;
		for (int i=0; i<d; i++) {
			upKor = new ArrayList<>();
			upUsa = new ArrayList<>();
			ups = incs[i].split(" ");
			for (String up : ups) {
				if (korMap.containsKey(up)) upKor.add(up);
				else upUsa.add(up);
			}
//			System.out.println(i + "번쨰");
			for (String uk : upKor) {
				utemp = 0;
				for (String uu : upUsa) {
					if (korMap.get(uk).containsKey(uu)) {
						utemp = korMap.get(uk).get(uu);
						korMap.get(uk).replace(uu, ++utemp);
					}else {
						korMap.get(uk).put(uu, 1);
						utemp = 1;
					}
//					System.out.println(uk + " : " + uu + " : " +utemp);
					answer = Math.max(answer, utemp);
				}
				
			}
		}
		
		System.out.println(answer);
	}
}
