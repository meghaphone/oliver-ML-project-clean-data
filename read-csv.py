import csv
import os.path
import shutil


new_dataset_folder_name = 'clean-dataset'
print(f'\tCreating new dataset folder: {new_dataset_folder_name}')
os.mkdir(new_dataset_folder_name)
created_new_dataset_folder = os.path.exists(new_dataset_folder_name)
print(f'\tcreating new dataset folder succeeded: {created_new_dataset_folder}')

print(f'\tCreating subfolders in dataset folder for each category [label].')
labels = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
for l in labels:
    new_label_folder_name = new_dataset_folder_name + "/" + l
    print(f'\tCreating subfolder for category [label]: {l} at path: {new_label_folder_name}')
    os.mkdir(new_label_folder_name)
    created_new_subfolder = os.path.exists(new_label_folder_name)
    print(f'\tcreating new subfolder at path: {new_label_folder_name} succeeded: {created_new_subfolder}')

with open('legend.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            filename = row[1]
            label = row[2].lower()
            imagePath = 'images/'+filename
            fileExists = os.path.exists(imagePath)
            #print(f'\t{row[1]} filename has label {row[2].lower()}')
            folderPath = new_dataset_folder_name+"/"+label
            folderExists = os.path.exists(folderPath)
            print(f'\tfilename: {filename}, label: {label}, image path: {imagePath}, file exists: {fileExists}, folder exists: {folderExists}')
            newFilePath = new_dataset_folder_name+"/"+label+'/'+filename
            newFolderPath = folderPath + "/"
            print(f'\tcopying image: {imagePath} to new folder path: {newFolderPath}. new file path: {newFilePath}')
            shutil.copyfile(imagePath, newFilePath)
            newFileExists = os.path.exists(newFilePath)
            print('image copy succeeded: {newFileExists}')
            line_count += 1
    print(f'Processed {line_count} lines.')