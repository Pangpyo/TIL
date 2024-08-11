import kotlin.math.max

// 16493 최대 페이지 수 S2
fun main() {
    var (n, m) = readln()!!.split(" ").map { it.toInt() }
    var books = Array(m) { readln()!!.split(" ").map { it.toInt() }.toIntArray() }
    var dp = IntArray(n+1)
    for (book in books){
        var (d, p) = book
        for (i in n downTo 1){
            if (i - d >= 0){
                dp[i] = max(dp[i-d] + p, dp[i])
            }
        }
    }
    print(dp[n])
}