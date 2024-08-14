import kotlin.math.max

// 18113 그르다 김가놈 S2
fun main() {
    val (n, k, m) = readln()!!.split(" ").map{ it.toInt() }
    var array = mutableListOf<Int>()
    for (i in 1..n){
        var l = readln()!!.toInt()
        if (l > 2*k)
            array.add(l - 2*k)
        else if(l < 2*k && l > k)
            array.add(l - k)
    }
    var s = 1
    var e = 1_000_000_000
    var answer = -1

    while (s <= e){
        var mid = (s+e)/2
        var cnt = 0
        for (a in array)
            cnt += a/mid
        if (cnt >= m){
            answer = max(answer, mid)
            s = mid + 1
        }else{
            e = mid - 1
        }
    }
    print(answer)
}