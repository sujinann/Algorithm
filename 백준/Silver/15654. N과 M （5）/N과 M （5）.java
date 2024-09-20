import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static boolean[] visited;
    static ArrayList<Integer> list = new ArrayList<>();
    static int[] arr;
    static int n;
    static int m;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        };
        Arrays.sort(arr);
        
        visited = new boolean[n];

        dfs();
    }

    private static void dfs() {
        if (list.size() == m) {
            for (int i=0; i<m-1; i++) {
                System.out.print(list.get(i) + " ");
            }
            System.out.println(list.get(m-1));
            return;
        }
        
        for (int i=0; i<n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                list.add(arr[i]);
                dfs();
                list.remove(list.size()-1);
                visited[i] = false;
            }
        }
    }
}