// 3187 양치기 꿍 S1

var v = 0
var k = 0
val dx = arrayOf(-1, 0, 1, 0)
val dy = arrayOf(0, 1, 0, -1)
var N = 0
var M = 0
fun main() {
    var (n, m) = readln()!!.split(" ").map { it.toInt() }
    N = n
    M = m
    var V = 0
    var K = 0
    val map = Array<String>(n) { readln()!! }
    var visit = Array(n) { BooleanArray(m) { false } }
    for (i in 0 until n){
        for (j in 0 until m){
            if (!visit[i][j]){
                v = 0
                k = 0
                dfs(i, j, map, visit)
                if (v >= k)
                    V += v
                else
                    K += k
            }
        }
    }
    print("$K $V")
}

fun dfs(x:Int, y:Int, map:Array<String>, visit:Array<BooleanArray>){
    visit[x][y] = true
    if (map[x][y] == 'v'){
        v++
    }else if (map[x][y] == 'k'){
        k++
    }
    for (i in 0..3){
        var nx = x + dx[i]
        var ny = y + dy[i]
        if (nx >= N || nx < 0 || ny >= M || ny < 0)
            continue
        if (visit[nx][ny] || map[nx][ny] == '#')
            continue
        dfs(nx, ny, map, visit)
    }

}