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

    MODEL = "llama-3.3-70b-versatile"

    def __init__(self,prompt):
        self.prompt = prompt

    from dotenv import load_dotenv
    load_dotenv()
    def chat(self,input):
        prompt = f"{self.prompt}:{input}"
        model = ChatGroq(model = GroqDesc.MODEL)
        return model.invoke(prompt)
    
a = GroqChat("What is the capital city of France?","llama-3.3-70b-versatile")

b = GroqDesc("translate to telugu")

res = b.chat(a.chat().content).content
print(res)