import sqlite3
import shutil
import os

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_images.db')
cursor = conn.cursor()

# Create table for storing images (BLOB and file path)
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_images (
    user_id INTEGER PRIMARY KEY,
    image BLOB,
    image_path TEXT
);
''')

# Function to store image as BLOB in the database
def store_image_blob(user_id, image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    cursor.execute("INSERT INTO user_images (user_id, image) VALUES (?, ?);", (user_id, image_data))
    conn.commit()
    print(f"Image for user {user_id} stored as BLOB.")

# Function to store image as a file path in the database
def store_image_file(user_id, image_path):
    file_name = f"{user_id}_profile_image.jpeg"
    destination_path = f"./images/{file_name}"
    
    # Ensure the directory exists
    if not os.path.exists('./images'):
        os.makedirs('./images')
    
    shutil.copy(image_path, destination_path)  # Copy image to destination folder
    cursor.execute("INSERT INTO user_images (user_id, image_path) VALUES (?, ?);", (user_id, destination_path))
    conn.commit()
    print(f"Image for user {user_id} stored as file path.")

# Function to retrieve image (as BLOB or file path)
def get_image(user_id):
    cursor.execute("SELECT image, image_path FROM user_images WHERE user_id = ?;", (user_id,))
    result = cursor.fetchone()
    
    if result:
        image_data, image_path = result
        if image_data:
            # Image is stored as BLOB, return it
            return image_data
        elif image_path:
            # Image is stored as a file path, return the file path
            return image_path
    else:
        print("No image found for this user.")
        return None

# Example usage:

# Store image as BLOB
user_id = 1
image_path = 'images/profile_image.jpeg'
  # Change this to the actual path of your image
store_image_blob(user_id, image_path)

# Store image as a file path
user_id = 2
image_path = 'images/profile_image.jpeg'
 # Change this to the actual path of your image
store_image_file(user_id, image_path)

# Retrieve image
image_data_or_path = get_image(1)  # Retrieve image for user 1
if image_data_or_path:
    print(f"Image data or path: {image_data_or_path}")

# Close the connection
conn.close()
