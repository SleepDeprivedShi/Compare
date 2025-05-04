import os

def save_filenames_to_txt(directory, output_file):
    try:
        filenames = os.listdir(directory)
        with open(output_file, 'w') as f:
            for name in filenames:
                f.write(name + '\n')
        print("Saved", len(filenames), "filenames to", output_file)
    except Exception as e:
        print("Error:", e)

def compare_filename_lists(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            list1 = set(line.strip() for line in f1)
            list2 = set(line.strip() for line in f2)

        missing = list1 - list2
        if missing:
            print("Files present in the first list but missing in the second:")
            for item in sorted(missing):
                print(item)
        else:
            print("No differences found.")
    except Exception as e:
        print("Error:", e)
print("Compare 2 files")
print("1.Make text file\n2.Compare")
ans=int(input("Choice(1/2):"))

if ans == 1:
    dire=input("Enter directory:")
    out=input("Enter output file name:")
    if out.endswith != ".txt":
        out += ".txt"
    save_filenames_to_txt(dire,out)

elif ans == 2:
    f1=input("Enter file1:")
    f2=input("Enter file2:")
    compare_filename_lists(f1,f2)

else:
    print("Do as said bro, comeon!")
