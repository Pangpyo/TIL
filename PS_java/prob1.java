package olive;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;

public class prob1 {
	
	

	
	
	public static void main(String[] args) {
		
		String number = "00090";
		int[] nums = {-1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
		int l = number.length();
		int[] str = new int[l];
		for (int i=0; i<l; i++) {
			str[i] = number.charAt(i) - '0';
		}
		System.out.println(Arrays.toString(str));
		int[] arr = new int[l+1];
		Arrays.fill(arr, -1);
		int cnt = 0;
		int i=0;
		while (i < l){
			System.out.println(i);
			if (str[i] != arr[i]) {
				if (arr[i] == -1) {
					arr[i] = str[i];
					if(str[i] != 0) arr[i+1] = nums[str[i]];
					cnt++;
					i++;
				}else {
					arr[i] = -1;
					cnt++;
				}
			}else {
				i++;
			}
		}
		if (arr[l] != -1) {
			cnt++;
			arr[l] = -1;
		}
		System.out.println(Arrays.toString(arr));
		System.out.println(cnt);
	}
}
