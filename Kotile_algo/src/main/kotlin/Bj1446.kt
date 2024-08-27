import kotlin.math.min

// 1446 지름길 S2

fun main() {
    val (n, d) = readln()!!.split(" ").map { it.toInt() }
    val roads = Array(n){ readln()!!.split(" ").map { it.toInt() }.toIntArray() }
    var dp = IntArray(10001)
    for (i in 1..10000){
        dp[i] = dp[i-1] + 1
        for (road in roads){
            if (road[1] == i)
                dp[i] = min(dp[i], dp[road[0]] + road[2])
        }
    }
    print(dp[d])
}