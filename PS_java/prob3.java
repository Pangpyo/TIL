package olive;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class prob3 {
	
	static int convertByte(String b) {
		String ans = "";
		int l = b.length();
		char temp;
		int k = 1;
		for (int i=0; i<l; i++) {
			temp = b.charAt(i);
			if (Character.isDigit(temp)) {
				ans += temp;
			}else {
				if (temp == 'K') k = 1024;
			}
		}
		return Integer.parseInt(ans)*k;
	}
	
	public static void main(String[] args) {
		
		String[][] folders = {{"animal", "root"}, {"fruit", "root"}};
		String[][] files = {{"car", "1B", "animal"}, {"dog", "2B", "animal"}, {"apple", "4B", "fruit"}};
		String[] selected = {"animal"};
		String[] excepted = {"apple"};
		
		HashSet<String> except = new HashSet<>(Arrays.asList(excepted));
		
		HashMap<String, HashSet<String>> dir = new HashMap<>();
		HashMap<String, HashMap<String, Integer>> folder = new HashMap<>();
		
		for (String[] fs : folders) {
			for (String f : fs) {
				if (!dir.containsKey(f)) {
					dir.put(f, new HashSet<String>());
					folder.put(f, new HashMap<>());
				}
			}
			dir.get(fs[1]).add(fs[0]);
		}
		
		for (String[] file : files) {
			folder.get(file[2]).put(file[0], convertByte(file[1]));
		}
		System.out.println(dir);
		System.out.println(folder);
		
		HashSet<String> visit = new HashSet<>();
		
		ArrayDeque<String> que = new ArrayDeque<>();
		for (String fd : selected) {
			visit.add(fd);
			que.offer(fd);
		}
		String fd;
		int[] ans = {0, 0};
		while (!que.isEmpty()) {
			fd = que.poll();
			for (String file : folder.get(fd).keySet()) {
				if (except.contains(file)) continue;
				ans[1]++;
				ans[0] += folder.get(fd).get(file);
			}
			for (String nfd : dir.get(fd)) {
				if (visit.contains(nfd)) continue;
				que.offer(nfd);
			}
		}
		
		System.out.println(Arrays.toString(ans));
	}
}
