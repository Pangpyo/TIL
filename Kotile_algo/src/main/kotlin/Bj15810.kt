import kotlin.math.min

// 15810 풍선 공장 S2
fun main() {
    val (n, k) = readln()!!.split(" ").map { it.toInt() }
    val array = readln()!!.split(" ").map { it.toInt() }.toIntArray()
    var s:Long = 0
    var e:Long = 1_000_000_000_000
    var answer = e
    while (s <= e){
        var m = (s + e)/2
        var cnt:Long = 0
        for (a in array)
            cnt += m/a
        if (cnt >= k){
            answer = min(answer, m)
            e = m - 1
        }else{
            s = m + 1
        }
    }
    print(answer)
}