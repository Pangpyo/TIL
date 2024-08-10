
// 24445 알고리즘 수업 - 너비 우선 탐색 2 S2
fun main() {
    var (n, m, r) = readln()!!.split(" ").map { it.toInt() }
    var graph = List(n+1) { mutableListOf<Int>() }
    var visit = BooleanArray(n+1)
    for (i in 1..m){
        var (u, v) = readln()!!.split(" ").map{ it.toInt() }
        graph[u].add(v)
        graph[v].add(u)
    }
    for (i in 1..n){
        graph[i].sortDescending()
    }
    var queue = ArrayDeque<Int>()
    queue.add(r)
    var order = 0
    visit[r] = true
    var orders = IntArray(n);
    while (!queue.isEmpty()){
        var n = queue.removeFirst()
        orders[n-1] = ++order
        for (nn in graph[n]){
            if (!visit[nn]){
                queue.add(nn)
                visit[nn] = true
            }
        }
    }
    print(orders.joinToString("\n"))
}