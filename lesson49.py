import os
import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.rstrip("\n"))


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    missing_files = [filename for filename in filenames if not os.path.exists(filename)]

    if missing_files:
        print("Отсутствуют следующие файлы:")
        for missing in missing_files:
            print(missing)
        exit(1)

    start_time_linear = time.time()
    for filename in filenames:
        read_info(filename)
    end_time_linear = time.time()

    print(f"Время выполнения линейного вызова: {end_time_linear - start_time_linear:.6f} секунд")

    start_time_multiprocessing = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)
    end_time_multiprocessing = time.time()

    print(f"Время выполнения многопроцессного вызова:"
          f" {end_time_multiprocessing - start_time_multiprocessing:.6f} секунд")