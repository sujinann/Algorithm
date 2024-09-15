import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] arr = new int[3];
            for (int i=0; i<3; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }

            if (arr[0] + arr[1] + arr[2] == 0){
                break;
            }

            Arrays.sort(arr);

            if (Math.pow(arr[0], 2) + Math.pow(arr[1], 2) == Math.pow(arr[2], 2)) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}