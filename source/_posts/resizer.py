from PIL import Image
import os

from PIL import Image
import os

def resize_images(input_folder, output_folder, max_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                # 获取原始图像的尺寸
                width, height = img.size

                # 只处理高度低于max_height的图像
                if height <= max_height:
                    img.save(output_path)
                    continue

                # 计算缩放比例
                ratio = max_height / height

                # 计算新的尺寸
                new_width = int(width * ratio)
                new_height = int(height * ratio)

                # 调整图像大小
                resized_img = img.resize((new_width, new_height))

                # 保存调整大小后的图像
                resized_img.save(output_path)


if __name__ == "__main__":
    input_folder = "乐器与音色 - 副本"
    output_folder = "乐器与音色"

    resize_images(input_folder, output_folder, 400)