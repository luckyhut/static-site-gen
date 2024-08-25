import os
import shutil

from blocks import markdown_to_html_node

def main():
    rm_and_copy()
    generate_page_recursive("content/", "template.html", "public/")

def rm_and_copy():
    shutil.rmtree("public")
    copy_to_public("static", "public")
    print("Files copied from static/ to public./")

def copy_to_public(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
        
    for file in os.listdir(source_path):
        full_source_path = os.path.join(source_path, file)
        full_dest_path = os.path.join(dest_path, file)
        if os.path.isdir(full_source_path):
            copy_to_public(full_source_path, full_dest_path)
        else:
            shutil.copy(full_source_path, full_dest_path)
            print(file, "copied.")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        print(line)
        if line.startswith("# "):
            return line.lstrip("# ")
    raise Exception("h1 not found")

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        
    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            new_dest_path = dest_path.replace(".md", ".html")
            print(new_dest_path, "hhhhh")
            generate_page(from_path, template_path, new_dest_path)
        else:
            generate_page_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    from_contents = from_file.read()
    from_file.close()
    template_file = open(template_path)
    template_contents = template_file.read()
    template_file.close()
    html_node = markdown_to_html_node(from_contents)
    html_string = html_node.to_html()
    title = extract_title(from_contents)
    title_replaced = template_contents.replace("{{ Title }}", title)
    content_replaced = title_replaced.replace("{{ Content }}", html_string)
    dest_file = open(dest_path, "w")
    dest_file.write(content_replaced)
    dest_file.close()
    
main()
