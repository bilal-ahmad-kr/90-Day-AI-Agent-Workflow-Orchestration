# Lead scoring system using if else system
email_opened = True
website_visited = True
demo_requested = False

score = 0

if email_opened:
    score +=10
if website_visited:
    score +=20
if demo_requested:
    score +=50       

# Determine lead status
if score >= 70:
    lead_status = "Hot Lead"
elif score >= 40:
    lead_status = "Warm Lead"
else:
    lead_status = "Cold Lead"

print("Score:", score)
print("Status:", lead_status)