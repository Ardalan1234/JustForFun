import os
import ctypes


class WallpaperChanger:
    def __init__(self, wallpaper_dir, index_file_path):
        self.wallpaper_dir = wallpaper_dir
        self.index_file_path = index_file_path

    def get_wallpapers(self):
        wallpapers = [wallpaper for wallpaper in os.listdir(self.wallpaper_dir) if
                      wallpaper.endswith(('png', 'jpg', 'jpeg'))]
        return wallpapers

    def get_index(self):
        with open(self.index_file_path, "r") as file:
            return int(file.read())

    def update_index(self, index):
        with open(self.index_file_path, "w") as file:
            file.write(str(index + 1))

    def get_wallpaper_path(self):
        wallpapers = self.get_wallpapers()
        index = self.get_index()
        self.update_index(index)
        wallpaper_path = os.path.join(self.wallpaper_dir, wallpapers[index % len(wallpapers)])
        return wallpaper_path

    @staticmethod
    def set_wallpaper(image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

    def change_wallpaper(self):
        image_path = self.get_wallpaper_path()
        self.set_wallpaper(image_path)


if __name__ == "__main__":
    WALLPAPER_DIR = "path\\to\\your\\wallpaper\\directory"
    INDEX_FILE_PATH = "path\\to\\index.txt"

    wallpaper_changer = WallpaperChanger(WALLPAPER_DIR, INDEX_FILE_PATH)
    wallpaper_changer.change_wallpaper()
