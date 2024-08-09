import java.util.ArrayDeque

// 5464 주차장 S2

fun main(args: Array<String>) {
    var (n, m) = readln().split(" ").map { it.toInt() }
    var fees = Array<Int>(n) { readln()!!.toInt() }
    var cars = Array<Int>(m) { readln()!!.toInt() }
    var use = Array<Boolean>(n) { false }
    var loc = Array<Int>(m) { 0 }
    var queue = ArrayDeque<Int>()
    var answer = 0
    var carIn = 0
    for (i in 1..m*2) {
        var carNum = readln()!!.toInt()
        if (carNum >= 0){
            carNum--
            queue.offer(carNum)
        }else {
            carNum = carNum * -1 - 1
            use[loc[carNum]] = false
        }
        if (!queue.isEmpty()) {
            for (j in 0 until n){
                if (!use[j]) {
                    use[j] = true
                    carIn = queue.poll()
                    loc[carIn] = j
                    answer += cars[carIn] * fees[j]
                    break
                }
            }
        }
    }
    print(answer)
}