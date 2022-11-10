from common import txt_to_file, get_txt_files, get_data_from_txt


def convert_txt_foldercontents_to_wav(sample_rate: int, folder_name: str) -> None:
    txt_files = get_txt_files(folder_name)
    if not txt_files:
        print("There's no txt files in the normalizable txt source folder")
        return None

    all_data = list()
    for txt_file in txt_files:
        data = get_data_from_txt(txt_file)
        for item in data:
            all_data.append(abs(item))
    normalizing_denominator = max(all_data)
    for txt_file in txt_files:
        txt_to_file(file_path=txt_file, sample_rate_hz=sample_rate, normalizing_denominator=normalizing_denominator)


if __name__ == "__main__":
    folder = "normalized_txt_files"
    sample_rate_input = input("Type the sample rate for the non-normalized files."
                              "Type anything but a number to skip.")
    try:
        sample_rate_input = int(sample_rate_input)
    except ValueError:
        exit()

    convert_txt_foldercontents_to_wav(sample_rate=sample_rate_input, folder_name=folder)
