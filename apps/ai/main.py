import os,httpx
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI(title='GenAI LMS AI Service')
class ChatRequest(BaseModel):
    message:str
    user_id:str
    conversation_id:str|None=None
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/chat')
async def chat(req:ChatRequest):
    key=os.getenv('AI_API_KEY');model=os.getenv('AI_MODEL')
    if not key or not model: raise HTTPException(503,'AI provider is not configured. Set AI_API_KEY and AI_MODEL.')
    base=os.getenv('AI_BASE_URL','https://api.openai.com/v1')
    system='You are CipherBot, an academic learning assistant. Do not claim knowledge from university documents unless retrieved context is supplied. Do not help bypass graded assessments. State uncertainty when needed.'
    payload={'model':model,'messages':[{'role':'system','content':system},{'role':'user','content':req.message}],'temperature':0.2}
    async with httpx.AsyncClient(timeout=30) as c:
        r=await c.post(f'{base}/chat/completions',json=payload,headers={'Authorization':f'Bearer {key}'})
    if r.status_code>=400: raise HTTPException(r.status_code,'AI provider request failed')
    return {'answer':r.json()['choices'][0]['message']['content'],'citations':[]}
