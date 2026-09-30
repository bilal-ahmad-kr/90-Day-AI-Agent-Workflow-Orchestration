# File organizer automation functiond
def organize_file(filename):
    #check file extension
    extension = filename.split('.')[-1]
    # Category according to extension
    if extension == 'pdf':
        category = 'Documents'
    elif extension == 'jpg' or extension == 'png':
        category = 'Images'
    elif extension == 'mp3':
        category = 'Audio'
    else:
        category = 'Other'
    print(f"{filename} {category}")
    return category

# files
files = [
    "document.pdf",
    "image.jpg",
    "song.mp3",
    "profile.png",
    "main.py",
    "data.zip",
    "notes.pdf",
]
for file in files:
    organize_file(file)