# Dictionaries for the course info
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Loop to keep asking the user until a valid course is entered
while True:
    course_number = input("Enter a course number (e.g., CSC101, NET110): ").strip()
    
    if course_number in course_rooms:
        print(f"\nCourse Number: {course_number}")
        print(f"Room Number: {course_rooms[course_number]}")
        print(f"Instructor: {course_instructors[course_number]}")
        print(f"Time: {course_times[course_number]}")
        break
    else:
        print("Invalid course number. Please try again.\n")
