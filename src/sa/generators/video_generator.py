"""Text-to-Video Generator"""

import os

import replicate
from moviepy.editor import (
    AudioFileClip,
    CompositeAudioClip,
    ImageClip,
    VideoFileClip,
    concatenate_videoclips,
)


class VideoGenerator:
    """Generate videos from text prompts and combine with audio"""

    def __init__(self, api_key: str | None = None):
        """
        Initialize the video generator

        Args:
            api_key: API key for video generation API
        """
        self.api_key = api_key or os.getenv("REPLICATE_API_TOKEN")
        if self.api_key:
            os.environ["REPLICATE_API_TOKEN"] = self.api_key

    def generate_from_text(self, prompt: str, duration: int = 5, fps: int = 24) -> str | None:
        """
        Generate video from text prompt

        Args:
            prompt: Text description of the video
            duration: Video duration in seconds
            fps: Frames per second

        Returns:
            Video URL or None if failed
        """
        try:
            output = replicate.run(
                "anotherjesse/zeroscope-v2-xl",
                input={"prompt": prompt, "num_frames": duration * fps},
            )
            return output if isinstance(output, str) else output[0]
        except Exception as e:
            print(f"Error generating video: {e}")
            return None

    def create_slideshow(
        self,
        image_paths: list[str],
        duration_per_image: int = 3,
        output_path: str = "output.mp4",
    ) -> str | None:
        """
        Create slideshow video from images

        Args:
            image_paths: List of image file paths
            duration_per_image: Duration for each image in seconds
            output_path: Path to save the video

        Returns:
            Path to created video or None if failed
        """
        try:
            clips = []
            for img_path in image_paths:
                clip = ImageClip(img_path, duration=duration_per_image)
                clips.append(clip)

            video = concatenate_videoclips(clips, method="compose")
            video.write_videofile(output_path, fps=24)
            return output_path
        except Exception as e:
            print(f"Error creating slideshow: {e}")
            return None

    def add_audio(
        self,
        video_path: str,
        audio_path: str,
        output_path: str = "output_with_audio.mp4",
    ) -> str | None:
        """
        Add audio to video

        Args:
            video_path: Path to video file
            audio_path: Path to audio file
            output_path: Path to save the output

        Returns:
            Path to video with audio or None if failed
        """
        try:
            video = VideoFileClip(video_path)
            audio = AudioFileClip(audio_path)

            # Trim audio to video length or loop it
            if audio.duration < video.duration:
                audio = audio.audio_loop(duration=video.duration)
            else:
                audio = audio.subclip(0, video.duration)

            video = video.set_audio(audio)
            video.write_videofile(output_path, codec="libx264", audio_codec="aac")
            return output_path
        except Exception as e:
            print(f"Error adding audio: {e}")
            return None

    def add_background_sounds(
        self,
        video_path: str,
        voice_audio: str,
        background_audio: str,
        background_volume: float = 0.3,
        output_path: str = "output_mixed.mp4",
    ) -> str | None:
        """
        Mix voice and background audio and add to video

        Args:
            video_path: Path to video file
            voice_audio: Path to voice audio file
            background_audio: Path to background audio file
            background_volume: Volume level for background (0.0 to 1.0)
            output_path: Path to save the output

        Returns:
            Path to video with mixed audio or None if failed
        """
        try:
            video = VideoFileClip(video_path)
            voice = AudioFileClip(voice_audio)
            background = AudioFileClip(background_audio)

            # Adjust background volume
            background = background.volumex(background_volume)

            # Loop background to match video duration
            if background.duration < video.duration:
                background = background.audio_loop(duration=video.duration)
            else:
                background = background.subclip(0, video.duration)

            # Mix voice and background
            if voice.duration < video.duration:
                voice = voice.set_duration(video.duration)

            mixed_audio = CompositeAudioClip([voice, background])
            video = video.set_audio(mixed_audio)

            video.write_videofile(output_path, codec="libx264", audio_codec="aac")
            return output_path
        except Exception as e:
            print(f"Error mixing audio: {e}")
            return None

    def enhance_prompt(self, prompt: str) -> str:
        """
        Enhance prompt for better video generation

        Args:
            prompt: Original prompt

        Returns:
            Enhanced prompt
        """
        return f"{prompt}, cinematic, smooth motion, high quality, 4k"
