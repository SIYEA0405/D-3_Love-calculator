# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small_text_name = name1.lower() + name2.lower()

true_t = small_text_name.count("t")
true_r = small_text_name.count("r")
true_u = small_text_name.count("u")
true_e = small_text_name.count("e")

love_l = small_text_name.count("l")
love_o = small_text_name.count("o")
love_v = small_text_name.count("v")
love_e = small_text_name.count("e")

name_true = true_t + true_r + true_u + true_e
name_love = love_l + love_o + love_v + love_e

total_score = name_true * 10 + name_love

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coka and mentos.")     
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")

    
    












