"""AI-powered suggestion system for content generation"""

from typing import List, Dict, Optional
import openai
import os


class SuggestionEngine:
    """Generate smart suggestions for prompts and improvements"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the suggestion engine

        Args:
            api_key: OpenAI API key
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if self.api_key:
            openai.api_key = self.api_key

    def improve_prompt(self, prompt: str, content_type: str = "image") -> str:
        """
        Improve user prompt using AI

        Args:
            prompt: Original user prompt
            content_type: Type of content (image, video, audio)

        Returns:
            Improved prompt
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are an expert in creating detailed prompts for {content_type} generation. Improve the user's prompt to be more detailed and effective.",
                    },
                    {"role": "user", "content": f"Improve this prompt: {prompt}"},
                ],
                max_tokens=200,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error improving prompt: {e}")
            return self._fallback_improve(prompt, content_type)

    def _fallback_improve(self, prompt: str, content_type: str) -> str:
        """Fallback improvement without API"""
        enhancements = {
            "image": "detailed, high quality, professional, 8k resolution",
            "video": "cinematic, smooth motion, high quality, 4k",
            "audio": "clear, professional quality, well-paced",
        }
        return f"{prompt}, {enhancements.get(content_type, 'high quality')}"

    def generate_variations(self, prompt: str, count: int = 5) -> List[str]:
        """
        Generate prompt variations

        Args:
            prompt: Base prompt
            count: Number of variations to generate

        Returns:
            List of prompt variations
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Generate creative variations of the given prompt. Each variation should be on a new line.",
                    },
                    {
                        "role": "user",
                        "content": f"Generate {count} variations of this prompt: {prompt}",
                    },
                ],
                max_tokens=300,
            )
            content = response.choices[0].message.content.strip()
            return [line.strip() for line in content.split("\n") if line.strip()][
                :count
            ]
        except Exception as e:
            print(f"Error generating variations: {e}")
            return self._fallback_variations(prompt, count)

    def _fallback_variations(self, prompt: str, count: int) -> List[str]:
        """Generate variations without API"""
        styles = [
            "realistic style",
            "artistic style",
            "modern style",
            "classic style",
            "minimalist style",
            "detailed style",
        ]
        return [f"{prompt} in {style}" for style in styles[:count]]

    def suggest_next_scene(self, current_scene: str) -> List[str]:
        """
        Suggest next scenes for video storytelling

        Args:
            current_scene: Description of current scene

        Returns:
            List of suggested next scenes
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a creative storyteller. Suggest logical next scenes.",
                    },
                    {
                        "role": "user",
                        "content": f"Current scene: {current_scene}\nSuggest 3 possible next scenes:",
                    },
                ],
                max_tokens=200,
            )
            content = response.choices[0].message.content.strip()
            return [line.strip() for line in content.split("\n") if line.strip()]
        except Exception as e:
            print(f"Error suggesting scenes: {e}")
            return [
                f"Continue from: {current_scene}",
                f"Transition to a different location",
                f"Close-up detail from the scene",
            ]

    def suggest_music_mood(self, scene_description: str) -> Dict[str, str]:
        """
        Suggest appropriate music mood for a scene

        Args:
            scene_description: Description of the scene

        Returns:
            Dictionary with mood, tempo, and genre suggestions
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Suggest appropriate background music characteristics.",
                    },
                    {
                        "role": "user",
                        "content": f"Scene: {scene_description}\nSuggest: mood, tempo, genre",
                    },
                ],
                max_tokens=100,
            )
            content = response.choices[0].message.content.strip()

            # Parse response
            lines = content.lower().split("\n")
            result = {"mood": "calm", "tempo": "medium", "genre": "ambient"}

            for line in lines:
                if "mood" in line:
                    result["mood"] = line.split(":")[-1].strip()
                elif "tempo" in line:
                    result["tempo"] = line.split(":")[-1].strip()
                elif "genre" in line:
                    result["genre"] = line.split(":")[-1].strip()

            return result
        except Exception as e:
            print(f"Error suggesting music: {e}")
            return {"mood": "calm", "tempo": "medium", "genre": "ambient"}

    def generate_script_from_idea(self, idea: str) -> List[Dict[str, str]]:
        """
        Generate a complete script from an idea

        Args:
            idea: Basic story idea

        Returns:
            List of scene dictionaries with text and visuals
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Create a video script with scene descriptions and narration.",
                    },
                    {
                        "role": "user",
                        "content": f"Create a 5-scene video script for: {idea}\nFormat each scene as: Scene X: [visual description] | Narration: [text]",
                    },
                ],
                max_tokens=500,
            )
            content = response.choices[0].message.content.strip()

            # Parse scenes
            scenes = []
            for line in content.split("\n"):
                if "|" in line and ":" in line:
                    parts = line.split("|")
                    visual = parts[0].split(":", 1)[-1].strip()
                    narration = parts[1].split(":", 1)[-1].strip()
                    scenes.append({"visual": visual, "narration": narration})

            return scenes if scenes else self._fallback_script(idea)
        except Exception as e:
            print(f"Error generating script: {e}")
            return self._fallback_script(idea)

    def _fallback_script(self, idea: str) -> List[Dict[str, str]]:
        """Generate basic script without API"""
        return [
            {
                "visual": f"Opening scene: {idea}",
                "narration": f"Introduction to {idea}",
            },
            {"visual": f"Main content about {idea}", "narration": "Main story unfolds"},
            {"visual": "Climax or key moment", "narration": "The most important part"},
            {"visual": "Resolution", "narration": "How things conclude"},
            {"visual": "Closing scene", "narration": "Final thoughts"},
        ]
