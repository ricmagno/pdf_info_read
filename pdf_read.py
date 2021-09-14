from tabula import read_pdf 
import pandas as pd
import glob


def instructions_read(file_pdf):
    df = read_pdf(file_pdf,pages="all")
    instructions_df = df[0].iloc[:,0].dropna()
    sorted_df = pd.DataFrame(columns=['Installation Instructions'])
    j = 1
    instruction = ''

    for i in instructions_df[1:]:
        if i.find(str(j)+'.') == 0:
            if instruction != '':
                sorted_df = sorted_df.append({'Installation Instructions': instruction}, ignore_index=True)
            instruction = i
            j += 1
        else:
            instruction = instruction + ' ' + i
    sorted_df = sorted_df.append({'Installation Instructions': instruction}, ignore_index=True)
    sorted_df.to_csv(str(file_pdf[:-4]+'.txt'), sep='\t', header=None, index=False)

files = glob.glob("*.pdf")

for file_pdf in files:
    print('Running ', file_pdf)
    instructions_read(file_pdf)
