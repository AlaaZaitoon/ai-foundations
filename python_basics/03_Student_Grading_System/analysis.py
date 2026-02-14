"""
Project: Student Grading System
Author: Alaa Zaitoon
Description:
    A compact grading analytics system that:
    - Accepts a classroom dictionary: {student_name: [scores]}
    - Silently validates/sanitizes scores (keeps only numeric values within a valid range)
    - Generates per-student analytics (avg/best/worst/pass-grade)
    - Produces class-level summary + Top N ranking
    - Prints a clean, professional report
"""

import statistics as st


class StudentGradingSystem:
    # ---------------------------
    # Configuration / Setup
    # ---------------------------
    def __init__(self, classroom_data, pass_mark=50, min_score=0, max_score=100):
        """
        classroom_data: dict[str, list]
            Example: {"Alaa": [85, 92], "Sara": [95, 88]}
        pass_mark: float
            Minimum average required to pass
        min_score/max_score: float
            Allowed score range
        """
        self.classroom_data = classroom_data
        self.pass_mark = float(pass_mark)
        self.min_score = float(min_score)
        self.max_score = float(max_score)

    # ---------------------------
    # Utilities (private helpers)
    # ---------------------------
    def _sanitize_scores(self, scores):
        """
        Silently keep only valid numeric scores within the allowed range.
        Returns a list[float]. If nothing valid remains, returns an empty list.
        """
        if not isinstance(scores, (list, tuple)):
            return []

        cleaned = []
        for s in scores:
            if isinstance(s, (int, float)) and self.min_score <= s <= self.max_score:
                cleaned.append(float(s))
        return cleaned

    def _grade_letter(self, avg):
        """
        Converts a numeric average into a letter grade.
        A: 90-100, B: 80-89, C: 70-79, D: 50-69, F: <50
        """
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 50:
            return "D"
        return "F"

    # ---------------------------
    # Core Logic (reports & stats)
    # ---------------------------
    def build_student_reports(self):
        """
        Builds a list of per-student reports.
        Each report is a dict with: name, avg, best, worst, status, grade, scores_count
        """
        reports = []

        if not isinstance(self.classroom_data, dict):
            return reports

        for name, scores in self.classroom_data.items():
            cleaned = self._sanitize_scores(scores)

            # If no valid data, keep the student in the report with NO DATA fields
            if not cleaned:
                reports.append({
                    "name": str(name),
                    "scores_count": 0,
                    "avg": None,
                    "best": None,
                    "worst": None,
                    "status": "NO DATA",
                    "grade": "-"
                })
                continue

            avg = float(st.mean(cleaned))
            best = float(max(cleaned))
            worst = float(min(cleaned))

            status = "PASSED" if avg >= self.pass_mark else "FAILED"
            grade = self._grade_letter(avg)

            reports.append({
                "name": str(name),
                "scores_count": len(cleaned),
                "avg": avg,
                "best": best,
                "worst": worst,
                "status": status,
                "grade": grade
            })

        return reports

    def build_class_summary(self, reports):
        """
        Creates class-level summary based on valid students only.
        """
        valid = [r for r in reports if r["avg"] is not None]

        summary = {
            "students_total": len(reports),
            "students_valid": len(valid),
            "class_avg": None,
            "pass_rate": None,
            "top_student": None,
            "bottom_student": None
        }

        if not valid:
            return summary

        class_avg = float(st.mean([r["avg"] for r in valid]))
        passed = sum(1 for r in valid if r["avg"] >= self.pass_mark)
        pass_rate = (passed / len(valid)) * 100

        top_student = max(valid, key=lambda r: r["avg"])
        bottom_student = min(valid, key=lambda r: r["avg"])

        summary.update({
            "class_avg": class_avg,
            "pass_rate": float(pass_rate),
            "top_student": top_student["name"],
            "bottom_student": bottom_student["name"]
        })

        return summary

    def top_n_students(self, reports, n=3):
        """
        Returns Top N students by average (valid only), sorted descending.
        """
        valid = [r for r in reports if r["avg"] is not None]
        valid_sorted = sorted(valid, key=lambda r: r["avg"], reverse=True)
        return valid_sorted[:n]

    # ---------------------------
    # Presentation (clean output)
    # ---------------------------
    def print_report(self, top_n=3):
        """
        Prints:
        - A table-like student report
        - Class summary
        - Top N ranking
        """
        reports = self.build_student_reports()
        summary = self.build_class_summary(reports)
        top_list = self.top_n_students(reports, n=top_n)

        print("\n" + "=" * 72)
        print("STUDENT GRADING SYSTEM - PERFORMANCE REPORT")
        print("=" * 72)

        # Table header (fixed-width formatting)
        header = f"{'Name':<14} | {'Avg':>6} | {'Best':>6} | {'Worst':>6} | {'Grade':^5} | {'Status':<10} | {'#Scores':>7}"
        print(header)
        print("-" * len(header))

        for r in reports:
            if r["avg"] is None:
                row = f"{r['name']:<14} | {'-':>6} | {'-':>6} | {'-':>6} | {'-':^5} | {r['status']:<10} | {r['scores_count']:>7}"
            else:
                row = f"{r['name']:<14} | {r['avg']:>6.2f} | {r['best']:>6.0f} | {r['worst']:>6.0f} | {r['grade']:^5} | {r['status']:<10} | {r['scores_count']:>7}"
            print(row)

        print("=" * 72)
        print("CLASS SUMMARY")
        print("-" * 72)

        print(f"Students (total) : {summary['students_total']}")
        print(f"Students (valid) : {summary['students_valid']}")

        if summary["class_avg"] is None:
            print("Class Average    : -")
            print("Pass Rate        : -")
            print("Top Student      : -")
            print("Bottom Student   : -")
        else:
            print(f"Class Average    : {summary['class_avg']:.2f}")
            print(f"Pass Rate        : {summary['pass_rate']:.2f}%")
            print(f"Top Student      : {summary['top_student']}")
            print(f"Bottom Student   : {summary['bottom_student']}")

        print("=" * 72)
        print(f"TOP {top_n} RANKING")
        print("-" * 72)

        if not top_list:
            print("No ranked students available.")
        else:
            for i, r in enumerate(top_list, start=1):
                print(f"{i}) {r['name']}  - Avg: {r['avg']:.2f} | Grade: {r['grade']} | {r['status']}")

        print("=" * 72 + "\n")


# ---------------------------
# Main (example run)
# ---------------------------
if __name__ == "__main__":
    # Example dataset (you can replace with your own)
    classroom_data = {
        "Alaa": [98, 92, 95, 97],
        "Ahmed": [45, 50, 48, 55],
        "Sara": [95, 88, 92, 97],
        "Omar": [60, 65, 58, 62],
        "NoScores": []
    }

    system = StudentGradingSystem(classroom_data, pass_mark=50)
    system.print_report(top_n=3)
