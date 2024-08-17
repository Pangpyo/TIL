// 1890 점프 S1
fun main() {
    val n = readln()!!.toInt()
    var board = Array(n) { readln()!!.split(" ").map { it.toInt() }.toIntArray() }
    var dp = Array(n) { LongArray(n) }
    dp[0][0] = 1
    for (x in 0 until n){
        for (y in 0 until n){
            if (board[x][y] == 0)
                continue
            var b = board[x][y]
            if (x + b < n)
                dp[x + b][y] += dp[x][y]
            if (y + b < n)
                dp[x][y + b] += dp[x][y]
        }
    }
    print(dp[n-1][n-1])
}