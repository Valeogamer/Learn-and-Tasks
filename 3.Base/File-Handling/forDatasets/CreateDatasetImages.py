"""
    Формирование датасета из изображений
"""
import os
import matplotlib.pyplot as plt
from pprint import pprint
from PIL import Image
import numpy as np
from sklearn.utils import shuffle
import pickle
import sys


def newName_newExtention(path_dir: str, new_name: str, extention: str):
    """
    Новое имя и рассширение
    """
    images_path = [path_dir + '//' + i for i in os.listdir(path_dir)]
    for i in range(1, len(images_path) + 1):
        os.rename(images_path[i - 1], f'{path_dir + "//" + new_name}.{i}.{extention}')


def convert_images_to_array(images_path):
    """
    Перевод изображения в матричный вид
    """
    images_data = []
    for image_path in images_path:
        image = Image.open(image_path)
        image = np.array(image)
        images_data.append(image)
    return images_data


def visualization(data_images, labels=None):
    """
    Визуализция матричного изображения
    """
    plt.imshow(data_images)
    if labels:
        plt.title(f"Метка: {labels}")
    else:
        plt.title("Вывод изображения")
    plt.show()


def save(data: np.array, name: str, flag: int=None):
    """
    Сохранение данных:
    flag: с помощью чего сохранить:
        1 - numpy
        2 - pickle
    """
    if flag == 1:
        with open(f'{name}.pkl', 'wb') as data_file:
            pickle.dump(data, data_file, protocol=pickle.HIGHEST_PROTOCOL)
    elif flag == 2:
        np.save(f'{name}.npy', data)
    else:
        with open(f'{name}.pkl', 'wb') as data_file:
            pickle.dump(data, data_file, protocol=pickle.HIGHEST_PROTOCOL)
        np.save(f'{name}.npy', data)
    print("Сохранение завершено ✨")


def load(data_dir):
    """
    Загрузка данных
    return: загруженные данные
    """
    if 'pkl' in data_dir:
        with open(f'{data_dir}', 'rb') as data_file:
            data = pickle.load(data_file)
            return data
    elif 'npy' in data_dir:
        data = np.load(f'{data_dir}', allow_pickle=True)
        return data
    else:
        raise Exception("Ошибка при загрузке данных!")


if __name__ == '__main__':
    new_name_Pronation = 'pronation'
    new_name_Overpronation = 'overpronation'
    new_extention = 'png'
    path_dir_Pronation = "c://Users//User//Desktop//Разметка Тесты//BigFootBackup//Pronation"
    path_dir_Overpronation = "c://Users//User//Desktop//Разметка Тесты//BigFootBackup//Overpronation"
    # newName_newExtention(path_dir_Pronation, new_name_Pronation, new_extention)
    # newName_newExtention(path_dir_Overpronation, new_name_Overpronation, new_extention)
    images_path_Pronation = [path_dir_Pronation + '//' + i for i in os.listdir(path_dir_Pronation)]
    images_path_Overpronation = [path_dir_Overpronation + '//' + i for i in os.listdir(path_dir_Overpronation)]
    images_data_Overpronation = convert_images_to_array(images_path_Overpronation)
    images_data_Pronation = convert_images_to_array(images_path_Pronation)
    # visualization(images_data_Pronation[0])
    overpronation_labels = [0] * len(images_data_Overpronation)
    pronation_labels = [1] * len(images_data_Pronation)
    data = images_data_Overpronation + images_data_Pronation
    labels = overpronation_labels + pronation_labels
    data, labels = shuffle(data, labels, random_state=42)
    save(data=data, name='data')
    save(data=labels, name='labels')
    data_n = load('data.npy')
    data_p = load('data.pkl')
    labels_n = load('labels.npy')
    labels_p = load('labels.pkl')
