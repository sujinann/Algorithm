import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int tc=0; tc<t; tc++) {
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());

            int[][] arr = new int[k+1][n];
            for (int i=0; i<n; i++) {
                arr[0][i] = i+1;
            };

            for (int i=1; i<k+1; i++) {
                for (int j=0; j<n; j++) {
                    if (j==0) {
                        arr[i][j] = 1;
                    } else {
                        arr[i][j] = arr[i][j-1] + arr[i-1][j];
                    }
                }
            };

            System.out.println(arr[k][n-1]);
        }
        
    }
}