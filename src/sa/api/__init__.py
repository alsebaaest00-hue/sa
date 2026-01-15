"""FastAPI server for SA Platform"""

from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

from sa.utils import project_manager
from sa.generators import ImageGenerator, AudioGenerator, VideoGenerator

app = FastAPI(
    title="SA Platform API",
    description="منصة تحويل النصوص إلى وسائط متعددة",
    version="1.0.0",
)


# Models
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class GenerateImageRequest(BaseModel):
    project_id: int
    prompt: str
    negative_prompt: Optional[str] = ""


class GenerateAudioRequest(BaseModel):
    project_id: int
    text: str
    voice: Optional[str] = "Adam"


# Projects endpoints
@app.get("/api/projects", tags=["Projects"])
async def list_projects():
    """قائمة جميع المشاريع"""
    try:
        projects = project_manager.list_projects()
        return {"status": "success", "data": projects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/projects/{project_id}", tags=["Projects"])
async def get_project(project_id: int):
    """الحصول على تفاصيل مشروع"""
    project = project_manager.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="المشروع غير موجود")
    return {"status": "success", "data": project}


@app.post("/api/projects", tags=["Projects"])
async def create_project(project: ProjectCreate):
    """إنشاء مشروع جديد"""
    try:
        project_id = project_manager.create_project(project.name, project.description)
        return {
            "status": "success",
            "message": "تم إنشاء المشروع",
            "project_id": project_id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/api/projects/{project_id}", tags=["Projects"])
async def update_project(project_id: int, project: ProjectUpdate):
    """تحديث مشروع"""
    try:
        project_manager.update_project(project_id, project.name, project.description)
        return {"status": "success", "message": "تم تحديث المشروع"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/projects/{project_id}", tags=["Projects"])
async def delete_project(project_id: int):
    """حذف مشروع"""
    try:
        project_manager.delete_project(project_id)
        return {"status": "success", "message": "تم حذف المشروع"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Generations endpoints
@app.get("/api/projects/{project_id}/generations", tags=["Generations"])
async def get_generations(project_id: int):
    """الحصول على عمليات المشروع"""
    generations = project_manager.get_generations(project_id)
    return {"status": "success", "data": generations}


@app.post("/api/generate/image", tags=["Generation"])
async def generate_image(request: GenerateImageRequest):
    """توليد صورة"""
    try:
        # التحقق من وجود المشروع
        project = project_manager.get_project(request.project_id)
        if not project:
            raise HTTPException(status_code=404, detail="المشروع غير موجود")

        # توليد الصورة
        import os
        from sa.utils.config import config

        generator = ImageGenerator(config.replicate_api_key)
        images = generator.generate(
            request.prompt,
            request.negative_prompt,
            num_outputs=1,
        )

        if images:
            # حفظ المعلومات
            file_path = f"outputs/image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            generator.download_image(images[0], file_path)

            # إضافة للمشروع
            project_manager.add_generation(
                request.project_id, "image", request.prompt, file_path
            )

            return {
                "status": "success",
                "message": "تم توليد الصورة",
                "image_url": images[0],
                "file_path": file_path,
            }
        else:
            raise HTTPException(status_code=500, detail="فشل توليد الصورة")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/generate/audio", tags=["Generation"])
async def generate_audio(request: GenerateAudioRequest):
    """توليد صوت"""
    try:
        project = project_manager.get_project(request.project_id)
        if not project:
            raise HTTPException(status_code=404, detail="المشروع غير موجود")

        from sa.utils.config import config

        generator = AudioGenerator(config.elevenlabs_api_key)
        import datetime as dt
        from datetime import datetime

        file_path = f"outputs/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        audio_path = generator.generate_speech(
            request.text, request.voice, output_path=file_path
        )

        if audio_path:
            project_manager.add_generation(
                request.project_id, "audio", request.text, audio_path
            )

            return {
                "status": "success",
                "message": "تم توليد الصوت",
                "file_path": audio_path,
            }
        else:
            raise HTTPException(status_code=500, detail="فشل توليد الصوت")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Statistics endpoints
@app.get("/api/statistics", tags=["Statistics"])
async def get_statistics():
    """الحصول على الإحصائيات"""
    try:
        stats = project_manager.get_statistics()
        all_stats = project_manager.get_all_statistics()
        return {
            "status": "success",
            "today": stats,
            "history": all_stats,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Health check
@app.get("/api/health", tags=["Health"])
async def health_check():
    """فحص صحة الخادم"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


# Root endpoint
@app.get("/", tags=["Info"])
async def root():
    """معلومات الـ API"""
    return {
        "name": "SA Platform API",
        "version": "1.0.0",
        "docs": "/docs",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
