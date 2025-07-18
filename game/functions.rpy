init python:
    import os

    background_folder = "images/bg"
    valid_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    dynamic_backgrounds = {}

    # Scan and define backgrounds
    for f in renpy.list_files():
        if f.startswith(background_folder + "/") and any(f.endswith(ext) for ext in valid_extensions):
            name = f[len(background_folder) + 1:].rsplit(".", 1)[0]  # Extract filename without folder or extension
            tag_name = "bg " + name  # Prefix the image name with "bg"
            dynamic_backgrounds[name] = tag_name
            renpy.image(tag_name, f)  # Define as a Ren'Py image

    # showing disabled options
    config.menu_include_disabled = False

    def getImage(path):
        for ext in valid_extensions:
            if renpy.loadable(path + ext):
                return path + ext
        return None

    def set_background(name):
        if name in dynamic_backgrounds:
            tag = dynamic_backgrounds[name]
            
            # Show the background and apply the matrix transformation for night mode
            renpy.scene()
            renpy.show(tag, at_list=[stretch_fullscreen])
        
        else:
            renpy.say("System", f"Background '{name}' not found.")

