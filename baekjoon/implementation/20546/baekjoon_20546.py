def junh(money, machine_duck_list):
  stock = 0
  left_money = money
  for day in machine_duck_list:
    n, left = divmod(left_money, day)
    if n > 0:
      stock += n
      left_money = left
  asset = stock * machine_duck_list[-1] + left_money
  return asset

def sungm(money, machine_duck_list):
    stock = 0
    left_money = money
    rise_day = 0
    drop_day = 0
    for idx, day in enumerate(machine_duck_list):
				# 3일 연속 가격이 전일 대비 상승하는 주식
        if rise_day == 3:
						# 전날 이미 전량 매도한걸로 계산
            left_money += stock * machine_duck_list[idx - 1]
						# 초기화
            stock = 0
            rise_day = 0
				# 3일 연속 가격이 전일 대비 하락하는 주식
        elif drop_day == 3 and left_money >= day:
						# 당일에 전량 매수
            n, left = divmod(left_money, day)
            if n > 0:
                stock += n
                left_money = left
						# 초기화
            drop_day = 0

        if idx >= 1:
						# 전날보다 주가가 상승했다면
            if day > machine_duck_list[idx - 1]:
                rise_day += 1
                drop_day = 0
						# 전날보다 주가가 하락했다면
            elif day < machine_duck_list[idx - 1]:
                drop_day += 1
                rise_day = 0
            else:
                rise_day = 0
                drop_day = 0

    asset = stock * machine_duck_list[-1] + left_money
    return asset


money =  int(input())
machine_duck_list = list(map(int, input().split()))

junh_money = junh(money, machine_duck_list)
sungm_money = sungm(money, machine_duck_list)

if junh_money > sungm_money:
  print("BNP")
elif junh_money < sungm_money:
  print("TIMING")
else:
  print("SAMESAME")