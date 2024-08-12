import kotlin.math.max

// 17216 가장 큰 감소 부분 수열 S2

fun main() {
    val n = readln()!!.toInt()
    val array = readln()!!.split(" ").map{ it.toInt() }.toIntArray()
    var dp = IntArray(n)
    dp[0] = array[0]
    for (i in 1 until n){
        dp[i] = array[i]
        for (j in 0 until i){
            if (array[i] < array[j])
                dp[i] = max(dp[i], dp[j] + array[i])
        }
    }
    print(dp.max())
}