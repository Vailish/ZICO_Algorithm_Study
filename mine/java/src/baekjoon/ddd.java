package baekjoon;

// dfs를 통해서 연결된 모든 수를 합한 뒤
// answer에 넣어주고 오름차순으로 정렬
class ddd {
    int days;
    void dfs(int[] location, boolean[][] visited, String[] maps){
        int r = location[0];
        int c = location[1];
        days += maps[r][c];

        // 델타이동
        for (int i=0; i<4; i++) {
            int newR = r + {-1, 1, 0, 0}[i];
            int newC = c + {0, 0, -1, 1}[i];

            if (
                    0 <= newR && newR < maps.length &&
                            0 <= newC && newC < maps[0].length() &&
                            visited[newR][newC] == false &&
                            !String.valueOf(maps[newR].charAt(newC)).equals('X'
                            ) {
                dfs({newR, newC}, visited, maps);
            }
        }
    }

    public int[] solution(String[] maps) {
        int r = maps.length;
        int c = maps[0].length();
        int[] answer = {};

        // visited 생성
        boolean[][] visited = new boolean[r][c];
        for (int i=0; i<r; i++) {
            for (int j=0; j<c; j++) {
                visited[i][j] = false;
            }
        }

        // dfs 실행
        for (int i=0, i<r; i++) {
            for (int j=0; j<c; j++) {
                days = 0;
                if (visited[i][j] == false) {
                    dfs({i, j}, visited, maps);
                    answer += days;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        solution
    }
}