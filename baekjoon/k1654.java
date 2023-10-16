package baekjoon;

import java.util.Scanner;

public class k1654 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();

        long maxi = 0L;
        int[] arr = new int[k];
        for (int i=0; i<k; i++){
            arr[i] = sc.nextInt();
            if (arr[i] > maxi){
                maxi = arr[i];
            }
        }

        long temp;
        if (n % k == 0){
            temp = n / k;
        }else{
            temp = n / k + 1;
        }

        long answer = maxi / temp;
        int cnt = 0;
        while (cnt < n){
            answer = maxi / temp;
            cnt = 0;
            for (int i=0; i<k; i++){
                cnt += arr[i] / answer;
            }
            temp++;
        }

        System.out.println(answer);
    }
}
