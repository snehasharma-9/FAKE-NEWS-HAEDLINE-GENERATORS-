import random
subjects = [
"Prime Minister",
"President",
"Famous Actor",
"Cricketer",
"Scientist",
"Tech CEO",
"School Principal",
"College Student",
"Army Officer",
"Police Commissioner",
"Doctor",
"Teacher",
"YouTuber",
"Influencer",
"Business Tycoon",
"Startup Founder",
"Film Director",
"Government Official",
"Space Scientist",
"Environmental Activist"
]

actions = [
"announces shocking decision",
"reveals secret plan",
"gets arrested",
"launches new project",
"makes controversial statement",
"wins international award",
"loses important position",
"faces serious allegations",
"breaks world record",
"introduces new policy",
"resigns unexpectedly",
"confirms major breakthrough",
"creates nationwide panic",
"surprises everyone",
"exposes hidden truth",
"claims unbelievable discovery",
"starts new movement",
"issues urgent warning",
"signs historic agreement",
"rejects popular demand"
]

places = [
"India",
"New Delhi",
"Mumbai",
"Bengaluru",
"Chennai",
"Hyderabad",
"Kolkata",
"United States",
"China",
"Japan",
"Russia",
"United Kingdom",
"Parliament",
"Supreme Court",
"Airport",
"Railway Station",
"University Campus",
"Research Lab",
"Space Center",
"Hospital",
"Village"
]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    
    headline = f"BREAKING NEWS: {subject} {action} in {place}"
    print("\n",headline)
    
    user_input = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if user_input != 'yes':
     print("Thank you for using the Fake News Headline Generator. Goodbye!")
     break
    