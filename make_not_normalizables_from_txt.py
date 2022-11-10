from common import txt_to_file, get_txt_files


def convert_txt_foldercontents_to_wav(sample_rate: int, folder_name: str) -> None:
    txt_files = get_txt_files(folder_name)
    if not txt_files:
        print("There's no txt files in the not to normaliza .txt source folder")
    for txt_file in txt_files:
        txt_to_file(file_path=txt_file, sample_rate_hz=sample_rate)


if __name__ == "__main__":
    folder = "not_normalized_csv_files"
    sample_rate_input = input("Type the sample rate for the non-normalized files."
                              "Type anything but a number to skip.")
    try:
        sample_rate_input = int(sample_rate_input)
    except ValueError:
        exit()

    convert_txt_foldercontents_to_wav(sample_rate=sample_rate_input, folder_name=folder)
