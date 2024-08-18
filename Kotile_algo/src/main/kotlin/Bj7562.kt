// 7562 나이트의 이동 S1

fun main() {
    val T = readln()!!.toInt()
    for (t in 1..T){
        val n = readln()!!.toInt()
        val (sx, sy) = readln()!!.split(" ").map{ it.toInt() }
        val (ex, ey) = readln()!!.split(" ").map{ it.toInt() }
        var visit = Array(n){ IntArray(n){ -1 } }
        visit[sx][sy] = 0
        var queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(sx to sy)
        val dx = arrayOf(-1, -2, -2, -1, 1, 2, 2, 1)
        val dy = arrayOf(-2, -1, 1, 2, 2, 1, -1, -2)
        while (!queue.isEmpty()){
            val (x, y) = queue.removeFirst()
            for (i in 0..7){
                var nx = x + dx[i]
                var ny = y + dy[i]
                if (nx >= n || nx < 0 || ny >= n || ny < 0)
                    continue
                if (visit[nx][ny] != -1)
                    continue
                visit[nx][ny] = visit[x][y] + 1
                queue.add(nx to ny)
            }
        }
        println(visit[ex][ey])
    }
}