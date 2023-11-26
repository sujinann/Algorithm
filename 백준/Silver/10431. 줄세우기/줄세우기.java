import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int p = Integer.parseInt(st.nextToken());
		
		for (int i=0; i<p; i++) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			
			int[] arr = new int[20];
			for (int j=0; j<20; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}
			
			int cnt = 0;
			int answer = 0;
			for (int j=1; j<20; j++) {
				cnt = 0;
				for (int k=0; k<=j-1; k++) {
					if (arr[k] > arr[j]) {
						cnt++;
					}
				}
				answer += cnt;
			}
			
			System.out.println(t +" "+ answer);
		}
	}
}
