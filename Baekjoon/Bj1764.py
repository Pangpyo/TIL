# 1764 듣보잡 S4

import sys

sys.stdin = open('input.txt')

a, b = map(int, input().split())

ns = []
nl = []
nsnl = []
for i in range(a) :
    ns.append(input())
for i in range(b) :
    nl.append(input())

nsnl = list(set(ns).intersection(nl))

nsnl.sort()
print(len(nsnl), *nsnl, sep = '\n')