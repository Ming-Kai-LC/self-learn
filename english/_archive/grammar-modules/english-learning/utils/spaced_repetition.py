"""
Spaced Repetition System for English Learning
Implements a SuperMemo-inspired algorithm for optimal review scheduling.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
from IPython.display import HTML, display


class SpacedRepetitionScheduler:
    """Manages spaced repetition schedule for grammar modules."""

    def __init__(self, data_file: str = "data/progress.json"):
        """
        Initialize the spaced repetition scheduler.

        Args:
            data_file: Path to JSON file storing progress data
        """
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)

        # Load or initialize progress data
        self.progress = self._load_progress()

        # Spaced repetition intervals (in days)
        self.intervals = [1, 2, 4, 7, 14, 30, 60, 120]  # Review schedule

    def _load_progress(self) -> Dict:
        """Load progress data from JSON file."""
        if self.data_file.exists():
            try:
                with open(self.data_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Warning: Could not read progress file. Starting fresh.")
                return {}
        return {}

    def _save_progress(self):
        """Save progress data to JSON file."""
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.progress, f, indent=2, ensure_ascii=False)

    def mark_module_complete(self, module_id: str, module_name: str, score: float = 100.0):
        """
        Mark a module as completed and schedule first review.

        Args:
            module_id: Unique module identifier (e.g., "A1_Module_01")
            module_name: Human-readable module name
            score: Completion score (0-100)
        """
        if module_id not in self.progress:
            self.progress[module_id] = {
                "name": module_name,
                "completed_date": datetime.now().isoformat(),
                "review_count": 0,
                "scores": [],
                "next_review": None,
                "last_review": None,
                "interval_index": 0,
            }

        self.progress[module_id]["scores"].append(score)

        # Schedule next review
        self._schedule_next_review(module_id)
        self._save_progress()

        display(
            HTML(
                f"""
            <div style="background-color: #d4edda; border-left: 5px solid #28a745; padding: 15px; margin: 10px 0;">
                <h4 style="color: #155724; margin-top: 0;">✅ Module Completed!</h4>
                <p style="margin: 5px 0;"><strong>Module:</strong> {module_name}</p>
                <p style="margin: 5px 0;"><strong>Score:</strong> {score:.1f}%</p>
                <p style="margin: 5px 0;"><strong>Next Review:</strong> {self.progress[module_id]['next_review']}</p>
            </div>
        """
            )
        )

    def _schedule_next_review(self, module_id: str):
        """Calculate and set the next review date for a module."""
        module_data = self.progress[module_id]
        interval_index = module_data["interval_index"]

        # Get interval in days
        if interval_index < len(self.intervals):
            days = self.intervals[interval_index]
        else:
            days = self.intervals[-1]  # Use maximum interval

        # Calculate next review date
        if module_data["last_review"]:
            last_review = datetime.fromisoformat(module_data["last_review"])
        else:
            last_review = datetime.fromisoformat(module_data["completed_date"])

        next_review = last_review + timedelta(days=days)
        module_data["next_review"] = next_review.strftime("%Y-%m-%d")

    def mark_review_complete(self, module_id: str, score: float):
        """
        Mark a review session as complete and schedule next review.

        Args:
            module_id: Module identifier
            score: Review score (0-100)
        """
        if module_id not in self.progress:
            print(f"❌ Module {module_id} not found in progress data.")
            return

        module_data = self.progress[module_id]
        module_data["review_count"] += 1
        module_data["scores"].append(score)
        module_data["last_review"] = datetime.now().isoformat()

        # Adjust interval based on performance
        if score >= 80:
            # Good performance - move to next interval
            module_data["interval_index"] = min(
                module_data["interval_index"] + 1, len(self.intervals) - 1
            )
        elif score < 60:
            # Poor performance - reset to shorter interval
            module_data["interval_index"] = max(0, module_data["interval_index"] - 1)

        # Schedule next review
        self._schedule_next_review(module_id)
        self._save_progress()

        display(
            HTML(
                f"""
            <div style="background-color: #cfe2ff; border-left: 5px solid #0d6efd; padding: 15px; margin: 10px 0;">
                <h4 style="color: #084298; margin-top: 0;">📝 Review Completed!</h4>
                <p style="margin: 5px 0;"><strong>Score:</strong> {score:.1f}%</p>
                <p style="margin: 5px 0;"><strong>Next Review:</strong> {module_data['next_review']}</p>
                <p style="margin: 5px 0;"><strong>Total Reviews:</strong> {module_data['review_count']}</p>
            </div>
        """
            )
        )

    def get_due_reviews(self) -> List[Dict]:
        """
        Get list of modules due for review today.

        Returns:
            List of module dictionaries with review information
        """
        today = datetime.now().date()
        due_reviews = []

        for module_id, data in self.progress.items():
            if data["next_review"]:
                review_date = datetime.fromisoformat(data["next_review"]).date()
                if review_date <= today:
                    due_reviews.append(
                        {
                            "module_id": module_id,
                            "module_name": data["name"],
                            "next_review": data["next_review"],
                            "review_count": data["review_count"],
                            "avg_score": (
                                sum(data["scores"]) / len(data["scores"]) if data["scores"] else 0
                            ),
                        }
                    )

        return sorted(due_reviews, key=lambda x: x["next_review"])

    def get_upcoming_reviews(self, days: int = 7) -> List[Dict]:
        """
        Get reviews due within the next N days.

        Args:
            days: Number of days to look ahead

        Returns:
            List of upcoming review modules
        """
        today = datetime.now().date()
        future_date = today + timedelta(days=days)
        upcoming = []

        for module_id, data in self.progress.items():
            if data["next_review"]:
                review_date = datetime.fromisoformat(data["next_review"]).date()
                if today < review_date <= future_date:
                    upcoming.append(
                        {
                            "module_id": module_id,
                            "module_name": data["name"],
                            "next_review": data["next_review"],
                            "days_until": (review_date - today).days,
                            "review_count": data["review_count"],
                        }
                    )

        return sorted(upcoming, key=lambda x: x["next_review"])

    def display_review_dashboard(self):
        """Display an interactive review dashboard."""
        due = self.get_due_reviews()
        upcoming = self.get_upcoming_reviews()

        # Header
        display(
            HTML(
                """
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white; padding: 20px; border-radius: 10px; margin: 20px 0;">
                <h2 style="margin: 0;">📅 Spaced Repetition Dashboard</h2>
                <p style="margin: 5px 0; opacity: 0.9;">Track your review schedule and maintain long-term retention</p>
            </div>
        """
            )
        )

        # Due reviews
        if due:
            display(
                HTML(
                    f"""
                <div style="background-color: #fff3cd; border-left: 5px solid #ffc107;
                            padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <h3 style="color: #856404; margin-top: 0;">⚠️ {len(due)} Module(s) Due for Review</h3>
                </div>
            """
                )
            )

            df_due = pd.DataFrame(due)
            df_due = df_due[["module_name", "next_review", "review_count", "avg_score"]]
            df_due.columns = ["Module", "Due Date", "Reviews", "Avg Score"]
            df_due["Avg Score"] = df_due["Avg Score"].apply(lambda x: f"{x:.1f}%")

            display(
                HTML(
                    df_due.to_html(
                        index=False, escape=False, classes="table table-striped", border=0
                    )
                )
            )
        else:
            display(
                HTML(
                    """
                <div style="background-color: #d4edda; border-left: 5px solid #28a745;
                            padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <p style="color: #155724; margin: 0;">✅ No reviews due today! Great job staying on track!</p>
                </div>
            """
                )
            )

        # Upcoming reviews
        if upcoming:
            display(
                HTML(
                    f"""
                <div style="background-color: #d1ecf1; border-left: 5px solid #0c5460;
                            padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <h3 style="color: #0c5460; margin-top: 0;">📆 Upcoming Reviews (Next 7 Days)</h3>
                </div>
            """
                )
            )

            df_upcoming = pd.DataFrame(upcoming)
            df_upcoming = df_upcoming[["module_name", "next_review", "days_until", "review_count"]]
            df_upcoming.columns = ["Module", "Review Date", "Days Until", "Total Reviews"]

            display(
                HTML(
                    df_upcoming.to_html(
                        index=False, escape=False, classes="table table-striped", border=0
                    )
                )
            )

    def get_module_stats(self, module_id: str) -> Optional[Dict]:
        """
        Get detailed statistics for a specific module.

        Args:
            module_id: Module identifier

        Returns:
            Dictionary with module statistics or None if not found
        """
        if module_id not in self.progress:
            return None

        data = self.progress[module_id]
        scores = data["scores"]

        return {
            "module_name": data["name"],
            "completed_date": data["completed_date"],
            "review_count": data["review_count"],
            "next_review": data["next_review"],
            "average_score": sum(scores) / len(scores) if scores else 0,
            "latest_score": scores[-1] if scores else 0,
            "all_scores": scores,
        }

    def reset_module(self, module_id: str):
        """Reset a module's progress (useful for relearning)."""
        if module_id in self.progress:
            del self.progress[module_id]
            self._save_progress()
            print(f"✅ Module {module_id} has been reset.")
        else:
            print(f"❌ Module {module_id} not found.")

    def export_progress_report(self) -> pd.DataFrame:
        """
        Export full progress report as a DataFrame.

        Returns:
            DataFrame with all module progress
        """
        if not self.progress:
            return pd.DataFrame()

        report_data = []
        for module_id, data in self.progress.items():
            report_data.append(
                {
                    "Module ID": module_id,
                    "Module Name": data["name"],
                    "Completed": data["completed_date"][:10],
                    "Reviews": data["review_count"],
                    "Avg Score": (
                        f"{sum(data['scores']) / len(data['scores']):.1f}%"
                        if data["scores"]
                        else "N/A"
                    ),
                    "Next Review": data["next_review"],
                    "Status": (
                        "Due"
                        if data["next_review"]
                        and datetime.fromisoformat(data["next_review"]).date()
                        <= datetime.now().date()
                        else "Scheduled"
                    ),
                }
            )

        return pd.DataFrame(report_data)


def create_review_reminder():
    """Display a reminder about the importance of spaced repetition."""
    html = """
    <div style="background-color: #e7f3ff; border: 2px solid #2196F3; border-radius: 10px; padding: 20px; margin: 20px 0;">
        <h3 style="color: #1976D2; margin-top: 0;">🧠 Why Spaced Repetition Works</h3>
        <p>Spaced repetition is scientifically proven to improve long-term retention by up to <strong>200%</strong>!</p>
        <ul style="line-height: 1.8;">
            <li><strong>Day 1:</strong> Review within 24 hours (prevents 80% forgetting)</li>
            <li><strong>Day 2-4:</strong> Second review (consolidates memory)</li>
            <li><strong>Week 1-2:</strong> Third review (builds long-term retention)</li>
            <li><strong>Monthly+:</strong> Maintenance reviews (ensures mastery)</li>
        </ul>
        <p style="margin-bottom: 0;"><em>💡 Tip: Don't cram! Short, regular review sessions are more effective than long, infrequent ones.</em></p>
    </div>
    """
    display(HTML(html))
