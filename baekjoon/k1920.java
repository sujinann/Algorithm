package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

class k1920 {
    static int N;



    public static int bsearch(int[] arr, int key){
        int left = 0;
        int right = N-1;

        while (left <= right){
            int mid = (left + right) / 2;

            if (key < arr[mid]){
                right = mid-1;
            }else if (key > arr[mid]){
                left = mid+1;
            }else{
                return 1;
            }

        

        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        int[] arr = new int[N];
        for (int i=0; i<N; i++){
            arr[i] = sc.nextInt();
        }

        int M = sc.nextInt();

        int[] brr = new int[M];
        for (int i=0; i<M; i++){
            brr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        for (int i=0; i<M; i++){
            System.out.println(bsearch(arr, brr[i]));
        }

        // int cnt = 0;
        // for (int i=0; i<M; i++){
        //     cnt = 0;
        //     for (int j=0; j<N; j++){
        //         if (brr[i] == arr[j]){
        //             cnt++;
        //             break;
        //         }
        //     }
        //     if (cnt > 0){
        //         System.out.println(1);
        //     }else{
        //         System.out.println(0);
        //     }
        // }

        

    }

    
}
