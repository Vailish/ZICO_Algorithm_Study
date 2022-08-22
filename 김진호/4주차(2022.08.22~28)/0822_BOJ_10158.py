# 위, 아래 벽을 만나면 델타방향값에서 i(row)만 바뀌며
# 왼쪽, 오른쪽 벽을 만나면 델타방향값에서 j(col)만 바뀐다.
import math

w, h = map(int,input().split())             # 가로, 세로값 입력
ant_x, ant_y = map(int,input().split())     # 개미 좌표 x,y 형식으로 입력 ( == 행열이 아니라 x,y 축으로 생각하자)
t = int(input())
# loop_len = math.lcm(w, h) * 2  # 공배수 * 2?
# t = t % loop_len
x_move = t % (2*w)
y_move = t % (2*h)
if
