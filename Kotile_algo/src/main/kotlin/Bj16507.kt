// 16507 어두운 건 무서워 S1

fun main() {
    val (R, C, Q) = readln()!!.split(" ").map { it.toInt() }
    val picture = Array(R) { readln()!!.split(" ").map { it.toInt() }.toIntArray() }
    var dp = Array(R+1) { IntArray(C+1) }
    for (i in 1..R){
        for (j in 1..C){
            dp[i][j] = picture[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        }
    }
    for (q in 1..Q){
        val (sr, sc, er, ec) = readln()!!.split(" ").map { it.toInt() }
        val prefixSum = dp[er][ec] - dp[sr-1][ec] - dp[er][sc-1] + dp[sr-1][sc-1]
        val extend = (er-sr+1)*(ec-sc+1)
        println(prefixSum/extend)
    }
}