2021.05.25
새로 추가된 기능들:
파란색 물약 -> 일정 시간 플레이어 스피드 업
노란색 물약 -> 일정 시간 플레이어 무기 데미지 증가
초록색 물약 -> 일정 시간 플레이어 무적
chest 타일 삭제(몹이 원하는 위치에서 생성되지 않아서 그냥 뺌)

settings.py
추가 물약 이미지 설정 및 TIME_LIMIT 각각 설정

main.py

def update() 코드 간결하게 가다듬음 하나의 hit 반복문 안에 아이템 먹었을때의 기능 구현 

def load_data()에다 check_time, check 변수들을 선언함 이걸로 물약을 먹었는지 안먹었는지 체크 및 먹은 시간 체크할 수 있음 
load_data에 구현한 이유는 처음 선언할때 초기화를 한 번만 해줄 수 있기 때문. update()에 선언하면 반복문을 계속돌며 초기화가 되므로 먹었는지 안먹었는지를 판단할 수 없음 각각 물약 먹었을때의 기능 추가적으로 구현