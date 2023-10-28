import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int s = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		int k = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		
		int mini = Integer.MAX_VALUE;
		int frog = 0;
		int len;
		
		for (int i=0; i<n; i++) {
			if (Math.abs(arr[i] - s) <= 2*k) {
				len = 2*k - Math.abs(arr[i] - s);
			}else {
				len = (Math.abs(arr[i] - s) - 2*k) * l;
			}
			
			if (len < mini) {
				mini = len;
				frog = i+1;
			}
		}
		
		System.out.println(mini + " " + frog);
	}

}
