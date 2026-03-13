from langchain_groq import ChatGroq

class GroqChat: 

    def __init__(self,prompt,MODEL):
        self.prompt = prompt
        self.MODEL = MODEL

    from dotenv import load_dotenv
    load_dotenv()   
    def chat(self):
        model = ChatGroq(model = self.MODEL)
        return model.invoke(self.prompt)
    

class GroqDesc:

    def __init__(self,MODEL,prompt):
        self.MODEL = MODEL
        self.prompt = prompt

    from dotenv import load_dotenv
    load_dotenv()
    def chat(self,input):
        model = ChatGroq(model = self.MODEL)
        return model.invoke(input)
    
a = GroqChat("What is the capital city of France?","llama-3.3-70b-versatile")

b = GroqDesc("llama-3.3-70b-versatile","Generate a description")

res = b.chat(a.chat().content)
print(res)