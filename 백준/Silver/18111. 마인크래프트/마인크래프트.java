import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][m];
        int min = Integer.MAX_VALUE;
        int max = 0;

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] < min) {
                    min = arr[i][j];
                }
                if (arr[i][j] > max) {
                    max = arr[i][j];
                }
            }
        }

        int s = Integer.MAX_VALUE;
        int height = 0;
        
        for (int i=min; i<=max; i++) {
            int second = 0;
            int block = 0;

            for (int j=0; j<n; j++) {
                for (int k=0; k<m; k++) {
                    if (i > arr[j][k]) {
                        block += i - arr[j][k];
                        second += i - arr[j][k];
                    } else {
                        block -= arr[j][k] - i;
                        second += 2 * (arr[j][k] - i);
                    }
                }
            }

            if (block <= b) {
                if (second <= s) {
                    s = second;
                    height = i;
                }
            }
        }

        System.out.println(s + " " + height);
    }
}