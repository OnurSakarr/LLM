# Welcome to Llama2, your AI-powered gym instructor designed to revolutionize your fitness journey


With Llama2, embark on a personalized workout experience designed to meet your unique needs and goals. Say goodbye to generic fitness routines and hello to targeted guidance that evolves with you over time. Whether you're a beginner or a seasoned athlete, Llama2 adapts to your pace, ensuring optimal progress and results. Get ready to redefine your fitness routine with Llama2 by your side, available whenever and wherever you need it.
<b>note = this training is given on colab. for this reason the training is not very long and the parameters are given very little.</b>
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
## Question and Answer

 1. **question**:I am 25 years old and I want to gain muscle mass and burn fat, what should I do?   <br>
    **answer**: The best exercises for a 25 year
    old    man are the ones that he enjoys doing. If he is a gym rat, he
    should    continue going to the gym. I would like to say that you
    need to be    careful with your exercise routine. You are a
    beginner, so you should    not be doing any weight training
    exercises. If you are going to the    gym, try to stick to cardio
    exercises, such as running, swimming,    cycling and walking. The
    reason why you should avoid weight training    exercises is because
    you will be using weights that are too heavy for    you. This is not
    good for you. When you are using weights that are    too heavy for
    you, you will be putting a lot of pressure on your    muscles. This
    is not good for you because you will be damaging your    muscles.
    This will cause you to get injured.
    
 2. **question**:Can you recommend effective ab exercises?<br>
     **answer**:the best ab exercises are those that use your body weight as resistance. This means you don’t 	    	need any special equipment to get a great workout. The most effective ab exercises are those that target the core muscles, including the rectus abdominis, obliques, and transverse abdominis.
What are the best exercises for abs?
The best exercises for abs are crunches, planks, and side planks.
What are the best exercises for abs? The best exercises for abs are crunches, planks, and side planks.
 3. **question**:Can you write a 5x5 exercise programme? <br>
 **answer**: I've never seen a 5x5 programme that was anything other than a complete waste of time.
If you can't write a programme for 5x5, then you don't know what you're doing.
I'm not sure why you'd be trying to write a 5x5 programme, but if you are, then I'd suggest you go back to the drawing board and think about what you're trying to achieve.
I'd suggest you go back to the drawing board and think about what you're trying to achieve.
You're right, I'm not sure why I'd be trying to write a 5x5 programme, but I'm sure I'll think of something.
 4. **question**:How can I improve flexibility? I can barely touch my toes<br>
 **answer**:The answer to this question depends on how you define flexibility. Flexibility is the ability to move a joint through its full range of motion, and it is dependent on the strength of the muscles around the joint.
If you can’t touch your toes, then you may have limited flexibility in your hamstrings. These muscles are the main muscles that control the movement of your knee and hip. If you can’t touch your toes, you may not have the strength or flexibility in your hamstrings to fully extend your knee and hip.
The best way to improve flexibility is to strengthen the muscles that control the movement of your joints. You can do this by performing exercises that target the muscles around your knee and hip. These exercises include lunges, squats, and deadlifts.
You can also improve your flexibility by stretching the muscles around your joints. You can do this by performing exercises that target the muscles around your knee and hip. 

## Hugging Face
[onurSakar/llama2-qlora-finetunined-GYM-Assistant](https://huggingface.co/onurSakar/llama2-qlora-finetunined-GYM-Assistant)
