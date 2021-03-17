import getopt
import json
import re
import sys
import fitz


def read_file(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "i:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("Invaild option provided")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
    return inputfile, outputfile


def file_process():
    inputFile, outputFile = read_file(sys.argv[1:])
    print(inputFile, outputFile)
    try:
        # Convert pdf into text using fitz library
        with fitz.open(inputFile) as doc:
            pdftext = ""
            for page in doc:
                pdftext += page.getText()
        print(pdftext)
        dict_apnd = []
        dict_apend = ['']
        final_list = ['']

        # split text file to get list
        data = re.split('\n \n', pdftext)
        for sub in data:
            dict_apnd.append(list(map(str.strip, re.split('\-{4,}', sub))))

        # to remove list of list items
        pdf_list = [item for sublist in dict_apnd for item in sublist]

        # removing empty items from list
        pdf_list = [x for x in pdf_list if x.strip()]
        check_string = '\n_'
        for uni_list in pdf_list:
            if check_string in uni_list:
                dict_apend.append(uni_list)
            else:
                print("not", uni_list)
                dict_apend[-1] += " " + uni_list
        print(dict_apend)
        for s in dict_apend:
            if check_string in s:
                final_list.append(s)
            else:
                print("not", s)
                final_list[-1] = "Personal Details \n___" + s
        print(final_list)

        # converting list to string
        listToStr = ' #$ '.join(map(str, final_list))
        final_text = re.sub('\_+', '_', listToStr)

        res = []
        for sub in final_text.split(' #$ '):
            res.append(map(str.strip, sub.split('\n_', 1)))
        res = dict(res)
        with open(outputFile, 'w') as fp:
            json.dump(res, fp, indent=1)

    except Exception as e:
        print(e.__str__())


if __name__ == "__main__":
    file_process()
