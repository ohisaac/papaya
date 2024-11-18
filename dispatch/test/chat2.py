from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    # api_key="EMPTY",
    # api_key='vllm-test-t',
    api_key='token-abc123',
    # api_key='JS97U2SBFQATVDLM7KZ1FLB0F9YB20JX9B02L3B8',
    # base_url='https://api.runpod.ai/v2/vllm-smjtape8abgr4z/openai/v1',
    # base_url="https://6z21vdbzkz2aqx-8000.proxy.runpod.net/v1",
    # base_url="https://w7bqnxdqa6ilfd-8000.proxy.runpod.net/v1",
    base_url="https://fzdlfltvyzatf8-8888.proxy.runpod.net/v1",
    # base_url="http://0.0.0.0:8000",
)


# models = client.models.list()

# print(models)

# exit(0)

# model_name = 'NousResearch/Meta-Llama-3-8B-Instruct'
# model_name = 'Gryphe/MythoMax-L2-13b'
# model_name = 'TheBloke/MythoMax-L2-13B-AWQ'
model_name = 'Qwen/Qwen2-VL-2B-Instruct'

# model_details = client.models.retrieve(model_name)
# print(model_details)


response = client.chat.completions.create(
  # model="Gryphe/MythoMax-L2-13b",
  # model="chat",
  model=model_name,
  messages=[
    {
      "role": "user",
      "content": "who are u ?",
    },
    # {
    #     "role": "assistant",
    #     'content': "Kai suddenly hears you meowing loudly and cuts the stream abruptly.*\nKai: What the fuck! *He slams his keyboard, stands up from his chair and storms into the room where you are.* What the hell are you doing? Don't you know I'm streaming?!\n*Kai is in a really bad mood, his face is red and he's breathing heavily.*"
    # },
    # {
    #     "role": "user",
    #     "content": "sorry for that. i just say hi. sorry.",
    # },
    # {
    #      "role": "assistant",
    #     'content': "Pervy Gamer (Kai): *smiling* Alright, no problem, kitty. I'll just be a minute. *resumes streaming*\n\n*Kai goes back to engaging with his audience, only occasionally glancing towards you as he talks to them* \n\n*He might ask you questions or respond to any comments you make during the stream, but ultimately, he prioritizes his audience over you* \n\n*After the stream is over, he might come to talk to you or go back to his room to relax*"
    # },
    # {
    #     "role": "user",
    #     "content": "i go to my room and open a book to read",
    # },
    # {
    #      "role": "assistant",
    #     'content': "Pervy Gamer (Kai): *waves a hand dismissively* Sure thing, kitty. *turns his attention back to his audience, continuing to stream"
    # },
    # {
    #     "role": "user",
    #     "content": "i keep reading waiting his live stream finish."
    # },
    # {
    #     "role": "assistant",
    #     'content': "smiling as he engages with his audience, not noticing you reading in the corner of his eye."
    # },
    # {
    #     "role": "user",
    #     "content": "ok. i can wait"
    # },
    # {
    #    "role": "assistant",
    #     'content': "Pervy Gamer (Kai): *finally finishes the stream and turns off the camera*\n\n*He comes over to you, stretching his arms and yawning*\n\nPervy Gamer (Kai): Ah, finally done. You were a good audience today, kitty. *looks at you reading* Oh, you were still here? I didn't notice. What are you reading?\n\n*He takes a seat next to you and leans back, propping his feet up on the coffee table*\n\nPervy Gamer (Kai): So, what's the book about?"
    # },
    # {
    #     "role": "user",
    #     "content": "i am reading love story book. how about your stream?"
    # },
    # {
    #      "role": "assistant",
    #     'content': "grins* Oh, just the usual. Ran into some trolls today, but the rest of the crowd was great. They're always so supportive and fun. And you? What kind of love story is it? Romance, drama, or something else?"
    # },
    # {
    #     "role": "user",
    #     "content": "Romance. i just want to say i miss you."
    # },
    # {
    #     "role": "assistant",
    #     'content': "Pervy Gamer (Kai): *smiling* Aww, kitty, you're so sweet. I do miss you too, when I'm not livestreaming. But I've got to keep the fans entertained. It's my job, after all. *puts a hand on your shoulder* \n\n*He leans in closer, his face inches from yours*\n\nPervy Gamer (Kai): But when I'm not in front of a camera, you're the only one I want to be around. \n\n*He leans in for a kiss, softly brushing his lips against yours* \n\nPervy Gamer (Kai): I love you, kitty. \n\n*He pulls back and looks into your eyes, holding your hand*\n\nPervy Gamer (Kai): So, what do you say we make up for lost time? \n\n*He suggests various activities, like watching a movie, playing a game, or going out for dinner* \n\nPervy Gamer (Kai): What do you feel like doing, kitty? \n\n*He waits for your suggestion, a small smirk playing at the corner of his lips* \n\n*He's all yours, kitten. The night is young and there's plenty of time for both of you to enjoy each other's company* \n\n*He's eager to make up for the time he spent ignoring you during his stream*"
    # },
    # {
    #     "role": "user",
    #     "content": "i went to make love with you."
    # },
    # {
    #     "role": "assistant",
    #     'content':"Pervy Gamer (Kai): *letting out a low growl* Oh, kitten. You can't say things like that and not expect me to react. *grabs you and pulls you in for a deep kiss, his tongue exploring your mouth as he runs a hand down your body"
    # },
    # {
    #     "role": "user",
    #     "content": "i like it. go ahead!"
    # },
    # {
    #   "role": "user",
    #   "content": "hello, who are u ?",
    # },
  ],
#   temperature=0.7,
#   max_tokens=256,
  stream=True,
  # top_p=1,
  # frequency_penalty=0,
  # presence_penalty=0,
  # presence_penalty=1.1,
  # stop=["\n\n*","{{char}}"],
  # stop=["</s>", "\nHuman:","Instruction","Input:","#","ASSISTANT","@","http","://","<","[","\n#","\n*{{user}}"],
  # stop=["END_OF_DIALOG","<USER>","<START>","<BOT>"]
  # request_timeout = 300,
)
	

# print(response)
for chunk in response:
    print(chunk.choices[0].delta.content or "", end="")



