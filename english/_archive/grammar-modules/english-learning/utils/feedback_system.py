"""
Interactive Feedback System for English Learning Notebooks
Provides exercise validation, immediate feedback, and progress tracking.
"""

import random
from typing import Callable, Dict, List, Tuple

import ipywidgets as widgets
from IPython.display import HTML, clear_output, display


class ExerciseValidator:
    """Validates user answers and provides constructive feedback."""

    def __init__(self):
        self.attempts = {}
        self.correct_count = 0
        self.total_count = 0

    def check_answer(
        self,
        user_answer: str,
        correct_answer: str,
        case_sensitive: bool = False,
        strip_whitespace: bool = True,
    ) -> Tuple[bool, str]:
        """
        Check if user answer matches the correct answer.

        Args:
            user_answer: The answer provided by the user
            correct_answer: The expected correct answer
            case_sensitive: Whether to check case
            strip_whitespace: Whether to strip leading/trailing whitespace

        Returns:
            Tuple of (is_correct, feedback_message)
        """
        if strip_whitespace:
            user_answer = user_answer.strip()
            correct_answer = correct_answer.strip()

        if not case_sensitive:
            user_answer = user_answer.lower()
            correct_answer = correct_answer.lower()

        is_correct = user_answer == correct_answer

        if is_correct:
            feedback = "✅ Correct! Well done!"
            self.correct_count += 1
        else:
            feedback = f"❌ Not quite. The correct answer is: <strong>{correct_answer}</strong>"

        self.total_count += 1
        return is_correct, feedback

    def check_multiple_choice(
        self, user_answer: str, correct_answer: str, explanation: str = ""
    ) -> Tuple[bool, str]:
        """
        Check multiple choice answer with optional explanation.

        Args:
            user_answer: User's selected choice
            correct_answer: The correct choice
            explanation: Additional explanation for why this is correct

        Returns:
            Tuple of (is_correct, feedback_message)
        """
        is_correct = user_answer.strip().upper() == correct_answer.strip().upper()

        if is_correct:
            feedback = f"✅ Correct! {explanation}" if explanation else "✅ Correct!"
            self.correct_count += 1
        else:
            feedback = f"❌ Incorrect. The correct answer is <strong>{correct_answer}</strong>. {explanation}"

        self.total_count += 1
        return is_correct, feedback

    def check_fill_in_blank(
        self, user_answer: str, possible_answers: List[str], explanation: str = ""
    ) -> Tuple[bool, str]:
        """
        Check fill-in-the-blank with multiple possible correct answers.

        Args:
            user_answer: User's answer
            possible_answers: List of acceptable answers
            explanation: Additional explanation

        Returns:
            Tuple of (is_correct, feedback_message)
        """
        user_clean = user_answer.strip().lower()
        is_correct = any(user_clean == ans.strip().lower() for ans in possible_answers)

        if is_correct:
            feedback = f"✅ Correct! {explanation}" if explanation else "✅ Correct!"
            self.correct_count += 1
        else:
            correct_list = " / ".join(possible_answers)
            feedback = (
                f"❌ Not quite. Acceptable answers: <strong>{correct_list}</strong>. {explanation}"
            )

        self.total_count += 1
        return is_correct, feedback

    def get_score(self) -> Tuple[int, int, float]:
        """
        Get current score statistics.

        Returns:
            Tuple of (correct_count, total_count, percentage)
        """
        percentage = (self.correct_count / self.total_count * 100) if self.total_count > 0 else 0
        return self.correct_count, self.total_count, percentage

    def reset_score(self):
        """Reset the score counter."""
        self.correct_count = 0
        self.total_count = 0
        self.attempts = {}

    def display_score(self):
        """Display current score with visual feedback."""
        correct, total, percentage = self.get_score()

        if percentage >= 80:
            color = "green"
            message = "Excellent work! 🌟"
        elif percentage >= 60:
            color = "orange"
            message = "Good progress! Keep practicing! 👍"
        else:
            color = "red"
            message = "Keep trying! Practice makes perfect! 💪"

        html = f"""
        <div style="padding: 15px; background-color: #f0f0f0; border-left: 5px solid {color}; margin: 10px 0;">
            <h3 style="margin: 0; color: {color};">Your Score: {correct}/{total} ({percentage:.1f}%)</h3>
            <p style="margin: 5px 0 0 0;">{message}</p>
        </div>
        """
        display(HTML(html))


class InteractiveExercise:
    """Creates interactive exercises with immediate feedback."""

    def __init__(self, validator: ExerciseValidator = None):
        self.validator = validator or ExerciseValidator()
        self.current_widget = None

    def create_fill_in_blank(
        self, question: str, correct_answer: str, placeholder: str = "Type your answer here"
    ):
        """Create an interactive fill-in-the-blank exercise."""
        text_input = widgets.Text(
            placeholder=placeholder, description="Answer:", style={"description_width": "initial"}
        )

        submit_button = widgets.Button(
            description="Check Answer", button_style="info", icon="check"
        )

        feedback_output = widgets.Output()

        def on_submit(b):
            with feedback_output:
                clear_output()
                is_correct, message = self.validator.check_answer(text_input.value, correct_answer)
                color = "green" if is_correct else "red"
                display(HTML(f'<p style="color: {color}; font-weight: bold;">{message}</p>'))

                if is_correct:
                    submit_button.disabled = True
                    text_input.disabled = True

        submit_button.on_click(on_submit)

        display(HTML(f"<p><strong>{question}</strong></p>"))
        display(widgets.HBox([text_input, submit_button]))
        display(feedback_output)

    def create_multiple_choice(
        self, question: str, options: Dict[str, str], correct_answer: str, explanation: str = ""
    ):
        """
        Create a multiple choice exercise.

        Args:
            question: The question text
            options: Dict mapping option keys (A, B, C, D) to option text
            correct_answer: The correct option key
            explanation: Optional explanation
        """
        radio_buttons = widgets.RadioButtons(
            options=[(f"{key}. {value}", key) for key, value in options.items()],
            description="",
            disabled=False,
        )

        submit_button = widgets.Button(
            description="Submit Answer", button_style="info", icon="check"
        )

        feedback_output = widgets.Output()

        def on_submit(b):
            with feedback_output:
                clear_output()
                if radio_buttons.value is None:
                    display(HTML('<p style="color: orange;">Please select an answer first!</p>'))
                    return

                is_correct, message = self.validator.check_multiple_choice(
                    radio_buttons.value, correct_answer, explanation
                )
                color = "green" if is_correct else "red"
                display(HTML(f'<p style="color: {color};">{message}</p>'))

                if is_correct:
                    submit_button.disabled = True
                    radio_buttons.disabled = True

        submit_button.on_click(on_submit)

        display(HTML(f"<p><strong>{question}</strong></p>"))
        display(radio_buttons)
        display(submit_button)
        display(feedback_output)

    def create_matching_exercise(
        self, items: List[Tuple[str, str]], instructions: str = "Match the items:"
    ):
        """Create a matching exercise with drag-and-drop simulation."""
        # Simplified version using dropdowns
        display(HTML(f"<h4>{instructions}</h4>"))

        left_items, right_items = zip(*items)
        shuffled_right = list(right_items)
        random.shuffle(shuffled_right)

        dropdowns = []
        for i, left_item in enumerate(left_items):
            dropdown = widgets.Dropdown(
                options=shuffled_right,
                description=f"{left_item}:",
                style={"description_width": "initial"},
            )
            dropdowns.append((dropdown, right_items[i]))
            display(dropdown)

        submit_button = widgets.Button(
            description="Check Answers", button_style="info", icon="check"
        )

        feedback_output = widgets.Output()

        def on_submit(b):
            with feedback_output:
                clear_output()
                correct = 0
                for dropdown, correct_match in dropdowns:
                    if dropdown.value == correct_match:
                        correct += 1

                total = len(dropdowns)
                percentage = (correct / total) * 100
                color = "green" if percentage >= 80 else "orange" if percentage >= 60 else "red"

                self.validator.correct_count += correct
                self.validator.total_count += total

                display(
                    HTML(
                        f'<p style="color: {color}; font-weight: bold;">You got {correct}/{total} correct ({percentage:.0f}%)</p>'
                    )
                )

                if percentage == 100:
                    submit_button.disabled = True
                    for dropdown, _ in dropdowns:
                        dropdown.disabled = True

        submit_button.on_click(on_submit)
        display(submit_button)
        display(feedback_output)


def create_progress_bar(current: int, total: int, label: str = "Progress") -> None:
    """Display a visual progress bar."""
    percentage = (current / total) * 100

    html = f"""
    <div style="margin: 20px 0;">
        <p style="margin: 5px 0;"><strong>{label}:</strong> {current}/{total} ({percentage:.0f}%)</p>
        <div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; overflow: hidden;">
            <div style="width: {percentage}%; background-color: #4CAF50; height: 25px; text-align: center; line-height: 25px; color: white; font-weight: bold;">
                {percentage:.0f}%
            </div>
        </div>
    </div>
    """
    display(HTML(html))


def display_hint(hint_text: str):
    """Display a collapsible hint."""
    hint_button = widgets.Button(
        description="💡 Show Hint", button_style="warning", icon="lightbulb-o"
    )

    hint_output = widgets.Output()

    def show_hint(b):
        with hint_output:
            clear_output()
            display(
                HTML(
                    f'<p style="background-color: #fff3cd; padding: 10px; border-left: 4px solid #ffc107;"><strong>Hint:</strong> {hint_text}</p>'
                )
            )
            b.disabled = True

    hint_button.on_click(show_hint)
    display(hint_button)
    display(hint_output)
