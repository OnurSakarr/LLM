import json
import prompt_ops 
import word_count as wc
import token_size as ts
import file_size as fs


"""
texts = entering the name of the rows in the data
format_number_input = 1: falcone prompt ### Human:... ### Assistant:...
                      2:<s> context </s>  
                      3: <s>[INST] title [/INST] context </s>
                      4: <s>[INST] title [/INST] context, response </s>
data_files = extension of the data to be converted
json_save_path = prompt location to save data     
model_name = model name to be used               
"""


def write_json_file(data, file_name):
    output_file=f"/{file_name}.json"
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        
        
if __name__ == "__main__":
    texts=["context"]
    format_number_input = "2"
    data_files = [""]    
    json_save_path = ""
    info_json_save = ""
    model_name = ""
    
    dataTest=prompt_ops.prompt_editor(texts=texts, format_number_input=format_number_input,
                data_files=data_files,
                json_save_path=json_save_path)
    
    row_count = wc.countsize(dataTest[0])
    token_size = ts.tokensize(model_name,dataTest[0])
    data_size = fs.file_size(data_files)
    prompt_data_size = fs.file_size([dataTest[1]])
    
    data_process_info = {
      "raw size": row_count,
      "token size": token_size,
      "data size": data_size,
      "prompt data size":prompt_data_size
    }
    write_json_file(data_process_info, info_json_save)      
  