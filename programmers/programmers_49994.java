class programmers_4994 {

    static boolean[][][] visited = new boolean[11][11][4];
    static int[][] direction = {{0, 1}, // U, D, L, R
            {-1, 0},
            {0, -1},
            {1, 0}};

    public static int directToInt(char c) {
        return switch (c) {
            case 'U' -> 0;
            case 'D' -> 2;
            case 'L' -> 1;
            default -> 3;
        };
    }

    public static int solution(String dirs) {
        int answer = 0;

        int x = 0, y = 0;
        for (int i = 0; i < dirs.length(); i++) {
            int idx = directToInt(dirs.charAt(i));
            int after_idx = (idx + 2) % 4;
            int dx = x + direction[idx][0];
            int dy = y + direction[idx][1];
            if (dx >= -5 && dx <= 5 && dy >= -5 && dy <= 5) {
                if (!visited[x + 5][y + 5][idx]
                        && !visited[dx + 5][dy + 5][after_idx]) {
                    answer++;
                }
                visited[x + 5][y + 5][idx] = true;

                x = dx;
                y = dy;
            }
        }

        return answer;
    }
}