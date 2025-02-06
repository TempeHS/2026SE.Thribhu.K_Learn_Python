# gif | image/gif
# jpg | image/jpeg
# jpeg | image/jpeg
# png | image/png
# pdf | application/pdf
# txt | text/plain
# zip | application/zip

print("Input your file and output the extension")
_input = input().lower().split('.')[1]

def compare(input: str) -> str:
    match _input:
        case 'gif':
            return "image/gif"
        case 'jpg':
            return "image/jpeg"
        case 'jpeg':
            return "image/jpeg"
        case 'pdf':
            return "application/pdf"
        case 'txt':
            return "text/plain"
        case 'zip':
            return "application/zip"
        case _:
            return "unknown/unknown"

print(compare(_input))