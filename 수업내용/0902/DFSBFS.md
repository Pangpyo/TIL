## DFS(깊이 우선 탐색) 개념

<img src = "https://velog.velcdn.com/images%2Flucky-korma%2Fpost%2F30737a15-9adf-49a6-96a0-98c211cab1cc%2FR1280x0.gif">

* 다음 경로로 넘어가기 전 해당 경로를 완전하게 탐색하기 위해 사용
  * ex)한 경로를 완전하게 탐색 한 후 다음 경로로 넘어가기 때문에 경로의 특징을 고려해야 하는 문제에 유용함.
  * 코드 작성이 BFS에 비해 간결한 편

* 코드 구성 : 방문 리스트를 사용하며, 방문한 노드를 재귀함수를 통해 계속해서 방문함

## BFS (너비 우선 탐색) 개념

<img src="https://velog.velcdn.com/images%2Flucky-korma%2Fpost%2F2112183b-bfcd-427e-8072-c9dc983180ba%2FR1280x0-2.gif">

* 인접한 노드를 먼저 방문하고자 할 때 주로 사용
  * 인접한 노드를 먼저 방문하기 때문에 최단거리 문제에 유용
* 큐를 사용해 구현

## 비교

<img src = "https://velog.velcdn.com/images%2Flucky-korma%2Fpost%2Fe2ef7ac3-14e6-42e7-a768-224c5f773e29%2FR1280x0-3.gif">