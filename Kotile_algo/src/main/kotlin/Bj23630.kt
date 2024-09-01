import kotlin.math.pow

// 23630 가장 긴 부분 수열 구하기 S2
fun main() {
    val n = readln()!!.toInt()
    val array = readln()!!.split(" ").map { it.toInt() }
    var bitCount = IntArray(21)
    for (a in array){
        for (i in 0..20){
            if ((a and 2.0.pow(i).toInt()) > 0)
                bitCount[i] += 1
        }
    }
    print(bitCount.max())
}