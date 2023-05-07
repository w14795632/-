height = input("請輸入身高:")
weight = input("請輸入體重:")

height = int(height)
weight = int(weight)

height = height/100

bmi =  weight /height/ height

if bmi < 18.5:
	print("你的BMI為:", bmi, "有點過輕囉!多吃一點吧!")

elif bmi >= 18.5 and bmi < 24:
	print("你的BMI為:", bmi, "很棒，繼續維持") 

elif bmi >= 24 and bmi < 27:
	print("你的BMI為:", bmi, "有點過重囉!要注意飲食")

elif bmi >= 27 and bmi < 30:
	print("你的BMI為:", bmi, "太胖了，需要減肥!")

elif bmi >= 30 and bmi < 35:
	print("你的BMI為:", bmi, "欸，太胖了啦!")

elif bmi >= 35 :
	print("你的BMI為:", bmi, "準備叫救護車了")