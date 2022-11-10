import soundfile as sf
from pathlib import Path
import os


def txt_to_file(file_path: str, sample_rate_hz: int = None, normalizing_denominator: float = None) -> None:
    """

    :param file_path: csv to read
    :param sample_rate_hz: optional ovreride for sample rate (dont ask me if someone ever needs this no clue)
    :param normalizing_denominator: optional nomralization of amplitude
    :return:
    """
    data = get_data_from_txt(file_path)

    # write data
    if normalizing_denominator is None:
        data = data
    else:
        data = [value / normalizing_denominator for value in data]
    output_file_path = f"{file_path}_{sample_rate_hz}hz_.wav"
    print(f"Saved {output_file_path}")
    sf.write(output_file_path, data, sample_rate_hz)


def get_data_from_txt(file_path: str) -> list:
    data = list()
    with open(file_path, 'r+') as f:
        for line in f:
            data.append(float(line))
    return data


def get_txt_files(folder_name: str) -> list:
    basepath = Path(__file__).parent.resolve()
    folder_path = Path().joinpath(basepath, folder_name)
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
        print(
            f"Made folder {folder_path}, put .csv files there and re-run this. "
            f"Each will be individually turned to .wav's assuming Column A is time and B amplitude")

    rv = list()
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            rv.append(f"{Path().joinpath(folder_path, str(file))}")
    return rv
