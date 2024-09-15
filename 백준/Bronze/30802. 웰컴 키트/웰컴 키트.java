import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[6];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<6; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        int tshirt = 0;
        for (int i=0; i<6; i++) {
            if (arr[i] % t > 0){
                tshirt += 1;
            }
            tshirt += arr[i] / t;
        }

        int pen1 = n/p;
        int pen2 = n%p;

        System.out.println(tshirt);
        System.out.println(pen1 + " " + pen2);
    }
}