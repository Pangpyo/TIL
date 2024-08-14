import kotlin.math.max

// 20922 겹치는 건 싫어 S1
fun main() {
    val (n, k) = readln()!!.split(" ").map{ it.toInt() }
    val array = readln()!!.split(" ").map { it.toInt() }.toIntArray()
    var queue = ArrayDeque<Int>()
    var answer = 0
    var count = IntArray(100_001)
    for (a in array){
        count[a] += 1
        queue.add(a)
        while (count[a] > k && !queue.isEmpty()){
            count[queue.removeFirst()] -= 1
        }
        answer = max(answer, queue.size)
    }
    print(answer)
}