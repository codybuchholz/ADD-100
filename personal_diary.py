def main():
     date_time = input("Enter the current date and time: ") 
     entry = input("Enter your diary entry: ") 
     diary_file = open('diary.txt', 'a') 
     diary_file.write(date_time + '\n') 
     diary_file.write(entry + '\n') 
     diary_file.write('\n') 
     diary_file.close() 
     main()