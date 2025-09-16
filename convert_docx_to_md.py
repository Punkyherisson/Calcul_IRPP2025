import os
import pypandoc

pypandoc.download_pandoc()

folder_path = r"C:\Github.com\Punkyherisson\Calcul_IRPP2025"

for filename in os.listdir(folder_path):
    if filename.endswith(".docx"):
        docx_path = os.path.join(folder_path, filename)
        md_filename = os.path.splitext(filename)[0] + ".md"
        md_path = os.path.join(folder_path, md_filename)
        try:
            output = pypandoc.convert_file(docx_path, 'md')
            with open(md_path, "w", encoding="utf-8") as md_file:
                md_file.write(output)
            print(f"Converti : {filename} -> {md_filename}")
        except Exception as e:
            print(f"Erreur lors de la conversion de {filename} : {e}")