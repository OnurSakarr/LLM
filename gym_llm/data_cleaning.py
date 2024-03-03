import json
import deduplication as dp 
import language_detection as ld
import remove_emoji as emoji
import bad_word_remove 
import remove_url
from tqdm import tqdm

def clean_data(data):
  clean_data = dp.deduplications(data, texts=["context"])
  detection_info = ld.language_detections(clean_data["data"], texts=["context"])
  emoji_clean = emoji.remove_emojis_from_json(detection_info["data"])
  bad_remove = bad_word_remove.bad_word_detections(emoji_clean, texts=["context"])
  url_clean= remove_url.url_word_remove(bad_remove["data"], texts=["context"])
  
  data_process_info = {
    "deduplication": {
      "raw": clean_data["all_data_size"],
      "delete": clean_data["repeat_data_size"],
      "clean": clean_data["clean_data_size"]
    },
    "language_detection": {
      "raw": detection_info["all_count"],
      "delete": detection_info["non_turkish_count"],
      "clean": detection_info["turkish_count"]
    },
    "bad_word_clean": {
      "raw": bad_remove["all_data_size"],
      "delete": bad_remove["bad_data_size"],
      "clean": bad_remove["clean_data_size"]
    },
    "url_clean": {
      "raw": url_clean["all_data_size"],
      "delete": url_clean["url_data_size"],
      "clean": url_clean["clean_data_size"]
    }
  }
  return url_clean["data"], data_process_info


def write_json_file(data, file_name):
    output_file=f"/{file_name}.json"
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        
if __name__ == "__main__":
    
    clean_data_result, data_process_info = clean_data(data)
    write_json_file(data_process_info, info_json)