import os
from PIL import Image
import pandas as pd

path = "./Train/images/"
df = pd.DataFrame(columns=["path", "name"])

images = []

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    name, filetype = filename.split('.')
    if filetype != "jpg":
        im = Image.open(os.path.join(path, filename))
        os.remove(os.path.join(path, filename))
        rgb_im = im.convert("RGB")
        filename = f"{name.split('.')[0]}.jpg"
        rgb_im.save(filepath)
    nombre, apellido, idx = name.split("_")
    image = {"path": os.path.join("/content/drive/MyDrive/Tarea_3/T3 Dataset/images/", filename),
            "name": f"{nombre.capitalize()} {apellido.capitalize()}"}
    images.append(image)
    
df = pd.DataFrame.from_records(images)

total = len(df)
count = df["name"].value_counts()

stat = df.copy(deep=True)
stat["count"] = stat.groupby("name").transform("count")
stat = stat.drop_duplicates('name')
stat = stat.sort_values('count')
stat = stat[["name", "count"]]

print(f"\nFound {total} images:\n")
for name, count in zip(stat["name"], stat["count"]):
    print("\t{:<20}{:<3}".format(name, count))

df.to_csv('data_train.txt', sep='\t', index=False, header=False)
stat.to_csv('info_train.txt', sep='\t', index=False, header=True)

with open('info.txt', 'a') as file:
	file.writelines(f"\nTotal Files: {total}")
