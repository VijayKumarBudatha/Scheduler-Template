# main.py

from scheduler.scheduler_utils import is_first_weekday_evening

if is_first_weekday_evening():
    print("✅ It's the first Monday evening of the month. Proceeding with job.")
    # Call your business logic here
else:
    print("⏳ Not the first Monday evening. Skipping job execution.")