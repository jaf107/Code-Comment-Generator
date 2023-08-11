def get_line_from_file(file_path, line_number):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            lines = file.readlines()

            if not lines:
                return "The file is empty."

            total_lines = len(lines)
            
            if 1 <= line_number <= total_lines:
                selected_line = lines[line_number - 1]
                return f"Line {line_number}: {selected_line}"
            else:
                return "Invalid line number."
    
    except FileNotFoundError:
        return "File not found."

def main():
    # code_file_path = input("Enter the path of the 'source.code' file: ")
    # comment_file_path = input("Enter the path of the 'source.comment' file: ")
    
    code_file_path = r"G:\My Drive\SPL_3_Demo\Code-Comment-Generator\CodeSensei_Decom\dataset\PCSD\test\source.code"
    comment_file_path = r"G:\My Drive\SPL_3_Demo\Code-Comment-Generator\CodeSensei_Decom\dataset\PCSD\test\source.comment"
    # line_number = int(input("Enter the line number to display: "))
    line_number = 7

    code_line = get_line_from_file(code_file_path, line_number)
    comment_line = get_line_from_file(comment_file_path, line_number)

    print("Source Code Line:")
    print(code_line)

    print("\nSource Comment Line:")
    print(comment_line)

if __name__ == "__main__":
    main()
