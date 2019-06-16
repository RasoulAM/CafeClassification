import pandas as pd
import os
from tqdm import tqdm_notebook as tqdm
from hazm import *
import divar_normalizer
normalizer = Normalizer()
dv = divar_normalizer.DivarNormalizer()

def clean_text(x):
    x = normalizer.normalize(x)
    x = dv.normalize(x)
    x = x.replace(",", " ")
    x = x.replace(".", " ")
    x = x.replace(";", " ")
    x = x.replace("\n", " ")
    x = x.replace("\t", " ")
    x = x.replace("\r", " ")
    return x


def clean_original_data_cat1(
        result_file="../data/formatted_data_cat1",
        labeler=lambda x:x,
        header=False,
        index=False,
        title_desc_concat=True
    ):
    path = '../data/raw'
    list_raw_data_files = os.listdir(path)
    list_raw_data_files.sort()
    train_file = open(result_file, "w")
    train_data_selected = None
    for cnt, file in tqdm(enumerate(list_raw_data_files)):
        print(cnt, file)
        try:
            next_train_data = pd.io.json.read_json(os.path.join(path, file), lines=True)
            train_data_cleaned = next_train_data[['cat1', 'title', 'desc']].copy()
            train_data_cleaned['cat1'] = train_data_cleaned['cat1'].apply(labeler)
            if title_desc_concat:
                train_data_cleaned['text'] = train_data_cleaned['title'] + " " + train_data_cleaned['desc']
                train_data_cleaned = train_data_cleaned[['cat1', 'text']]
                train_data_cleaned['text'] = train_data_cleaned['text'].apply(clean_text)
            else:
                train_data_cleaned['title'] = train_data_cleaned['title'].apply(clean_text)
                train_data_cleaned['desc'] = train_data_cleaned['desc'].apply(clean_text)
            train_file.write(train_data_cleaned[:].to_csv(header=header, index=index))

        except KeyError as e:
            print('unformatted file found')
            print(e)
        except KeyboardInterrupt:
            print("Interrupting!")
            break
        except IsADirectoryError:
            pass
    train_file.close()
    
    
def clean_original_data_cats(
        result_file="../data/formatted_data_cats",
        labeler=lambda x:x,
        header=False,
        index=False,
        title_desc_concat=True
    ):
    path = '../data/raw'
    list_raw_data_files = os.listdir(path)
    list_raw_data_files.sort()
    train_file = open(result_file, "w")
    train_data_selected = None
    for cnt, file in tqdm(enumerate(list_raw_data_files)):
        print(cnt, file)
        try:
            next_train_data = pd.io.json.read_json(os.path.join(path, file), lines=True)
            train_data_cleaned = next_train_data[['cat1', 'cat2', 'cat3', 'title', 'desc']].copy()
            train_data_cleaned['cat1'] = train_data_cleaned['cat1'].apply(labeler)
            train_data_cleaned['cat2'] = train_data_cleaned['cat2'].apply(labeler)
            train_data_cleaned['cat3'] = train_data_cleaned['cat3'].apply(labeler)
            
            if title_desc_concat:
                train_data_cleaned['text'] = train_data_cleaned['title'] + " " + train_data_cleaned['desc']
                train_data_cleaned = train_data_cleaned[['cat1', 'cat2', 'cat3', 'text']]
                train_data_cleaned['text'] = train_data_cleaned['text'].apply(clean_text)
            else:
                train_data_cleaned['title'] = train_data_cleaned['title'].apply(clean_text)
                train_data_cleaned['desc'] = train_data_cleaned['desc'].apply(clean_text)
            train_file.write(train_data_cleaned[:].to_csv(header=header, index=index))

        except KeyError as e:
            print('unformatted file found')
            print(e)
        except KeyboardInterrupt:
            print("Interrupting!")
            break
        except IsADirectoryError:
            pass
    train_file.close()