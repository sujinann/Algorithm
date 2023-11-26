import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		
		String standard = br.readLine();
		
		int answer = 0;
		
		for (int i=1; i<n; i++) {
			int[] alphabet = new int[26];
			for (int j=0; j<standard.length(); j++) {
				int idx = standard.charAt(j) - 'A';
				alphabet[idx]++;
			}
			
			String str = br.readLine();
			int cnt = 0;
			for (int j=0; j<str.length(); j++) {
				int idx = str.charAt(j) - 'A';
				if (alphabet[idx] > 0) {
					alphabet[idx]--;
					cnt++;
				}
			}
			
			if (standard.length() == str.length() && (cnt == standard.length() || cnt+1 == standard.length() )) {
				answer++;
			} else if (standard.length()-1 == str.length() && cnt == str.length()) {
				answer++;
			} else if (standard.length()+1 == str.length() && cnt == standard.length()) {
				answer++;
			}
		}
		
		System.out.println(answer);
	}
}
