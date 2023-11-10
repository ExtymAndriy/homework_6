import datetime
import logging
import os

def main(path_to_folder):
    try:
        started_at = datetime.datetime.now()


        extensions = {
            'image': ('JPEG', 'PNG', 'JPG', 'SVG'),
            'video': ('AVI', 'MP4', 'MOV', 'MKV'),
            'text': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
            'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
            'archive': ('ZIP', 'GZ', 'TAR'),
        }

        with open(file='sorted.log', mode='w', encoding='utf-8') as file:
            def create_folders_from_list(path_to_folder, folder_names) -> None:
                for folder in folder_names:
                    if not os.path.exists(f'{path_to_folder}\\{folder}'):
                        log = f'[+] Створення папки {folder} по шляху: {path_to_folder}\n'
                        file.write(log)
                        logging.info(log)
                        os.mkdir(f'{path_to_folder}\\{folder}')


        def get_subfolder_paths(path_to_folder) -> list:
            subfolder_paths = [folder.path for folder in os.scandir(path_to_folder) if folder.is_dir()] 
            return subfolder_paths



        def file_paths(path_to_folder) -> list:
            file_paths = [f.path for f in os.scandir(path_to_folder) if not f.is_dir()]
            return file_paths



        def sort_files(path_to_folder):
            file_paths = get_file_paths(path_to_folder)
            extensions_list = list(extensions.items())
            for file_paths in file_paths:
                file_extension = file_paths.split('.')[-1]
                filename = file_paths.split('\\')[-1]
                directory = None


                for dict_key_int in range(len(extensions_list)):
                    if file_extension in extensions_list[dict_key_int][1]:
                        directory = extensions_list[dict_key_int][0]
                    break



            if not directory:
                file_extension = '*'
                for dict_key_int in range(len(extensions_list)):
                        if file_extension in extensions_list[dict_key_int][1]:
                            directory = extensions_list[dict_key_int][0]
                        break


            if directory:
                log = f'[*] Переміщення файлу \'{filename}\' в папку {directory} по шляху {file_paths}' 
                file.write(log)
                logging.info(log)
                error_log = None
                try:

                    os.rename(file_paths, f'{path_to_folder}\\{directory}\\{filename}')
                except FileExistsError:
                    error_log = f'[*] не вийшло перемістити файл\'{filename}\' оскільки він вже сворений' 
                except FileNotFoundError:
                    error_log = f'[*] не вийшло знайти файл\'{filename}\' в папці по шляху: {filename}'
                except Exception as err:
                    error_log = f'[*] при переміщенні файла\'{filename}\' вийшла помилка\n'
                finally:
                    if error_log:
                        file.write(error_log)
                        logging.error(error_log)


        def remove_empty_folders(path_to_folder):

            subfolder_paths = get_subfolder_paths(path_to_folder)

            for path in subfolder_paths:

                if not os.listdir(path):
                    folder = path.split('\\')[-1]
                    log = f'[-] видалення пустої папки {folder} по шляху: {path}\n'
                    file.write(log)
                    logging.info(log)
                    os.rmdir(path)


        create_folders_from_list(path_to_folder, extensions)
        sort_files(path_to_folder)
        remove_empty_folders(path_to_folder)

        file.write(f'\n Сортування завершене за {datetime.datetime.now() - started_at}')
except FileNotFoundError as err:
    logging.warning(err.args[1] + ' | ' + path_to_folder)
finally:
    logging.info(f'Сортування файлів по шляху {path_to_folder} завершено.')
            





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    path_to_folder = 'from'
    main(path_to_folder )