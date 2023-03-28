import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
        
		Queue<int[]> que = new ArrayDeque<>();
		
		Set<Integer> set = new HashSet<>();
		Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
		que.offer(new int[] {N, 0});
		int[] nd;
		int n, d, nn;
        if (N==1) {
			System.out.println(0);
			return;
		}
		while (!que.isEmpty()) {
			nd = que.poll();
			n = nd[0];
			d = nd[1];
			if (n%3 == 0) {
				nn = n/3;
				if (nn == 1) {
					System.out.println(d+1);
					return;
				}
				if (!set.contains(nn)) {
					que.offer(new int[] {nn, d+1});
					set.add(nn);
				}
				
			}
			if (n%2==0){
				nn = n/2;
				if (nn == 1) {
					System.out.println(d+1);
					return;
				}
				if (!set.contains(nn)) {
					que.offer(new int[] {nn, d+1});
					set.add(nn);
				}
			}
			nn = n-1;
			if (nn == 1) {
				System.out.println(d+1);
				return;
			}
			if (!set.contains(nn)) {
				que.offer(new int[] {nn, d+1});
				set.add(nn);
			}
		}
		
	}
}
