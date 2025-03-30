# # # #1
# # # # import json

# # # # with open('3sv1.json', 'r') as file:
# # # #     data = json.load(file)

# # # # for item in data:
# # # #     if item["name"] == "falseashoka":
# # # #         item["size"] = 2.5

# # # # with open('3sv2.json', 'w') as jfile:
# # # #     json.dump(data, jfile, indent=4)

# # # # print("Done mm")









# # # #2
# # # # import json

# # # # with open('3sv1.json', 'r') as file:
# # # #     dta = json.load(file)

# # # # tree_types = []

# # # # for tree in dta:
# # # #     tree["name"] = tree.get("name")
# # # #     if tree["name"] and tree["name"] not in tree_types:
# # # #         tree_types.append(tree["name"])

# # # # print(tree_types)
# # # # print("Done mm")



# # # # ['pinkblossoms', 'coco', 'coconuttree', 'brazilianrosewood', 'dividivi', 'foxtailpalm', 'jaggerypalm', 'indiancoraltree', 'indiansandalwood', 'droopingashoka', 'jamaicancherry', 'cherryblossom', 'falseashoka', 'coconuttrre', 'yellowtrumpettree', 'bougainvillea', 'jackfruittree', 'cookpine', 'bamboo', 'ba,boo', 'bush', 'yellowtrumpet', 'bushes', 'arecapalm', 'indianalmond', 'peepaltree', 'blue trumpet vine', 'wheepingbottlebrush', 'Tree of Heaven', 'African tulip tree', 'Guava tree', 'Weeping Fig', 'Fig', 'She-oak', 'Indian Almond Tree', 'Ravenala', 'Champaka', 'Copperpod', 'coconut', 'Bougainvillea', 'Peace Lilly', 'Bamboo', 'Mango Tree', 'Norfolk Island Pine', 'Norfol Island Pine', 'Unknown']









# # # #3
# # # # import json

# # # # with open('3sv1.json', 'r') as file:
# # # #     dta = json.load(file)

# # # # for tree in dta:
# # # #     if tree["name"] == "coco":
# # # #         tree["name"] = "Coconut Tree"
# # # #     if tree["name"] == "coconuttree":
# # # #         tree["name"] = "Coconut Tree"
# # # #     if tree["name"] == "brazilianrosewood":
# # # #         tree["name"] = "Brazilian Rosewood"
# # # #     if tree["name"] == "dividivi":
# # # #         tree["name"] = "Divi Divi"
# # # #     if tree["name"] == "foxtailpalm":
# # # #         tree["name"] = "Foxtail Palm"
# # # #     if tree["name"] == "jaggerypalm":
# # # #         tree["name"] = "Jaggery Palm"
# # # #     if tree["name"] == "indiancoraltree":
# # # #         tree["name"] = "Indian Coral Tree"
# # # #     if tree["name"] == "indiansandalwood":
# # # #         tree["name"] = "Indian Sandalwood"
# # # #     if tree["name"] == "droopingashoka":
# # # #         tree["name"] = "Drooping Ashoka"
# # # #     if tree["name"] == "jamaicancherry":
# # # #         tree["name"] = "Jamaican Cherry"
# # # #     if tree["name"] == "cherryblossom":
# # # #         tree["name"] = "Cherry Blossoms"
# # # #     if tree["name"] == "falseashoka":
# # # #         tree["name"] = "False Ashoka"
# # # #     if tree["name"] == "coconuttrre":
# # # #         tree["name"] = "Coconut Tree"
# # # #     if tree["name"] == "yellowtrumpettree":
# # # #         tree["name"] = "Yellow Trumpet"
# # # #     if tree["name"] == "bougainvillea":
# # # #         tree["name"] = "Bougainvillea"
# # # #     if tree["name"] == "jackfruittree":
# # # #         tree["name"] = "Jackfruit Tree"
# # # #     if tree["name"] == "cookpine":
# # # #         tree["name"] = "Cookpine"
# # # #     if tree["name"] == "bamboo":
# # # #         tree["name"] = "Bamboo"
# # # #     if tree["name"] == "ba,boo":
# # # #         tree["name"] = "Bamboo"
# # # #     if tree["name"] == "bush":
# # # #         tree["name"] = "Bush"
# # # #     if tree["name"] == "yellowtrumpet":
# # # #         tree["name"] = "Yellow Trumpet"
# # # #     if tree["name"] == "bushes":
# # # #         tree["name"] = "Bush"
# # # #     if tree["name"] == "arecapalm":
# # # #         tree["name"] = "Areca Palm"
# # # #     if tree["name"] == "indianalmond":
# # # #         tree["name"] = "Indian Almond"
# # # #     if tree["name"] == "peepaltree":
# # # #         tree["name"] = "Peepal"
# # # #     if tree["name"] == "blue trumpet vine":
# # # #         tree["name"] = "Blue Trumpet Vine"
# # # #     if tree["name"] == "wheepingbottlebrush":
# # # #         tree["name"] = "Wheeping Bottlebrush"
# # # #     if tree["name"] == "Indian Almond Tree":
# # # #         tree["name"] = "Indian Almond"
# # # #     if tree["name"] == "coconut":
# # # #         tree["name"] = "Coconut Tree"
# # # #     if tree["name"] == "pinkblossoms":
# # # #         tree["name"] = "Pink Blossoms"
# # # #     # if tree["name"] == "Tree of Heaven":
# # # #     # if tree["name"] == "African tulip tree":
# # # #     # if tree["name"] == "Guava tree":
# # # #     # if tree["name"] == "Weeping Fig":
# # # #     # if tree["name"] == "Fig":
# # # #     # if tree["name"] == "She-oak":
# # # #     # if tree["name"] == "Ravenala":
# # # #     # if tree["name"] == "Champaka":
# # # #     # if tree["name"] == "Copperpod":
# # # #     # if tree["name"] == "coconut":
# # # #     # if tree["name"] == "Bougainvillea":
# # # #     # if tree["name"] == "Peace Lilly":
# # # #     # if tree["name"] == "Bamboo":
# # # #     # if tree["name"] == "Mango Tree":
# # # #     # if tree["name"] == "Norfolk Island Pine":
# # # #     # if tree["name"] == "Unknown":

# # # # with open('3sv2.json', 'w') as jfile:
# # # #     json.dump(dta, jfile, indent=4)

# # # # print("Done mm")

# # # # print("Done mm")








# # # #4
# # # import json
# # # import random

# # # import random

# # # def getRandomGreenShade():
# # #     g = random.randint(100, 255)  # Generate green between 100-255
# # #     r = random.randint(0, 50)     # Generate red between 0-50
# # #     b = random.randint(0, 50)     # Generate blue between 0-50
# # #     return f"rgb({r}, {g}, {b})"  # Use f-string for proper formatting

# # # with open('3sv1.json', 'r') as file:
# # #     dta = json.load(file)
    

# # # for tree in dta:
# # #     if tree["name"] == "Coconut Tree":
# # #         tree["color"] = "rgb(30, 130, 76)"  # Dark green
# # #     if tree["name"] == "Brazilian Rosewood":
# # #         tree["color"] = "rgb(53, 94, 59)"  # Deep forest green
# # #     if tree["name"] == "Divi Divi":
# # #         tree["color"] = "rgb(46, 139, 87)"  # Sea green
# # #     if tree["name"] == "Foxtail Palm":
# # #         tree["color"] = getRandomGreenShade()  # Medium sea green
# # #     if tree["name"] == "Jaggery Palm":
# # #         tree["color"] = getRandomGreenShade()  # Forest green
# # #     if tree["name"] == "Indian Coral Tree":
# # #         tree["color"] = "rgb(0, 128, 0)"  # Green
# # #     if tree["name"] == "Indian Sandalwood":
# # #         tree["color"] = "orange"  # Keeping your color
# # #     if tree["name"] == "Drooping Ashoka":
# # #         tree["color"] = getRandomGreenShade()  # Light sea green
# # #     if tree["name"] == "Jamaican Cherry":
# # #         tree["color"] = getRandomGreenShade()  # Sea green
# # #     if tree["name"] == "Cherry Blossoms":
# # #         tree["color"] = getRandomGreenShade()  # Lime green
# # #     if tree["name"] == "False Ashoka":
# # #         tree["color"] = getRandomGreenShade()  # Dark olive green
# # #     if tree["name"] == "Yellow Trumpet":
# # #         tree["color"] = "yellow"  # Olive drab
# # #     if tree["name"] == "Jackfruit Tree":
# # #         tree["color"] = "#B79400"  # Bright green
# # #     if tree["name"] == "Cookpine":
# # #         tree["color"] = "rgb(41, 106, 46)"  # Green
# # #     if tree["name"] == "Bamboo":
# # #         tree["color"] = "rgb(143, 188, 143)"  # Dark sea green
# # #     if tree["name"] == "Bush":
# # #         tree["color"] = "rgb(0,255,0)"  # Keeping your color
# # #     if tree["name"] == "Areca Palm":
# # #         tree["color"] = getRandomGreenShade()  # Medium sea green
# # #     if tree["name"] == "Indian Almond":
# # #         tree["color"] = getRandomGreenShade()  # Green
# # #     if tree["name"] == "Peepal":
# # #         tree["color"] = getRandomGreenShade()  # Forest green
# # #     if tree["name"] == "Blue Trumpet Vine":
# # #         tree["color"] = "blueviolet"  # Keeping your color
# # #     if tree["name"] == "Wheeping Bottlebrush":
# # #         tree["color"] = getRandomGreenShade()  # Sea green
# # #     if tree["name"] == "Pink Blossoms":
# # #         tree["color"] = "palevioletred"  # Keeping your color
# # #     if tree["name"] == "Tree of Heaven":
# # #         tree["color"] = getRandomGreenShade()  # Dark green
# # #     if tree["name"] == "African tulip tree":
# # #         tree["color"] = getRandomGreenShade()  # Dark olive green
# # #     if tree["name"] == "Guava tree":
# # #         tree["color"] = getRandomGreenShade()  # Medium sea green
# # #     if tree["name"] == "Weeping Fig":
# # #         tree["color"] = getRandomGreenShade()  # Forest green
# # #     if tree["name"] == "Fig":
# # #         tree["color"] = getRandomGreenShade()  # Sea green
# # #     if tree["name"] == "She-oak":
# # #         tree["color"] = getRandomGreenShade()  # Green
# # #     if tree["name"] == "Ravenala":
# # #         tree["color"] = getRandomGreenShade()  # Medium sea green
# # #     if tree["name"] == "Champaka":
# # #         tree["color"] = getRandomGreenShade()  # Sea green
# # #     if tree["name"] == "Copperpod":
# # #         tree["color"] = getRandomGreenShade()  # Bright green
# # #     if tree["name"] == "Bougainvillea":
# # #         tree["color"] = "red"  # Keeping your color
# # #     if tree["name"] == "Peace Lilly":
# # #         tree["color"] = "white"  # Keeping your color
# # #     if tree["name"] == "Mango Tree":
# # #         tree["color"] = getRandomGreenShade()  # Green
# # #     if tree["name"] == "Norfolk Island Pine":
# # #         tree["color"] = getRandomGreenShade()  # Dark green
# # #     if tree["name"] == "Unknown":
# # #         tree["color"] = getRandomGreenShade()  # Dim gray

# # # with open('3sv2.json', 'w') as jfile:
# # #     json.dump(dta, jfile, indent=4)

# # # print("Done mm")



# # import json

# # with open("3sv2.json", "r") as f:
# #     data = json.load(f)

# # tree_map = {}

# # for item in data:
# #     name = item["name"]
# #     latlng = item["latlng"]
# #     color = item["color"]
# #     size = item["size"]

# #     if name not in tree_map:
# #         tree_map[name] = {
# #             "color": color,
# #             "size": size,
# #             "latlng": []
# #         }

# #     tree_map[name]["latlng"].append(latlng)

# # with open("3sv3.json", "w") as f:
# #     json.dump(tree_map, f, indent=4)


# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# import json

# cred = credentials.Certificate('treemap--cu-firebase-adminsdk-fbsvc-a93090909f.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# def upload_to_firestore(collection_name, json_file_path):
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)

#     collection_ref = db.collection(collection_name)

#     for tree_type, tree_data in data.items():
#         doc_ref = collection_ref.document(tree_type)
#         doc_ref.set(tree_data)
#         print(f"Uploaded {tree_type} to {collection_name}")

# print("Uploading tree data...")
# upload_to_firestore('trees', '3sv3.json')

# print("Uploading descriptions...")
# upload_to_firestore('descriptions', 'descriptions.json')

# print("Upload complete!")




import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def upload_json_to_firebase():
    # Initialize Firebase with your service account
    # Replace 'path/to/serviceAccountKey.json' with your actual service account file path
    cred = credentials.Certificate('treemap--cu-firebase-adminsdk-fbsvc-a93090909f.json')
    
    # Initialize the app with a database URL
    # Replace 'your-database-url' with your actual Firebase Realtime Database URL
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://treemap--cu-default-rtdb.firebaseio.com/'
    })
    
    # Load descriptions.json
    try:
        with open('descriptions.json', 'r') as f:
            descriptions_data = json.load(f)
        
        # Upload descriptions data to Firebase
        descriptions_ref = db.reference('descriptions')
        descriptions_ref.set(descriptions_data)
        print("Descriptions data uploaded successfully!")
        
    except Exception as e:
        print(f"Error uploading descriptions data: {e}")

    
    # Load trees.json
    try:
        with open('3sv3.json', 'r') as f:
            trees_data = json.load(f)
        
        # Upload trees data to Firebase
        trees_ref = db.reference('trees')
        trees_ref.set(trees_data)
        print("Trees data uploaded successfully!")
        
    except Exception as e:
        print(f"Error uploading trees data: {e}")

if __name__ == "__main__":
    print("Starting upload to Firebase Realtime Database...")
    upload_json_to_firebase()
    print("Upload process completed.")