from typing import List, Dict

from app.github.client import get_pr_files


class PRService:
    """
    Service responsible for preparing Pull Request data
    for the AI review pipeline.

    Responsibilities:
    - Fetch changed files from GitHub
    - Normalize GitHub response
    - Detect programming language
    - Return AI-friendly objects
    """

    @staticmethod
    def get_changed_files(
        owner: str,
        repository: str,
        pr_number: int,
    ) -> List[Dict]:
        """
        Fetch changed files from a GitHub Pull Request and
        convert them into a normalized format.

        Returns:
        [
            {
                "filename": "login.py",
                "language": "Python",
                "status": "modified",
                "patch": "...",
                "additions": 10,
                "deletions": 2,
                "changes": 12
            }
        ]
        """

        github_files = get_pr_files(
            owner=owner,
            repo=repository,
            pr_number=pr_number,
        )

        normalized_files = []

        for file in github_files:

            normalized_files.append(
                {
                    "filename": file["filename"],
                    "language": PRService.detect_language(
                        file["filename"]
                    ),
                    "status": file["status"],
                    "patch": file.get("patch", ""),
                    "additions": file.get("additions", 0),
                    "deletions": file.get("deletions", 0),
                    "changes": file.get("changes", 0),
                }
            )

        return normalized_files

    @staticmethod
    def detect_language(filename: str) -> str:
        """
        Detect programming language
        from file extension.
        """

        if "." not in filename:
            return "Unknown"

        extension = filename.rsplit(".", 1)[1].lower()

        extension_map = {
            "py": "Python",
            "js": "JavaScript",
            "ts": "TypeScript",
            "jsx": "React",
            "tsx": "React",
            "java": "Java",
            "cpp": "C++",
            "cc": "C++",
            "cxx": "C++",
            "c": "C",
            "cs": "C#",
            "go": "Go",
            "rs": "Rust",
            "rb": "Ruby",
            "php": "PHP",
            "swift": "Swift",
            "kt": "Kotlin",
            "kts": "Kotlin",
            "scala": "Scala",
            "dart": "Dart",
            "sql": "SQL",
            "html": "HTML",
            "css": "CSS",
            "scss": "SCSS",
            "json": "JSON",
            "yaml": "YAML",
            "yml": "YAML",
            "xml": "XML",
            "sh": "Shell",
            "dockerfile": "Docker",
            "md": "Markdown",
        }

        return extension_map.get(
            extension,
            "Unknown",
        )