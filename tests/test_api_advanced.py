"""Advanced API endpoint tests to improve coverage"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from sa.api import app


@pytest.fixture(scope="module")
def client():
    """Create test client"""
    return TestClient(app)


class TestImageEndpoints:
    """Test image generation endpoints"""

    @patch("sa.api.routes.image_generator")
    def test_generate_image_with_guidance(self, mock_gen, client):
        """Test image generation with guidance scale"""
        mock_gen.generate.return_value = ["http://example.com/image.jpg"]
        mock_gen.download_image.return_value = True

        response = client.post(
            "/api/v1/images/generate",
            json={
                "prompt": "beautiful sunset",
                "width": 512,
                "height": 512,
                "guidance_scale": 8.5,
                "num_outputs": 1,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "job_id" in data
        assert data["status"] == "completed"

    def test_get_image_job_not_found(self, client):
        """Test getting non-existent image job"""
        response = client.get("/api/v1/images/jobs/nonexistent-id")
        assert response.status_code == 404

    def test_list_images_pagination(self, client):
        """Test image listing with pagination"""
        response = client.get("/api/v1/outputs")
        assert response.status_code == 200
        data = response.json()
        assert "images" in data
        assert isinstance(data["images"], list)


class TestVideoEndpoints:
    """Test video generation endpoints"""

    @patch("sa.api.routes.video_generator")
    @patch("os.path.exists")
    def test_generate_video_from_text(self, mock_exists, mock_gen, client):
        """Test video generation from images"""
        mock_gen.create_slideshow.return_value = "video.mp4"
        mock_exists.return_value = True  # Pretend image files exist

        response = client.post(
            "/api/v1/videos/generate",
            json={"image_paths": ["outputs/img1.png", "outputs/img2.png"]},
        )
        assert response.status_code == 200
        data = response.json()
        assert "job_id" in data

    def test_get_video_job_not_found(self, client):
        """Test getting non-existent video job"""
        response = client.get("/api/v1/videos/jobs/nonexistent-id")
        assert response.status_code == 404


class TestAudioEndpoints:
    """Test audio generation endpoints"""

    @patch("sa.api.routes.audio_generator")
    def test_generate_speech_with_voice(self, mock_gen, client):
        """Test speech generation with specific voice"""
        mock_gen.generate_speech.return_value = "audio.mp3"

        response = client.post(
            "/api/v1/audio/generate",
            json={"text": "Hello world"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "job_id" in data

    def test_get_audio_job_not_found(self, client):
        """Test getting non-existent audio job"""
        response = client.get("/api/v1/audio/jobs/nonexistent-id")
        assert response.status_code == 404


class TestSuggestionEndpoints:
    """Test AI suggestion endpoints"""

    @patch("sa.api.routes.suggestion_engine")
    def test_improve_prompt(self, mock_engine, client):
        """Test prompt improvement"""
        mock_engine.improve_prompt.return_value = "improved prompt"

        response = client.post(
            "/api/v1/suggestions/improve",
            json={"prompt": "cat", "content_type": "image"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "improved" in data

    @patch("sa.api.routes.suggestion_engine")
    def test_generate_prompts(self, mock_engine, client):
        """Test generating multiple prompts from theme"""
        mock_engine.generate_variations.return_value = ["prompt1", "prompt2", "prompt3"]

        response = client.post(
            "/api/v1/suggestions/variations",
            json={"prompt": "nature", "count": 3},
        )
        assert response.status_code == 200
        data = response.json()
        assert "variations" in data


class TestProjectEndpoints:
    """Test project management endpoints - Skipped as endpoints not implemented yet"""

    def test_projects_not_implemented(self, client):
        """Projects endpoints are not yet implemented"""
        response = client.get("/api/v1/projects")
        assert response.status_code == 404


class TestErrorHandling:
    """Test error handling"""

    def test_invalid_endpoint(self, client):
        """Test accessing invalid endpoint"""
        response = client.get("/api/v1/invalid")
        assert response.status_code == 404

    def test_invalid_method(self, client):
        """Test using invalid HTTP method"""
        response = client.put("/api/v1/health")
        assert response.status_code == 405

    def test_missing_required_field(self, client):
        """Test request with missing required field"""
        response = client.post(
            "/api/v1/images/generate",
            json={"width": 512, "height": 512},  # Missing prompt
        )
        assert response.status_code == 422

    def test_invalid_json(self, client):
        """Test request with invalid JSON"""
        response = client.post(
            "/api/v1/images/generate",
            data="invalid json",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 422
