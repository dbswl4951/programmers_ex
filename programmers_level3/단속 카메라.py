'''
1. 진출 지점을 기준으로 오름차순 정렬
2. routes 배열을 반복하며 카메라의 위치가 진입 지점(route[0])보다 작은지 확인
3. 작다면 카메라가 해당 차량을 만나지 못했다는 의미이므로
 1) 카메라 추가
 2) 추가한 카메라의 위치를 차량의 진출 지점(route[1])으로 갱신

해결 방안이 잘 떠오르지 않아 다른 사람 풀이 참고.
풀이 과정은 이해 했으나, 이게 모든 케이스에서 맞다고 확신 할 수 있는지는 잘 이해가 안된다..
그리디는 항상 최적의 결과를 얻는다는 보장이 없는데 어떻게 모든 케이스에서 맞다는걸 알고 코드를 짤까??
'''

def solution(routes):
    routes.sort(key=lambda x:x[1])  #진출 차수를 기준으로 오름차순으로 정렬
    camera=-30001
    result=0
    for route in routes:
        if camera<route[0]: #3) 차량의 진입 지점이 카메라보다 앞에 있을 경우
            result+=1   #3-1) 카메라 추가
            camera=route[1] #3-2) 카메라의 위치를 차량의 진출 지점으로 갱신
    return result

#print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))