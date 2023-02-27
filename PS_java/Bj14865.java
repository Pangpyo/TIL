package com.ssafy.live15;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class algo2 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int out = 0; // 어떤것에도 포함되지 않는 봉우리
		int in = 0; // 아무것도 포함하지 않는 봉우리
		int N = Integer.parseInt(br.readLine());
		
		long x, y, px, py, side;

		int[][] d = new int[N][2];
		List<long[]> list = new ArrayList<>();
		int min = Integer.MAX_VALUE;
		int idx = 0;
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			d[i][0] = Integer.parseInt(st.nextToken());
			d[i][1] = Integer.parseInt(st.nextToken()); 
			if (d[i][1] < 0 && d[i][0] <= min) {
				if (d[i][0] == min) {
					if (d[i][1] > d[idx][1]) continue;
				}
				min = d[i][0];
				idx = i;
			}
		}
		
		boolean flag = false;
		side = 0;
		py = 0;
		int k;
		for (int j=0; j <= N; j++) {
			k = (idx+j)%N;
			x = d[k][0];
			y = d[k][1]; 
			if (py*y < 0) { // 직전에 들어온 점과 y축 부호가 다르면 봉우리 만들기 시작
				if(!flag) { // 봉우리를 만들고 있지 않았다면
					flag = true; // flag를 true
					side = x; // 첫 점을 지정
				} else { // 봉우리를 만들고 있었던 경우
					flag = false; // 봉우리 만들기 종료
					list.add(new long[] {Math.min(side, x), Math.max(side, x)}); // 새 봉우리를 스택에 add
				}
			}
			py = y;
		}
		
		Collections.sort(list, new Comparator<long[]>() {
			@Override
			public int compare(long[] o1, long[] o2) {
				// TODO Auto-generated method stub
				return (int) (o1[0]-o2[0]);
			}
		});
		
		Stack<long[]> stack = new Stack<>();
		
		for(int i=0; i<list.size(); i++) {
			x= list.get(i)[0];
			y = list.get(i)[1];
			flag = false;
			while (true) {
				if (stack.isEmpty()) {
					out++;
					break;
				}
				px = stack.peek()[0];
				py = stack.peek()[1];
				if (px < x && y < py) {
					break;
				}else {
					stack.pop();
					flag = true;
				}
			}
			if (flag) in++;
			stack.add(list.get(i));
		}

		if (!stack.isEmpty()) in++; // 처리하지 않은 마지막 봉우리 처리
		System.out.println(out + " " + in);
		
	}
}

