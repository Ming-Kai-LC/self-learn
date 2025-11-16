"""
Audio Generation Utility for English Learning
Generates pronunciation audio using text-to-speech for vocabulary and sentences.
"""

import hashlib
import os
from pathlib import Path
from typing import List, Optional

from IPython.display import HTML, Audio, display


class AudioGenerator:
    """Generates and manages pronunciation audio files."""

    def __init__(self, audio_dir: str = "audio", use_gtts: bool = True):
        """
        Initialize the audio generator.

        Args:
            audio_dir: Directory to store generated audio files
            use_gtts: Use gTTS if True, pyttsx3 if False
        """
        self.audio_dir = Path(audio_dir)
        self.audio_dir.mkdir(parents=True, exist_ok=True)
        self.use_gtts = use_gtts

        # Try to import the appropriate TTS library
        self.tts_available = False
        self.tts_engine = None

        if use_gtts:
            try:
                from gtts import gTTS

                self.gTTS = gTTS
                self.tts_available = True
            except ImportError:
                print("WARNING: gTTS not installed. Install with: pip install gtts")
        else:
            try:
                import pyttsx3

                self.tts_engine = pyttsx3.init()
                self.tts_available = True
            except ImportError:
                print("WARNING: pyttsx3 not installed. Install with: pip install pyttsx3")

    def _get_audio_filename(self, text: str, accent: str = "us") -> str:
        """Generate a unique filename for the audio based on text content."""
        # Create a hash of the text to use as filename
        text_hash = hashlib.md5(f"{text}_{accent}".encode()).hexdigest()[:12]
        # Clean text for filename (first few words)
        clean_text = "".join(c if c.isalnum() else "_" for c in text[:30])
        return f"{clean_text}_{text_hash}.mp3"

    def generate_audio(self, text: str, accent: str = "us", slow: bool = False) -> Optional[str]:
        """
        Generate audio file from text.

        Args:
            text: The text to convert to speech
            accent: Accent/language code ('us', 'uk', 'au', etc.)
            slow: Whether to speak slowly (useful for beginners)

        Returns:
            Path to the generated audio file, or None if generation failed
        """
        if not self.tts_available:
            print("ERROR: Text-to-speech not available. Please install gTTS or pyttsx3.")
            return None

        filename = self._get_audio_filename(text, accent)
        filepath = self.audio_dir / filename

        # Check if file already exists
        if filepath.exists():
            return str(filepath)

        try:
            if self.use_gtts:
                # Map accent codes to gTTS language codes
                accent_map = {"us": "com", "uk": "co.uk", "au": "com.au", "in": "co.in"}
                tld = accent_map.get(accent, "com")

                tts = self.gTTS(text=text, lang="en", slow=slow, tld=tld)
                tts.save(str(filepath))
            else:
                # pyttsx3 doesn't support different accents easily, but we can adjust rate
                rate = self.tts_engine.getProperty("rate")
                self.tts_engine.setProperty("rate", rate - 50 if slow else rate)
                self.tts_engine.save_to_file(text, str(filepath))
                self.tts_engine.runAndWait()

            return str(filepath)

        except Exception as e:
            print(f"ERROR: Error generating audio: {e}")
            return None

    def play_audio(self, text: str, accent: str = "us", slow: bool = False, autoplay: bool = False):
        """
        Generate and play audio for the given text.

        Args:
            text: The text to speak
            accent: Accent/language code
            slow: Whether to speak slowly
            autoplay: Whether to autoplay the audio
        """
        audio_file = self.generate_audio(text, accent, slow)

        if audio_file and os.path.exists(audio_file):
            # Display text being spoken
            speed_label = " (slow)" if slow else ""
            display(
                HTML(f'<p style="color: #1976d2; font-style: italic;">🔊 "{text}"{speed_label}</p>')
            )

            # Display audio player
            display(Audio(audio_file, autoplay=autoplay))
        else:
            # Fallback: just display the text
            display(HTML(f'<p style="color: #666;">📝 "{text}" (audio not available)</p>'))

    def create_pronunciation_card(
        self,
        word: str,
        phonetic: str = "",
        definition: str = "",
        example: str = "",
        accent: str = "us",
    ):
        """
        Create a rich pronunciation card with audio.

        Args:
            word: The word to pronounce
            phonetic: Phonetic spelling (IPA)
            definition: Word definition
            example: Example sentence
            accent: Accent for pronunciation
        """
        # Generate audio for word and example
        word_audio = self.generate_audio(word, accent, slow=False)
        slow_audio = self.generate_audio(word, accent, slow=True)

        # Create HTML card
        phonetic_html = f"<p><strong>Phonetic:</strong> /{phonetic}/</p>" if phonetic else ""
        definition_html = f"<p><strong>Definition:</strong> {definition}</p>" if definition else ""
        example_html = f"<p><strong>Example:</strong> <em>{example}</em></p>" if example else ""

        html = f"""
        <div style="border: 2px solid #1976d2; border-radius: 10px; padding: 15px; margin: 10px 0; background-color: #f5f5f5;">
            <h3 style="color: #1976d2; margin-top: 0;">{word}</h3>
            {phonetic_html}
            {definition_html}
            {example_html}
        </div>
        """
        display(HTML(html))

        # Display audio players
        if word_audio and os.path.exists(word_audio):
            display(HTML("<p><strong>🔊 Normal speed:</strong></p>"))
            display(Audio(word_audio))

        if slow_audio and os.path.exists(slow_audio):
            display(HTML("<p><strong>🔊 Slow speed:</strong></p>"))
            display(Audio(slow_audio))

    def create_sentence_audio(
        self, sentence: str, accent: str = "us", label: str = "Listen to the sentence:"
    ):
        """
        Create audio for a full sentence with label.

        Args:
            sentence: The sentence to speak
            accent: Accent code
            label: Label to display
        """
        display(HTML(f'<p style="font-weight: bold; color: #333;">{label}</p>'))
        display(
            HTML(
                f'<p style="font-size: 16px; padding: 10px; background-color: #e3f2fd; border-left: 4px solid #1976d2;">"{sentence}"</p>'
            )
        )

        audio_file = self.generate_audio(sentence, accent, slow=False)
        if audio_file and os.path.exists(audio_file):
            display(Audio(audio_file))

    def create_conversation_audio(self, conversation: List[tuple], accent: str = "us"):
        """
        Create audio for a conversation/dialogue.

        Args:
            conversation: List of (speaker, text) tuples
            accent: Accent code
        """
        display(HTML("<h4>🗣️ Conversation:</h4>"))

        for speaker, text in conversation:
            # Display speaker and text
            display(
                HTML(
                    f'<p style="margin: 10px 0;"><strong style="color: #1976d2;">{speaker}:</strong> {text}</p>'
                )
            )

            # Generate and play audio
            audio_file = self.generate_audio(text, accent, slow=False)
            if audio_file and os.path.exists(audio_file):
                display(Audio(audio_file))

    def batch_generate(
        self, texts: List[str], accent: str = "us", slow: bool = False
    ) -> List[Optional[str]]:
        """
        Generate multiple audio files at once.

        Args:
            texts: List of texts to convert
            accent: Accent code
            slow: Whether to speak slowly

        Returns:
            List of file paths (or None for failed generations)
        """
        results = []
        for text in texts:
            result = self.generate_audio(text, accent, slow)
            results.append(result)
        return results


def create_pronunciation_guide():
    """Display a simple pronunciation guide for English sounds."""
    guide_html = """
    <div style="background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; margin: 20px 0;">
        <h3>📚 Pronunciation Guide</h3>
        <p><strong>Tips for better pronunciation:</strong></p>
        <ul>
            <li>Listen to the audio multiple times before trying to speak</li>
            <li>Use the slow speed option when learning new words</li>
            <li>Pay attention to word stress (the syllable that sounds louder)</li>
            <li>Record yourself and compare with the audio</li>
            <li>Practice regularly - even 5 minutes daily helps!</li>
        </ul>
    </div>
    """
    display(HTML(guide_html))


def create_audio_player_with_transcript(audio_file: str, transcript: str):
    """Display an audio player with its transcript."""
    if os.path.exists(audio_file):
        display(
            HTML(
                f'<p style="background-color: #e8f5e9; padding: 10px; border-radius: 5px;"><strong>Transcript:</strong> {transcript}</p>'
            )
        )
        display(Audio(audio_file))
    else:
        display(HTML(f'<p style="color: #666;">📝 {transcript}</p>'))
        display(HTML(f'<p style="color: #999; font-size: 12px;">(Audio file not found)</p>'))
