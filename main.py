import webview
import os
import configparser
import shutil

#Config Impotation
config  = configparser.ConfigParser()
config.read('config.ini')

#Shortcuts
shortcut_a  = config['paths'].get('shortcut_a')
shortcut_b  = config['paths'].get('shortcut_b')
shortcut_c  = config['paths'].get('shortcut_c')

#Titles
title_a = config['titles'].get('title_a')
title_b = config['titles'].get('title_b')
title_c = config['titles'].get('title_c')

#Icons
icon_a  = config['icons'].get('icon_a')
icon_b  = config['icons'].get('icon_b')
icon_c  = config['icons'].get('icon_c')

#Update Icons/Titles
def replace_icons(icon, id):
        source_path = icon
        destination_path = f"assets/tmp/{id}"
        shutil.copy(source_path, destination_path)


def replace_titles(window):
    js_code = f"""
        changeButtonName('title_a', '{title_a}');
        changeButtonName('title_b', '{title_b}');
        changeButtonName('title_c', '{title_c}');
        """
    window.evaluate_js(js_code)


replace_icons(icon=icon_a, id="icon_a.png")
replace_icons(icon=icon_b, id="icon_b.png")
replace_icons(icon=icon_c, id="icon_c.png")

#Import methods to JS
class Api:
    
    def quit(self):
        window.destroy()

    def a(self):
            os.startfile(shortcut_a)
            self.quit()
            
    def b(self):
            os.startfile(shortcut_b)
            self.quit()

    def c(self):
            os.startfile(shortcut_c)
            self.quit()

    def settings(self):
            os.popen("config.ini")



#Display loop
window = webview.create_window("Lynx", "assets/ui.html", width=380, height=600, background_color='#FFFFFF', resizable=False, js_api=Api())
webview.start(replace_titles, window, icon="assets/icon.ico")

#Deleting temp files
os.remove("assets/tmp/icon_a.png")
os.remove("assets/tmp/icon_b.png")
os.remove("assets/tmp/icon_c.png")