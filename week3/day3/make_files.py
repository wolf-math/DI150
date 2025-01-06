import os

base_dir = "schedule"

for week in range(1, 6):
    week_dir = os.path.join(base_dir, f"week{week}")
    os.makedirs(week_dir, exist_ok=True)
    
    for day in range(1, 6):
        day_dir = os.path.join(week_dir, f"day{day}")
        os.makedirs(day_dir, exist_ok=True)
        
        lesson_dir = os.path.join(day_dir, "lesson")
        homework_dir = os.path.join(day_dir, "homework")
        os.makedirs(lesson_dir, exist_ok=True)
        os.makedirs(homework_dir, exist_ok=True)

print(f"Directory structure created under {base_dir}")
