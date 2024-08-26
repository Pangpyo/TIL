// 1182 부분수열의 합 S2

var answer = 0
var N1 = 0
var S = 0
var array = IntArray(0)
fun main() {
    val (n, s) = readln()!!.split(" ").map{ it.toInt() }
    N1 = n
    S = s
    val temp = readln()!!.split(" ").map{ it.toInt() }.toIntArray()
    array = temp
    combination(0, 0)
    print(answer)
}

fun combination(cnt:Int, sums:Int) {
    if (cnt > 0 && sums == S)
        answer++
    for (i in cnt until N1){
        combination(i+1, sums+array[i])
    }
}