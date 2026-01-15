"""Text-to-Image Generator using AI models"""

import os
from typing import Optional, Dict, Any
import replicate
from PIL import Image
import requests
from io import BytesIO


class ImageGenerator:
    """Generate images from text prompts using AI models"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the image generator

        Args:
            api_key: API key for Replicate (optional, uses env var if not provided)
        """
        self.api_key = api_key or os.getenv("REPLICATE_API_TOKEN")
        if self.api_key:
            os.environ["REPLICATE_API_TOKEN"] = self.api_key

    def generate(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: int = 1024,
        height: int = 1024,
        num_outputs: int = 1,
        model: str = "stability-ai/sdxl",
    ) -> list[str]:
        """
        Generate images from text prompt

        Args:
            prompt: Text description of the image to generate
            negative_prompt: Things to avoid in the image
            width: Image width
            height: Image height
            num_outputs: Number of images to generate
            model: AI model to use

        Returns:
            List of image URLs
        """
        try:
            output = replicate.run(
                model,
                input={
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "width": width,
                    "height": height,
                    "num_outputs": num_outputs,
                },
            )
            return list(output) if isinstance(output, (list, tuple)) else [output]
        except Exception as e:
            print(f"Error generating image: {e}")
            return []

    def enhance_prompt(self, prompt: str) -> str:
        """
        Enhance user prompt with better descriptions for AI generation

        Args:
            prompt: Original user prompt

        Returns:
            Enhanced prompt
        """
        enhancements = [
            "high quality",
            "detailed",
            "professional",
            "8k resolution",
            "photorealistic",
        ]

        return f"{prompt}, {', '.join(enhancements)}"

    def download_image(self, url: str, save_path: str) -> Optional[str]:
        """
        Download image from URL

        Args:
            url: Image URL
            save_path: Path to save the image

        Returns:
            Path to saved image or None if failed
        """
        try:
            response = requests.get(url)
            response.raise_for_status()

            img = Image.open(BytesIO(response.content))
            img.save(save_path)
            return save_path
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None

    def get_suggestions(self, base_prompt: str) -> list[str]:
        """
        Get prompt suggestions for variations

        Args:
            base_prompt: Base prompt to build suggestions from

        Returns:
            List of suggested prompts
        """
        styles = [
            "in anime style",
            "in realistic style",
            "in watercolor painting style",
            "in digital art style",
            "in 3D render style",
            "in oil painting style",
        ]

        return [f"{base_prompt} {style}" for style in styles]
