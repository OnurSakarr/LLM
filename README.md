# Welcome to Llama2, your AI-powered gym instructor designed to revolutionize your fitness journey


With Llama2, embark on a personalized workout experience designed to meet your unique needs and goals. Say goodbye to generic fitness routines and hello to targeted guidance that evolves with you over time. Whether you're a beginner or a seasoned athlete, Llama2 adapts to your pace, ensuring optimal progress and results. Get ready to redefine your fitness routine with Llama2 by your side, available whenever and wherever you need it.
![](https://github.com/OnurSakarr/LLM/blob/master/gym_llm/Image/image%20%2875%29.png)
## Model
meta-llama/Llama-2-7b <br> 
per_device_train_batch_size  =  1 <br> 
gradient_accumulation_steps  =  1 <br>
optim  =  "paged_adamw_32bit" <br>
save_steps  =  500 <br>
logging_steps  =  10 <br>
learning_rate  =  2e-4 <br>
max_grad_norm  =  0.3 <br>
max_steps  =  1500 <br>
warmup_ratio  =  0.03 <br> 
lora_alpha  =  16 <br>
lora_dropout  =  0.1 <br>
lora_r  =  8 <br>

## Data
token size = 214464 <br>
row = 1660 <br>
word count = 130755 <br>
prompt= \<s\>\[INST\] \<\<SYS\>\> Below is an instruction that describes a task. Write a response that appropriately completes the request \<\<\/SYS\>\> ("title") \[\/INST\] ("context")\</s\>


## Hugging Face
onurSakar/llama2-qlora-finetunined-GYM-Assistant
