def main():
    programming_classes = ('Intro to Python','Advanced Python','Database Essentials','Web Development Basics','Data Structures in Python','Web Design Fundamentals')
    print("Programming Certificate Classes:\n")
    for course in programming_classes:
        print(course)
    print("\nThere are", len(programming_classes), "classes in total.")

main()