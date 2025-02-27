f= open("fileone.txt","w+")
f.write("first FILE")
f.close()

f= open("filetwo.txt","w+")
f.write("two FILE")
f.close()

import zipfile
comp_file=zipfile.ZipFile("comp_file.zip","w")
comp_file.write("fileone.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


zipfile=zipfile.ZipFile("comp_file.zip","r")
zipfile.extractall("extracted_content") ##folder name where the files are extracted
zipfile.close()

print("=====================================END OF zip and unzip=====================================")

