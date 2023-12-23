import os


def aggregate_parkhouse_data(data_dir):
    return


def create_parkhouse_data_folder(data_dir):
    module_dir = os.path.dirname(os.path.dirname(__file__))

    parkhouse_data_dir = os.path.join(module_dir, data_dir)

    os.makedirs(parkhouse_data_dir, exist_ok=True)
    return


def main():
    return


if __name__ == "__main__":
    main()
