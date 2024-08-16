import requests
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from app.schemas import YouTubeLink, AnalysisResult, QAResults
from app.process_video import download_video
router = APIRouter()
MODEL_SERVER_URL = "http://~"


@router.post("/analyze", response_model=AnalysisResult)
async def analyze_youtube_video(youtube_link: YouTubeLink):
    try:
        
        #video_path = download_video(youtube_link.url)
        video_path = "/Users/kjinh/Desktop/sports-police/BackEnd/app/test.mp4"
        files = {'file': open(video_path, 'rb')}
        # response = requests.post(MODEL_SERVER_URL, files=files)
        
        # if response.status_code == 200:
        #     model_report = response.content
        #     return AnalysisResult(report=model_report)
        # else:
        #     raise HTTPException(status_code=500, detail="Model server error")
        
        with open("/Users/kjinh/Desktop/sports-police/diving2_report.html", "rb") as f:
            response = f.read()
        return AnalysisResult(report=response)
        
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/qa", response_model=QAResults)
async def qa_with_res():
    try:
        
        # TODO
        res_from_gpt = "Hello Worlds!"
        return QAResults(answer=res_from_gpt)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
