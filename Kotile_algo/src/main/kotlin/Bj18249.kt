// 18249 욱제가 풀어야 하는 문제 S2

fun main() {
    val T = readln()!!.toInt()
    var answer = IntArray(T)
    val MAX = 200_000
    var dp = IntArray(MAX)
    val MOD = 1_000_000_000 + 7
    dp[0] = 1
    dp[1] = 1
    for (i in 2 until MAX){
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    }
    for (t in 0 until T){
        val N = readln()!!.toInt()
        answer[t] = dp[N]
    }
    print(answer.joinToString("\n"))
}