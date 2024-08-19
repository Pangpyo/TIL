import kotlin.math.max

// 25916 싫은데요 S1

fun main() {
    val (n, m) = readln()!!.split(" ").map { it.toInt() }
    val array = readln()!!.split(" ").map { it.toInt() }.toIntArray()
    var answer = 0
    var temp = 0
    var s = 0
    for (e in 0 until n){
        temp += array[e]
        while (s <= e && temp > m){
            temp -= array[s]
            s += 1
        }
        answer = max(answer, temp)
    }
    print(answer)
}