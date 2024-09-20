import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    // static int n, m;
    // static int[][] arr;
    // static boolean[][] visited;
    // static int[][] dir = {
    //     {-1, 0}, 
    //     {1, 0},   
    //     {0, -1},  
    //     {0, 1},  
    //     {-1, -1}, 
    //     {-1, 1},  
    //     {1, -1},  
    //     {1, 1}    
    // };
    // static boolean flag;
    
    // public static void main(String[] args) throws Exception {
    //     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //     StringTokenizer st = new StringTokenizer(br.readLine());

    //     n = Integer.parseInt(st.nextToken());
    //     m = Integer.parseInt(st.nextToken());

    //     arr = new int[n][m];
    //     for (int i=0; i<n; i++) {
    //         st = new StringTokenizer(br.readLine());
    //         for (int j=0; j<m; j++) {
    //             arr[i][j] = Integer.parseInt(st.nextToken());
    //         }
    //     }

    //     int answer = 0;
    //     visited = new boolean[n][m];
    //     for (int i=0; i<n; i++) {
    //         for (int j=0; j<m; j++) {
    //             if (visited[i][j]) {
    //                 continue;
    //             }

    //             boolean flag = false;
    //             search(i, j);

    //             if (!flag) {
    //                 answer += 1;
    //                 System.out.println(i+" "+j);
    //             }
    //         }
    //     }

    //     System.out.println(answer);
    // }

    // private static void search(int x, int y) {
    //     visited[x][y] = true;

    //     for (int[] d : dir) {
    //         int nx = x + d[0];
    //         int ny = y + d[1];

    //         if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
    //             continue;
    //         }

    //         if (arr[nx][ny] > arr[x][y]) {
    //             flag = true;
    //         }

    //         if (!visited[nx][ny] && arr[nx][ny] == arr[x][y]) {
    //             search(nx, ny);
    //         }
    //     }
    // }
    static int col, row,ans;
	static int[][] map;
	static boolean[][] visited;
	static boolean pick;
	//8방 탐색 
	static int dx[]= {-1,1,0,0,1,1,-1,-1};
	static int dy[]= {0,0,-1,1,1,-1,1,-1};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		col = Integer.parseInt(st.nextToken());
		row = Integer.parseInt(st.nextToken());
		map = new int[col][row];
		visited = new boolean[col][row];
		
		for (int i = 0; i < col; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < row; j++) {			
				map[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < col; i++) {
			for (int j = 0; j < row; j++) {
				if(!visited[i][j]) {
					pick=true;
					dfs(i,j);
					if(pick)ans++;
				}
			}
		}
		
		System.out.println(ans);
	}
	private static void dfs(int x, int y) {
		visited[x][y]=true;
		for (int k = 0; k < 8; k++) {
			int xx=x+dx[k];
			int yy=y+dy[k];
			if(xx<0||yy<0|| xx>=col|| yy>=row)continue;
			//꼭대기가 아니면 값을 더하지 않기 위해 사용
			if(map[xx][yy]>map[x][y])pick=false;
			if(!visited[xx][yy]&&map[xx][yy]==map[x][y]) {
				dfs(xx,yy);
			}
		}
	}
}